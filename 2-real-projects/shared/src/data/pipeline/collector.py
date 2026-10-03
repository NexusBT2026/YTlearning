"""
Data Collector Module: REST + WebSocket Unified Pipeline

This module demonstrates a production-grade data collection pattern that combines:
- REST API calls for historical/batch data (synchronous)
- WebSocket connections for real-time streaming (asynchronous)

Why this pattern?
  REST API: Stateless, reliable for historical data, easier debugging
  WebSocket: Persistent connection, low-latency updates, event-driven
  Combined: Get historical context + live updates in one pipeline

Architecture:
  1. Fetch historical data synchronously (blocking REST call)
  2. Stream live updates asynchronously (non-blocking WebSocket)
  3. Both run independently without blocking each other

Use case: Financial data collection (crypto, stocks), IoT sensor networks,
          real-time dashboards with historical context
"""

import asyncio                   # Provides async event loop and concurrency primitives
import logging                   # Provides logging for debugging and production visibility
from dotenv import load_dotenv   # Loads environment variables from .env
import os                        # Used for filesystem operations
from rich import print           # Rich print formatting for colored terminal output
import sys                       # Used to modify Python import paths
import csv                       # Used to write OHLCV and trade data to CSV files

# Add shared folder to Python path so imports work across episodes
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../'))

# Import REST and WebSocket client wrappers
from shared.src.data.rest_api.api_client import ApiClient
from shared.src.data.websockets.ws_client import WebsocketClient

# Load environment variables
load_dotenv()

# Configure logging output format and level
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)

# Create logger instance
logger = logging.getLogger(__name__)


