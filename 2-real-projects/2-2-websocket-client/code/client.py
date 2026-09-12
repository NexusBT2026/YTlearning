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

    async def connect(self):
        """Connect to the WebSocket server and start listening."""
        try:
            async with websockets.connect(
                self.url,
                #extra_headers={"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}
            ) as ws:
                print(f"[green]Connected to {self.url}[/green]")
                await self.listen(ws)
        except Exception as e:
            logging.error(f"Websocket connection error: {e}")

    async def listen(self, ws):
        """Listen for real-time messages from the WebSocket."""
        try:
            async for message in ws:
                print(f"[cyan]Received:[/cyan] {message}")
        except Exception as e:
            logging.error(f"Websocket listen error: {e}")
