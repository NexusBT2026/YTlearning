# Story 2-3: Unified Data Collector

## Overview

This episode teaches building a production-ready Data Collector in Python that combines REST API (for historical data) and WebSocket (for real-time streams) into a single, coordinated pipeline.

This episode teaches how to build a production‑ready Data Collector in Python that combines:
- REST API (for historical OHLCV candles)
- WebSocket streaming (for both OHLCV candles and trades)
- CSV storage for historical and live data
- Real‑time candle updating and appending
- Dual WebSocket streaming using asyncio.gather
- Callback‑based message handling

Viewers learn how to:
- Fetch historical OHLCV data using REST
- Stream live OHLCV candles
- Stream live trades
- Update the last candle while it’s forming
- Append new candles when they close
- Save all data to CSV files
- Run both WebSocket streams concurrently
- Prepare data for downstream modules (Strategy Engine, Dashboards, Trading Bots)

## Key Concepts

### REST vs WebSocket

**REST API (Historical Data):**
- Request/response pattern: Ask the server for data
- Synchronous: Wait for response before continuing
- Good for: Historical data, batch operations, occasional queries
- Binance example: Fetch last 10 minutes of OHLCV candlesticks

**WebSocket (Real-Time Streaming):**
- Persistent connection: Server pushes data continuously
- Asynchronous: Receive updates without asking
- Good for: Live updates, continuous monitoring, event-driven systems
- Two independent streams:
    - OHLCV candles (kline_1m)
    - Trades (@trade)

**Unified Approach:**
- Start with historical context (REST)
- Transition to live updates (WebSocket)
- Combine both in a single pipeline
- Useful for dashboards, trading systems, analytics

### Async/Await Patterns in Python

**Synchronous vs Asynchronous:**
- `fetch_historical()`: Synchronous method (blocks until complete)
- `stream_live()`: Asynchronous OHLCV stream method (async def, await, concurrent)
- `stream_live_trades()`: Asynchronous trade stream method (async def, await, concurrent)
- `run()`: Starts both WebSocket streams concurrently using asyncio.gather

**Key Patterns Used:**
```python
async def method_name():     # Defines async function
    await other_async()      # Waits for async operation
    asyncio.gather()         # Runs async code from sync context
    asyncio.wait_for()       # Sets timeout on async operation
```

### Class Design

**DataCollector Architecture:**
- `__init__()`: Stores REST client, OHLCV WebSocket client, and trade WebSocket client
- `fetch_historical()`: Synchronous OHLCV data fetch and saves them to CSV (uses ApiClient)
- `handle_ws_kline()`: Updates the current candle or appends a new one
- `handle_ws_trade()`: Saves each trade to CSV
- `stream_live_kline()`: Asynchronous OHLCV stream (uses WebsocketClient)
- `stream_live_trades()`: Asynchronous trade stream (uses WebsocketClient)
- `run()`: Orchestrates pipeline (REST then WebSocket)
- Error handling: Separate try/except for each connection type

**Integration Pattern:**
```python
from shared.api_client import ApiClient       # Story 2-1
from shared.ws_client import WebsocketClient  # Story 2-2

class DataCollector:
    def __init__(self):
        self.rest = ApiClient(...)            # Composed REST client
        self.ws_kline = WebsocketClient(...)  # Composed WebSocket client
        self.ws_trades = WebsocketClient(...) # Composed WebSocket client
```

## Code Structure

### File: `code/collector.py`

**DataCollector class** with mixed sync/async methods:
- Loads configuration for Binance endpoints (REST and WebSocket)
- `fetch_historical()`: Synchronously fetches BTC/USDT 1-minute candlesticks and saves them to CSV
- `handle_ws_kline()`: Updates or appends candles in real time
- `handle_ws_trade()`: Saves trade events to CSV
- `stream_live_kline()`: Asynchronously listens to live OHLCV candle updates
- `stream_live_trades()`: Asynchronously streams trades
- `run()`: Runs both WebSocket streams concurrently using asyncio.gather
- Proper logging for all operations
- Rich console output for formatted display