class DataCollector:
    """
    Unified Data Collector: REST + WebSocket Pipeline
    
    Combines synchronous REST API calls with asynchronous WebSocket streaming.
    This is the canonical pattern for real-world data collection systems.
    
    Example for SPOT data:
        collector = DataCollector(
            rest_url="https://api.binance.com",
            ws_url_kline="wss://stream.binance.com:9443/ws/btcusdt@kline_1m",
            ws_url_trades="wss://stream.binance.com:9443/ws/btcusdt@trade"
        )
        await collector.run(stream_duration=60)  # Fetch history + stream 60s

    Example for futures data:
        collector = DataCollector(
            rest_url="https://api.binance.com",
            ws_url_kline="wss://fstream.binance.com/ws/btcusdt@kline_1m",
            ws_url_trades="wss://fstream.binance.com/ws/btcusdt@trade"
        )
    
    Attributes:
        rest (ApiClient): HTTPS REST client for historical data
        ws_kline (WebsocketClient): WebSocket client for OHLCV candles
        ws_trades (WebsocketClient): WebSocket client for trades
        historical_data (list): Cache of fetched historical records
        collecting (bool): Flag tracking if stream is active
    """

    def __init__(
        self,
        rest_url="https://api.binance.com",
        ws_url_kline="wss://stream.binance.com:9443/ws/btcusdt@kline_1m",
        ws_url_trades="wss://stream.binance.com:9443/ws/btcusdt@trade"
    ):
        # Create REST client for historical OHLCV data
        self.rest = ApiClient(rest_url)

        # Log REST endpoint configuration
        logger.info(f"REST endpoint configured: {rest_url}")

        # Create WebSocket client for OHLCV candle stream
        self.ws_kline = WebsocketClient(ws_url_kline)

        # Log OHLCV WebSocket endpoint configuration
        logger.info(f"WebSocket OHLCV endpoint configured: {ws_url_kline}")

        # Create WebSocket client for trade stream
        self.ws_trades = WebsocketClient(ws_url_trades)

        # Log trade WebSocket endpoint configuration
        logger.info(f"WebSocket trades endpoint configured: {ws_url_trades}")

        # Placeholder for historical OHLCV data fetched via REST
        self.historical_data = None

        # Flag indicating whether live streaming is active
        self.collecting = False

    # =====================================================================
    # FILESYSTEM HELPERS
    # =====================================================================

    def ensure_folder_exists(self, filename):
        # Extract folder path from filename
        folder = os.path.dirname(filename)

        # Check if folder path is not empty and does not exist
        if folder and not os.path.exists(folder):
            # Create folder and any missing parent directories
            os.makedirs(folder, exist_ok=True)

    # =====================================================================
    # CSV STORAGE HELPERS — OHLCV
    # =====================================================================

    def save_rest_to_csv(self, filename="2-real-projects/shared/src/data/ohlcv_data/BTC_ohlcv_data.csv"):
        """
        Save REST historical candles to CSV.

        REST candles are *finished* candles, so they can be written directly.
        Binance returns OHLCV as arrays, so each array becomes one CSV row.
        """
        # Check if historical_data is available before saving
        if not self.historical_data:
            # Print error message when no data is available
            print("[red]✗ Cannot save REST data: historical_data is None[/red]")
            # Exit function early
            return

        # Ensure the folder for the CSV file exists
        self.ensure_folder_exists(filename)

        # Define CSV header fields for OHLCV data
        header = [
            "open_time","open","high","low","close","volume",
            "close_time","quote_volume","num_trades",
            "taker_buy_base","taker_buy_quote","ignore"
        ]

        # Open CSV file in write mode
        with open(filename, "w", newline="") as f:
            # Create CSV writer instance
            writer = csv.writer(f)
            # Write header row
            writer.writerow(header)
            # Write all historical OHLCV rows
            writer.writerows(self.historical_data)

    def update_last_candle(self, kline, filename="2-real-projects/shared/src/data/ohlcv_data/BTC_ohlcv_data.csv"):
        """
        Update the last candle in the CSV file.

        WebSocket OHLCV stream sends the *live* candle.
        When kline["x"] == False → candle still forming → update last row.
        """
        # Ensure the folder exists before reading/writing CSV
        self.ensure_folder_exists(filename)

        # Open CSV file in read mode
        with open(filename, "r") as f:
            # Read all rows into memory
            rows = list(csv.reader(f))

        # Replace last row with updated OHLCV values from live candle
        rows[-1] = [
            kline["t"], kline["o"], kline["h"], kline["l"], kline["c"],
            kline["v"], kline["T"], kline["q"], kline["n"],
            kline["V"], kline["Q"], kline["B"]
        ]

        # Open CSV file in write mode to overwrite updated rows
        with open(filename, "w", newline="") as f:
            # Write updated rows back to CSV
            csv.writer(f).writerows(rows)

    def append_new_candle(self, kline, filename="2-real-projects/shared/src/data/ohlcv_data/BTC_ohlcv_data.csv"):
        """
        Append a new finished candle to CSV.

        When kline["x"] == True → Binance signals the candle is closed.
        The finished candle is appended as a new CSV row.
        """
        # Ensure the folder exists before appending CSV rows
        self.ensure_folder_exists(filename)

        # Open CSV file in append mode
        with open(filename, "a", newline="") as f:
            # Append new finished candle to CSV file
            csv.writer(f).writerow([
                kline["t"], kline["o"], kline["h"], kline["l"], kline["c"],
                kline["v"], kline["T"], kline["q"], kline["n"],
                kline["V"], kline["Q"], kline["B"]
            ])

    # =====================================================================
    # CSV STORAGE HELPERS — TRADES
    # =====================================================================

    def save_trade(self, trade, filename="2-real-projects/shared/src/data/trades/BTC_trades.csv"):
        """
        Save a single trade event to CSV.

        Each WebSocket trade message is written as one row with:
        event time, symbol, trade id, price, quantity, trade time, maker flag.
        """
        # Ensure folder exists before writing trade CSV
        self.ensure_folder_exists(filename)

        # Check if file already exists
        file_exists = os.path.isfile(filename)

        # Open CSV file in append mode
        with open(filename, "a", newline="") as f:
            # Create CSV writer instance
            writer = csv.writer(f)

            # Write header row only if file is new
            if not file_exists:
                writer.writerow([
                    "event_time", "symbol", "trade_id",
                    "price", "quantity", "trade_time",
                    "is_buyer_maker"
                ])

            # Write trade event fields to CSV
            writer.writerow([
                trade["E"], trade["s"], trade["t"],
                trade["p"], trade["q"], trade["T"],
                trade["m"]
            ])

    # =====================================================================
    # REST HISTORICAL FETCH
    # =====================================================================

    def fetch_historical(self):
        """
        Fetch historical candlestick (kline) data using Binance REST API.

        REST returns *arrays*, not objects:
        Each kline is a list of 12 values:

        [0] Open time (ms)
        [1] Open price
        [2] High price
        [3] Low price
        [4] Close price
        [5] Volume
        [6] Close time (ms)
        [7] Quote asset volume
        [8] Number of trades
        [9] Taker buy base volume
        [10] Taker buy quote volume
        [11] Ignore (always 0)

        Why REST for historical data?
        - Indexed: You can request exact time ranges
        - Stateless: No persistent connection required
        - Retryable: Safe to retry on network errors
        - Efficient: Server returns compressed arrays

        Return type:
        list[list] — A list of kline arrays
        """
        # Print status message for REST fetch
        print("[yellow]Fetching historical OHLCV data...[/yellow]")

        # Log REST fetch operation
        logger.info("Fetching historical klines from REST")

        try:
            # Perform REST GET request for OHLCV data
            data = self.rest.get("/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=10")

            # Check if REST returned valid data
            if data:
                # Print success message
                print("[green]✓ Historical data received[/green]")

                # Store historical OHLCV data
                self.historical_data = data

                # Save REST OHLCV data to CSV
                self.save_rest_to_csv()

                # Print confirmation message
                print("[green]✓ REST candles saved to CSV[/green]")

                # Return fetched data
                return data

            # Print error message when no data returned
            print("[red]✗ No historical data received[/red]")

            # Return None when no data available
            return None

        except Exception as e:
            # Print error message when REST fetch fails
            print(f"[red]✗ Error fetching historical data:[/red] {e}")

            # Return None on exception
            return None

    # =====================================================================
    # WEBSOCKET HANDLERS
    # =====================================================================

    def handle_ws_kline(self, msg):
        """
        Handle incoming OHLCV WebSocket kline messages.

        The payload `msg["k"]` contains the live candle:
        - If k["x"] == False → candle still forming → update last CSV row
        - If k["x"] == True  → candle closed        → append new CSV row
        """
        # Extract kline payload from WebSocket message
        k = msg["k"]

        # Check if candle is still forming
        if k["x"] == False:
            # Print update message
            print("[yellow]Updating current candle...[/yellow]")

            # Update last candle in CSV
            self.update_last_candle(k)
        else:
            # Print new candle message
            print("[green]New candle closed → appending[/green]")

            # Append finished candle to CSV
            self.append_new_candle(k)

    def handle_ws_trade(self, msg):
        """
        Handle incoming trade WebSocket messages.

        WebSocket sends JSON trade events with fields:
        - Price, quantity, trade time, symbol, trade id, maker flag, etc.
        Each event is printed and then saved to the trades CSV file.
        """
        # Print readable trade event information
        print(f"[magenta]TRADE EVENT[/magenta] → Price={msg['p']} Qty={msg['q']} Time={msg['T']}")

        # Save trade event to CSV
        self.save_trade(msg)

    # =====================================================================
    # WEBSOCKET STREAMERS
    # =====================================================================

    async def stream_live_kline(self):
        """
        Stream real-time OHLCV data using WebSocket asynchronously.

        This connects to the kline_1m stream and passes each message
        to `handle_ws_kline`, which updates or appends candles in CSV.
        """
        # Print status message for OHLCV stream
        print("[yellow]Starting OHLCV WebSocket stream...[/yellow]")

        try:
            # Connect to OHLCV WebSocket and process messages via callback
            await self.ws_kline.connect(on_message=self.handle_ws_kline)
        except KeyboardInterrupt:
            # Print stop message when interrupted
            print("\n[yellow]OHLCV stream stopped[/yellow]")

            # Update collecting flag
            self.collecting = False

    async def stream_live_trades(self):
        """
        Stream real-time trade data using WebSocket asynchronously.

        This connects to the trade stream and passes each message
        to `handle_ws_trade`, which prints and saves trades to CSV.
        """
        # Print status message for trade stream
        print("[yellow]Starting trade WebSocket stream...[/yellow]")

        try:
            # Connect to trade WebSocket and process messages via callback
            await self.ws_trades.connect(on_message=self.handle_ws_trade)
        except KeyboardInterrupt:
            # Print stop message when interrupted
            print("\n[yellow]Trade stream stopped[/yellow]")

            # Update collecting flag
            self.collecting = False

    # =====================================================================
    # MAIN PIPELINE
    # =====================================================================

    async def run(self, stream_duration=10):
        """
        Execute the complete data collection pipeline.
        
        Pipeline stages:
        1. Fetch historical data (BLOCKING: waits for REST response)
           - Gives context: recent price history and candles
        2. Stream live updates (ASYNC: listens for WebSocket events)
           - OHLCV candles via kline stream
           - Trades via trade stream
           - Both run concurrently for `stream_duration` seconds
        
        Args:
            stream_duration (int): Number of seconds to collect live data.
        """
        # Print status message for REST fetch
        print("[cyan]Fetching REST historical candles...[/cyan]")

        # Fetch historical OHLCV data
        self.fetch_historical()

        # Print status message for WebSocket streams
        print("[cyan]Starting WebSocket streams...[/cyan]")

        try:
            # Run OHLCV and trade streams concurrently with timeout
            await asyncio.wait_for(
                asyncio.gather(
                    self.stream_live_kline(),
                    self.stream_live_trades()
                ),
                timeout=stream_duration
            )
        except asyncio.TimeoutError:
            # Print timeout message
            print("[yellow]Streaming duration complete[/yellow]")
        except KeyboardInterrupt:
            # Print stop message when interrupted
            print("\n[yellow]Streaming stopped[/yellow]")

            # Update collecting flag
            self.collecting = False

        # Print completion message
        print("[cyan]Data Collection Complete[/cyan]")


# Run module when executed directly
if __name__ == "__main__":
    # Log module load event
    logger.info("DataCollector module loaded")
