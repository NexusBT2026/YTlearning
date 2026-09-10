# Story 2-1: Building a Reusable REST API Client

## Overview

This is the foundation episode of the **Real Projects series**. We build a reusable REST API client that becomes the base for all subsequent modules: data collectors, automation tools, dashboards, trading bots, and the full Liquidator ecosystem.

**No theory — only practical, production-ready code.**

## What We Build

✅ **ApiClient class** with configurable base URL and timeout
✅ **GET and POST methods** with proper error handling
✅ **JSON parsing** and response validation
✅ **Environment variable support** for secure API key management
✅ **Logging infrastructure** for debugging and monitoring
✅ **Exception handling** with graceful error recovery
✅ **Demo script** that validates everything works

## Files Created

```
2-real-projects/
├── 2-1-reusable-api/
│   ├── code/
│   │   ├── client.py          # ApiClient class
│   │   └── demo.py            # Test/demo script
│   ├── script/
│   │   └── script.md          # Video script
│   ├── assets/
│   │   └── ASSETS.md          # Production assets checklist
│   └── README.md              # This file
└── (also uses root .env)
```

## Key Concepts

| Concept | Why | How |
|---------|-----|-----|
| **Reusability** | Foundation for all other modules | Base URL + methods in class |
| **Security** | API keys never in code | Environment variables via .env |
| **Error Handling** | Production reliability | Try/catch with logging |
| **Logging** | Debugging and monitoring | Python logging module |
| **JSON Parsing** | Data consistency | Built into requests library |
| **Timeouts** | Prevent hangs | Configurable per request |

## Dependencies
# Via pip (Windows / macOS / Linux)
```bash
pip install requests python-dotenv rich
```

## Next Story

Story 2-2: **Building a Websocket Client** — the real-time counterpart to this REST client.

---

**Duration:** 6-7 minutes  
**Difficulty:** Beginner+  
**Prerequisites:** Basic Python, pip or uv