### File: `code/demo.py`

**Test script** that:
- Imports DataCollector from collector.py
- Creates instance with REST, OHLCV WebSocket, and trade WebSocket endpoints
- Runs `collector.run(stream_duration=30)`
- Streams OHLCV candles and trades concurrently
- Saves all data to CSV
- Handles KeyboardInterrupt (Ctrl+C) gracefully
- Logs all operations with proper error handling
- Demonstrates both REST and WebSocket working together

### File: `code/requirements.txt`

**Python dependencies:**
- `requests` — HTTP library for REST API calls
- `websockets` — WebSocket protocol implementation
- `python-dotenv` — Environment variable loading
- `rich` — Terminal formatting and colors

### File: `code/.env.example`

**Environment template** showing optional configuration.
Note: Binance public market data requires NO authentication, so .env can be empty.

## Dependencies on Previous Stories

### Story 2-1 (REST API Client):
- Imports `ApiClient` class: `from api_client.client import ApiClient`
- Uses same .env location: `YTlearning/.env`
- Follows same logging pattern: `logging.basicConfig(format="...")`
- Uses same Rich formatting: `from rich import print` with `[green]`, `[red]` tags
- Shares error handling philosophy: Try/except with user-friendly messages

### Story 2-2 (WebSocket Client):
- Imports `WebsocketClient` class: `from websocket_client.client import WebsocketClient`
- Uses same async/await patterns: `async def`, `await self.ws.connect()`
- Uses same Rich output: Colored terminal messages for status
- Follows same connection lifecycle: Connect → Listen → Handle errors → Disconnect

### Shared Patterns Across All Three Stories:
```python
# Common pattern from Story 2-1 and 2-2:
from dotenv import load_dotenv
from rich import print
import logging

load_dotenv()
logging.basicConfig(format="%(asctime)s — %(levelname)s — %(message)s")

# Story 2-3 combines both approaches:
# - REST: Synchronous operations (from Story 2-1)
# - WebSocket: Asynchronous operations (from Story 2-2)
```

## Project Structure

```
YTlearning/
├── .env                                    # Shared configuration
├── 2-real-projects/
│   ├── 2-1-reusable-api/
│   |   └── code/
│   │       ├── client.py                  # Story 2-1
│   │       └── demo.py
│   │
│   ├── 2-2-websocket-client/
│   |   └── code/
│   │       ├── .env.example               # Story 2-2
│   │       ├── client.py
│   │       ├── demo.py
│   │       └── requirements.txt
│   │
│   └── data_collector/                    # Story 2-3
│       ├── code/
│       │   ├── collector.py               # DataCollector class
│       │   ├── demo.py                    # Test script
│       │   ├── requirements.txt           # Dependencies
│       │   └── .env.example               # Config template
│       ├── script/
│       │   └── script.md                  # Video script
│       ├── assets/
│       │   └── ASSETS.md                  # Production checklist
│       └── README.md                      # This file
|
├── shared/                                # shared code folder for the whole series cause python modules cannot start with numbers!
│   └── code/
│       ├── api_client.py
│       └── ws_client.py
```

## Acceptance Criteria Coverage

✅ **Understand data collection patterns** — Explains REST vs Dual WebSocket vs unified approach  
✅ **Implement DataCollector class** — Complete class with fetch_historical() and stream_live()  
✅ **Handle mixed sync/async** — fetch_historical() is sync, stream_live() is async, run() orchestrates  
✅ **Coordinate REST and WebSocket** — Both run in sequence with proper lifecycle management  
✅ **Handle errors independently** — Separate try/except for REST and WebSocket  
✅ **Load configuration from .env** — Uses python-dotenv (though no API key needed for Binance)  
✅ **Use asyncio patterns** — async/await with asyncio.gather() and asyncio.wait_for()  
✅ **Integrate with previous modules** — Imports ApiClient and WebsocketClient  
✅ **Test with demo script** — demo.py uses real Binance data (public API)  
✅ **Proper logging** — All operations logged with timestamps and levels  
✅ **CSV saving** — OHLCV + trades saved to disk
✅ **Real‑time candle updating** — update last candle + append new candle

