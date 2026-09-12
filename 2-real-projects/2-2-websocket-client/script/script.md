# Real Projects — Episode 2 — Building a Real-Time Websocket Client in Python

## INTRO

"Welcome back!
In the last video, we built the REST API Client — the foundation for all future Real Projects.

Today we're building the real‑time counterpart: a Websocket Client that listens to live data streams, receives updates instantly, and integrates directly into the Liquidator ecosystem.

No theory — only real, practical code that works."

## SECTION 1 — Required Installs (pip + environment)

"Before we start coding, let's install the required packages.

If you followed Episode 1, you already have python-dotenv and rich installed.
In that case, you only need to install websockets.

If you're starting from this episode, install all three packages."

**Install on Windows / macOS / Linux (pip):**
```bash
pip install websockets
pip install python-dotenv
pip install rich
```

**On Linux/macOS with pip3:**
```bash
pip3 install websockets python-dotenv rich
```

**Using uv (recommended for faster installs):**
#### 🐧 Linux / macOS / WSL
##### ✔ Standard (most common)
```bash
pip install websockets
```

##### ✔ If pip is mapped to Python 2 (older systems)
```bash
pip3 install websockets
```

##### ✔ If pip/pip3 are missing but python works
```bash
python -m pip install websockets
```

##### ✔ If Python is installed as `python` (macOS Homebrew)
```bash
python -m pip install websockets
```

#### 🪟 Windows PowerShell

##### ✔ Standard (recommended)
```powershell
pip install websockets
```

##### ✔ If pip is not found but Python works
```powershell
python -m pip install websockets
```

##### ✔ If Python is installed from Microsoft Store
```powershell
py -m pip install websockets
```

##### ✔ If pip is broken (rare)
```powershell
python -m ensurepip --upgrade
python -m pip install websockets
```

#### 🪟 Windows CMD (legacy)

##### ✔ CMD version
```cmd
pip install websockets
```

##### ✔ CMD fallback
```cmd
py -m pip install websockets
```

"These packages allow us to connect to websocket servers, load environment variables, and print clean logs."

## SECTION 2 — Project Structure

"Let's create the project structure for this module."

**Create folders:**
```bash
mkdir -p YTlearning/2-real-projects/websocket_client
```

**Create files (Linux/macOS):**
```bash
touch YTlearning/2-real-projects/websocket_client/client.py
touch YTlearning/2-real-projects/websocket_client/demo.py
```

**Create files (Windows PowerShell):**
```powershell
New-Item -Path YTlearning/2-real-projects/websocket_client/client.py -ItemType File
New-Item -Path YTlearning/2-real-projects/websocket_client/demo.py -ItemType File
```

**Final structure:**
```
YTlearning/
    .env
    2-real-projects/
        api_client/
            client.py
            demo.py
        websocket_client/
            client.py
            demo.py
```

"This keeps the module clean, organized, and ready for integration into larger systems."

## SECTION 3 — Creating the Websocket Client Class

"Now that the structure is ready, let's build the actual client.

We'll create a class that:
- connects to a websocket server
- listens for real‑time messages
- prints clean output
- handles disconnects
- loads API keys from the root .env
- uses async functions for concurrency"

**File: client.py**

```python
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
        try:
            async with websockets.connect(
                self.url,
                extra_headers={"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}
            ) as ws:
                print(f"[green]Connected to {self.url}[/green]")
                await self.listen(ws)
        except Exception as e:
            logging.error(f"Websocket connection error: {e}")

    async def listen(self, ws):
        try:
            async for message in ws:
                print(f"[cyan]Received:[/cyan] {message}")
        except Exception as e:
            logging.error(f"Websocket listen error: {e}")
```

"This client is production-ready. It handles connection errors, loads environment variables, and uses async/await for real-time concurrency."

## SECTION 4 — Testing the Websocket Client with a Demo Script

"Now that the client is ready, let's test it with a simple demo."

**File: demo.py**

```python
import asyncio
from client import WebsocketClient

ws = WebsocketClient("wss://ws.postman-echo.com/raw")

asyncio.run(ws.connect())
```

“This confirms that the client connects, does not receive messages, and does not prints real‑time updates for now, cause this is only a test server in the following episodes we will work with real data and messages and prints will be a fact then.”

## SECTION 5 — Using Environment Variables

“So as we saw. We don't need the API key yet, but before running the project, make sure your root .env file contains your API key. We will need it later in the project! (or leave it empty for public APIs)."

**Root .env (located at YTlearning/.env):**

```bash
# Optional API_KEY for authenticated websocket servers
# API_KEY=your_api_key_here
```

"This keeps your secrets out of your code. For public WebSocket servers like Postman Echo, you can leave API_KEY empty."

## SECTION 6 — Recap & Next Video

"Quick recap:

We installed the required packages, created the project structure, built the Websocket Client class, added logging and environment variables, tested the module with a demo script, and prepared the foundation for all future Real Projects.

The WebSocket client is now ready to:
- Connect to any WebSocket server
- Handle real-time messages
- Integrate with Story 2-1's REST API Client
- Feed into Story 2-3's Data Collector

In the next video, we'll build the Data Collector — combining REST + Websocket into a unified data pipeline.

If this helped you, leave a like and subscribe. And tell me in the comments what Real Project you want next!"

---
## 📌 Timestamps

- 00:00 – Intro
- 00:27 – Required installs
- 01:45 – Project structure
- 04:32 – Building the Websocket Client class
- 05:50 – Testing the client
- 06:30 – Adding environment variables
- 07:15 – Recap & next video

## Key Takeaways

✅ Websocket client foundation for all future Real Projects
✅ Environment variable support for secure API key management
✅ Logging infrastructure for debugging
✅ async/await support
✅ Error handling and exception management

## Requirements

- Python 3.8+
- pip package manager
- requests library
- python-dotenv library
- rich library
- websockets library
