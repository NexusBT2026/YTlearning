import asyncio
import websockets
import logging
from dotenv import load_dotenv
import os
from rich import print

# Load the root .env file
load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)

class WebsocketClient:
    def __init__(self, url: str):
        self.url = url
        self.api_key = os.getenv("API_KEY")

    async def connect(self, on_message=None):
        """
        Connect to the WebSocket server.

        on_message:
            A callback function provided by the DataCollector.
            If provided, every incoming message is passed to it.
            If not provided, messages are simply printed.
        """
        try:
            async with websockets.connect(
                self.url,
                #extra_headers={"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}
            ) as ws:
                print(f"[green]Connected to {self.url}[/green]")
                await self.listen(ws, on_message)
        except Exception as e:
            logging.error(f"Websocket connection error: {e}")

    async def listen(self, ws, on_message=None):
        """
        Listen for real-time messages.

        If on_message is provided:
            - Pass parsed JSON messages to the callback.
        If not:
            - Print raw messages.
        """
        try:
            async for raw in ws:
                try:
                    # Binance always sends JSON
                    import json
                    msg = json.loads(raw)
                except Exception:
                    print(f"[red]Invalid JSON:[/red] {raw}")
                    continue

                if on_message:
                    # Pass parsed message to DataCollector handler
                    on_message(msg)
                else:
                    # Default behavior: print raw message
                    print(f"[cyan]Received:[/cyan] {msg}")

        except Exception as e:
            logging.error(f"Websocket listen error: {e}")