## Testing Recommendations

### Manual Testing (Recommended)

**Setup:**
```bash
# Install dependencies
pip install -r 2-real-projects/2-3-data-collector/code/requirements.txt
```

### Navigate to code folder
```bash
cd 2-real-projects/2-3-data-collector/code
```

### Ensure shared folder exist and its needed files
```bash
ls 2-real-projects/shared/api_client.py
ls 2-real-projects/shared/ws_client.py
```

### OR
```bash
get-Item 2-real-projects/shared/api_client.py
get-Item 2-real-projects/shared/ws_client.py
```

## Else copy the files from the previous stories
### 🗐 Copy files (Windows PowerShell) 
```powershell
Copy-Item YTlearning/2-real-projects/2-1-reusable-api/code/client.py -Destination YTlearning/2-real-projects/shared/api_client.py
Copy-Item YTlearning/2-real-projects/2-2-websocket-client/code/client.py -Destination YTlearning/2-real-projects/shared/ws_client.py
```

### 🗐 Copy files (Windows CMD)
```cmd
copy YTlearning\2-real-projects\2-1-reusable-api\code\client.py YTlearning\2-real-projects\shared\api_client.py
copy YTlearning\2-real-projects\2-2-websocket-client\code\client.py YTlearning\2-real-projects\shared\ws_client.py
```

### 🗐 Copy files (macOS / Linux)
```bash
cp YTlearning/2-real-projects/2-1-reusable-api/code/client.py YTlearning/2-real-projects/shared/api_client.py
cp YTlearning/2-real-projects/2-2-websocket-client/code/client.py YTlearning/2-real-projects/shared/ws_client.py
```
## 🚨 then only adjust the ws_client with this: WebSocket Client Improvements
WebSocket Client Improvements
In Story 2‑2, the WebSocket client only printed incoming messages:

```python
async def connect(self):
    async with websockets.connect(self.url) as ws:
        await self.listen(ws)

async def listen(self, ws):
    async for message in ws:
        print(message)
```

This worked for simple demos, but it had two major limitations:

1. ❌ No way to pass messages back to other modules
The DataCollector needs to process messages, not just print them.
The old client could not:
    - update candles
    - append new candles
    - save trades
    - run custom logic
    - integrate with Strategy Engine


2. ❌ No JSON parsing
Binance sends JSON strings.
The old client printed raw text, forcing every module to parse JSON manually.

✔ What We Added. 

To support the DataCollector, we added callback support and JSON parsing.

✔ 1. Added on_message callback.

This allows the DataCollector to pass a handler function:

```python
await self.ws_kline.connect(on_message=self.handle_ws_kline)
await self.ws_trades.connect(on_message=self.handle_ws_trade)
```

✔ 2. Added JSON parsing inside the client.

The improved client automatically converts raw WebSocket text into Python dictionaries:

```python
msg = json.loads(raw)
```

✔ 3. Added conditional behavior.

If a callback is provided → pass parsed message to it
If not → print the message (same behavior as before)

✔ 4. Added improved listen loop.

The new listen method handles:
- JSON parsing
- invalid JSON
- callback dispatch
- default printing

✔ Final Improved WebSocket Client
```python
async def connect(self, on_message=None):
    async with websockets.connect(self.url) as ws:
        await self.listen(ws, on_message)

async def listen(self, ws, on_message=None):
    async for raw in ws:
        msg = json.loads(raw)

        if on_message:
            on_message(msg)
        else:
            print(msg)
``` 
Why This Change Was Necessary?

✔ Required for DataCollector

