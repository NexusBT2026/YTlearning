import asyncio
from client import WebsocketClient

# Create WebSocket client and connect to public test server
ws = WebsocketClient("wss://ws.postman-echo.com/raw")

# Run the async connection
asyncio.run(ws.connect())
