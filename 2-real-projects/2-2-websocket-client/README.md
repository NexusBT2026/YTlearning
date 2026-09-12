# Story 2-2: Real-Time WebSocket Client

## Overview

This episode teaches building a production-ready WebSocket client in Python using async/await patterns. Viewers will learn how to:
- Connect to WebSocket servers
- Listen for real-time messages
- Handle connection errors gracefully
- Load authentication from environment variables
- Integrate with Story 2-1's REST API Client

## Key Concepts

**WebSocket vs REST API:**
- REST: Request/response polling (asks for data repeatedly)
- WebSocket: Persistent connection (server pushes data instantly)
- Use case: Real-time dashboards, trading bots, live notifications

**Async/Await in Python:**
- `async def`: Defines an asynchronous function
- `await`: Pauses execution until async operation completes
- `asyncio.run()`: Runs async code from synchronous context
- Enables concurrent operations without threading

**Class Design:**
- `__init__()`: Store configuration (WebSocket URL, API key)
- `async connect()`: Establish WebSocket connection
- `async listen()`: Handle incoming messages
- Separate error handling for connection vs message phases

## Code Structure

### File: `code/client.py`
**WebsocketClient class** with async methods:
- Loads API_KEY from root .env file
- Connects to any WebSocket server (public or authenticated)
- Listens for real-time messages with error handling
- Prints formatted output using Rich library

### File: `code/demo.py`
**Simple test script** that:
- Creates a WebsocketClient instance
- Connects to Postman Echo (free public WebSocket test server)
- Prints received messages in real-time

### File: `code/requirements.txt`
**Python dependencies:**
- requests (HTTP requests)
- websockets (WebSocket protocol)
- python-dotenv (environment variables)
- rich (terminal formatting)

### File: `code/.env.example`
**Environment template** showing optional API_KEY configuration

## Files Created

```
2-real-projects/
├── 2-2-websocket-client/
│   ├── code/
│   │   ├── client.py          # WebsocketClient class
│   │   ├── demo.py            # Test/demo script
│   │   ├── requirements.txt   # Python dependencies
│   │   └── .env.example       # Environment template
│   ├── script/
│   │   └── script.md          # Video script
│   ├── assets/
│   │   └── ASSETS.md          # Production assets checklist
│   └── README.md              # This file
└── (also uses root .env)
```

## Dependencies on Previous Stories

**Story 2-1 (REST API Client):**
- Uses same logging pattern (basicConfig)
- Uses same Rich output formatting ([green], [cyan])
- Uses same .env location (YTlearning/.env)
- Follows same error handling philosophy
- WebSocket and REST clients will be combined in Story 2-3

**Shared Patterns:**
```python
# From Story 2-1, reused in 2-2:
load_dotenv()  # Load root .env file
logging.basicConfig(format="%(asctime)s — %(levelname)s — %(message)s")
from rich import print
print(f"[green]Message[/green]")
```

## Acceptance Criteria Coverage

✅ **Understand WebSocket basics** — Intro explains connection lifecycle vs polling
✅ **Implement async WebsocketClient** — Class with async connect() and listen()
✅ **Handle connection errors** — Try/except wraps connection phase
✅ **Handle listen errors** — Try/except wraps message listening phase
✅ **Load API_KEY from env** — Uses os.getenv("API_KEY")
✅ **Use asyncio patterns** — async/await with asyncio.run()
✅ **Test with demo script** — demo.py runs client against Postman Echo
✅ **Understand WebSocket vs REST** — Recap section compares approaches

## Testing Recommendations

**Manual Testing:**
```bash
# Install dependencies
pip install -r 2-real-projects/2-2-websocket-client/code/requirements.txt

# Run demo
cd 2-real-projects/2-2-websocket-client/code
python demo.py
```

**Expected Output:**
```
✓ Connects to wss://ws.postman-echo.com/raw
✓ Prints "[green]Connected to wss://...[/green]"
✓ Listens for messages from server
```

## Next Story Integration

**Story 2-3 (Data Collector)** will:
- Import WebsocketClient from 2-2
- Import ApiClient from 2-1
- Combine both into unified DataCollector class
- Show real async coordination (REST polling + WebSocket streaming)

## Production Notes

- **Duration:** 7-8 minutes of video
- **Audience:** Python intermediate developers
- **Difficulty:** Medium (async/await concepts required)
- **Hardware:** CPU-only, works on any laptop or desktop
- **Network:** Requires internet for WebSocket demo

## Quality Gates

✅ Story specification matches 2-1 structure
✅ Code follows architecture standards from Story 2-1
✅ async/await patterns properly documented
✅ Error handling includes both connection and listen phases
✅ Demo uses public, free WebSocket server (Postman Echo)
✅ No external API key required for demo
✅ README and assets complete
✅ Ready for video recording and publication

---

**Duration:** 7-8 minutes
**Difficulty:** Medium+
**Prerequisites:** Basic Python, pip or uv