The DataCollector needs to:
- Update the last candle
- Append new candles
- Save trades
- Run two WebSocket streams at once
- Pass messages to handler functions

The old WebSocket client could not do any of this.

✔ Required for Strategy Engine
    
The Strategy Engine (next video) needs:
- Parsed messages
- Structured data
- Callback‑driven logic

✔ Required for Dashboards

Dashboards need:
- Structured OHLCV data
- Structured trade data
- Real‑time updates

**Run Demo:**
```bash
# Run the demo script (will stream for 10 seconds then stop)
python demo.py

# Expected output:
# ✓ Fetches historical BTC/USDT candlesticks (10 1-minute bars)
# ✓ Shows historical data timestamps and prices
# ✓ Connects to Binance WebSocket for live trades
# ✓ Prints incoming trade messages
# ✓ Stops after 10 seconds
# ✓ All output formatted with Rich colors
```

**Stopping Early:**
```bash
# Press Ctrl+C during execution to stop the WebSocket stream
# Demo handles KeyboardInterrupt gracefully
```

### Expected Behavior

**Phase 1 — Fetch Historical:**
```
Fetching historical data...
✓ Historical data received:
✓ REST candles saved to CSV:
  Last kline timestamp: 1694265600000
  Open: 26000.00, Close: 26050.00
```

**Phase 2 — Stream Live (30 seconds):**
```
Starting OHLCV WebSocket stream...
Starting trade WebSocket stream...
Updating current candle...
New candle closed → appending
TRADE EVENT → Price=..., Qty=..., Time=...
```

**Completion:**
```
Streaming duration complete
Data Collection Complete
```

### Troubleshooting

**Error: "No module named 'api_client'"**
- Ensure 2-1-reusable-api folder exists at 2-real-projects/api_client/
- The collector.py file uses sys.path.insert to import from sibling modules

**Error: "WebSocket connection failed"**
- Check internet connection
- Verify Binance WebSocket server is accessible
- Binance endpoint: wss://stream.binance.com:9443/ws/btcusdt@trade

**Error: "requests not found"**
- Install requirements: `pip install -r requirements.txt`
- Or individual package: `pip install requests`

**Error: "asyncio" not available**
- Requires Python 3.7+
- Check Python version: `python --version`
- Use `python3` instead of `python` if needed

## Integration Points

### Used By:
- **Story 2-4 (Strategy Engine):** Processes DataCollector output to make decisions
- **Story 2-5 (Dashboard):** Displays real-time and historical data from collector
- **Future modules:** Any system needing coordinated REST + WebSocket data

### Uses:
- **Story 2-1 (ApiClient):** REST API client for historical data fetch
- **Story 2-2 (WebsocketClient):** WebSocket client for real-time streams

### Shared Resources:
- `.env` file: Root configuration (empty for Binance public data)
- `logging`: Shared logging configuration pattern
- `rich`: Shared output formatting library

## Next Story

Following this story is **Story 2-4: Strategy Engine**, which processes the collected data to make automated decisions based on conditions and thresholds.

The data pipeline becomes:
1. DataCollector (2-3): Gathers data
2. StrategyEngine (2-4): Makes decisions
3. Dashboard (2-5): Visualizes results
4. ... and more

## Quick Reference

### Run the Demo:
```bash
cd 2-real-projects/2-3-data-collector/code 
python demo.py
```

### Modify Configuration:
Edit `collector.py` to change:
- REST endpoint: `rest_url` parameter
- WebSocket endpoint: `ws_url` parameter
- Stream duration: Pass different `stream_duration` to `run()`

### Add Your Own Integration:
```python
from data_collector.code.collector import DataCollector

collector = DataCollector()
historical = collector.fetch_historical()
# Use historical data...
await collector.stream_live()  # Listen for updates
```

---

**Status:** ✅ Ready for Implementation  
**Duration:** 20-21 minutes
**Difficulty:** Intermediate (requires async understanding)  
**Prerequisites:** Story 2-1 and 2-2 completed
