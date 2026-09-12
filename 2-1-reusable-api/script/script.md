# Real Projects — Episode 1 — REST API Client

🎬 YouTube title  
Real Projects — Episode 1 — Building a Reusable REST API Client in Python

## INTRO

"Welcome back!
Today we start the very first Real Project: building a reusable REST API Client that becomes the foundation for all future modules in this series.

This client will be used in data collectors, automation tools, dashboards, trading bots, and the Liquidator ecosystem.
No theory — only real, practical code that works."

## SECTION 1 — Required Installs (pip + environment)

"Before we start coding, let's install the required packages. I already prepared the code, which you can find back on GitHub later, so the video's don't take too much of your time. As you can see I used the bmad agent to create the project files. After I made the scripts myself."

Terminal:

📦 Windows / macOS / Linux (pip)
```bash
pip install requests 
pip install python-dotenv
pip install rich
```

🐧 Linux/macOS note
"On Linux/macOS, some systems require pip3 instead of pip:

```bash
pip3 install requests python-dotenv rich
```

"These packages allow us to send HTTP requests, load environment variables, and print clean logs."

"If you're using uv (recommended):"

#### 🐧 Linux / macOS / WSL

##### ✔ Standard (most common)
```bash
pip install requests
```

##### ✔ If pip is mapped to Python 2 (older systems)
```bash
pip3 install requests
```

##### ✔ If pip/pip3 are missing but python works
```bash
python -m pip install requests
```

##### ✔ If Python is installed as `python` (macOS Homebrew)
```bash
python -m pip install requests
```

#### 🪟 Windows PowerShell

##### ✔ Standard (recommended)
```powershell
pip install requests
```

##### ✔ If pip is not found but Python works
```powershell
python -m pip install requests
```

##### ✔ If Python is installed from Microsoft Store
```powershell
py -m pip install requests
```

##### ✔ If pip is broken (rare)
```powershell
python -m ensurepip --upgrade
python -m pip install requests
```

#### 🪟 Windows CMD (legacy)

##### ✔ CMD version
```cmd
pip install requests
```

##### ✔ CMD fallback
```cmd
py -m pip install requests
```

## SECTION 2 — Project Structure

"Let's create the project structure for this module."

📁 Create folders (works on all systems)
```bash
mkdir -p YTlearning/2-real-projects/2-1-reusable-api
```

📄 Create files (Linux/macOS)
```bash
touch YTlearning/.env
touch YTlearning/2-real-projects/2-1-reusable-api/code/client.py
touch YTlearning/2-real-projects/2-1-reusable-api/code/demo.py
```

📄 Create files (Windows PowerShell)
PowerShell does not support touch, so use:

```powershell
New-Item -Path YTlearning/.env -ItemType File
New-Item -Path YTlearning/2-real-projects/2-1-reusable-api/code/client.py -ItemType File
New-Item -Path YTlearning/2-real-projects/2-1-reusable-api/code/demo.py -ItemType File
```

📄 Or shorter (PowerShell)
```powershell
ni YTlearning/.env
ni YTlearning/2-real-projects/2-1-reusable-api/code/client.py
ni YTlearning/2-real-projects/2-1-reusable-api/code/demo.py
```

📄 Or simplest (PowerShell)
```powershell
echo "" > YTlearning/.env
echo "" > YTlearning/2-real-projects/2-1-reusable-api/code/client.py
echo "" > YTlearning/2-real-projects/2-1-reusable-api/code/demo.py
```

📦 Final structure
```python
YTlearning/
    .env
    2-real-projects/
        2-1-reusable-api/
            code/
                client.py
                demo.py
```

"This keeps the module clean, organized, and ready for integration into larger systems."

## SECTION 3 — Creating the Environment File

"Before writing any code, we need to prepare the .env file that will store our API key.

All modules in the Real Projects series will use this single .env file in the project root, not inside the module folder."

Root .env (located at YTlearning/.env):

```bash
API_KEY=your_api_key_here
```

"This keeps your secrets out of your code and ensures all modules share the same configuration."

## SECTION 4 — Creating the ApiClient Class

client.py

```python
import requests
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

class ApiClient:
    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url
        self.timeout = timeout
        self.api_key = os.getenv("API_KEY")

    def get(self, endpoint: str):
        try:
            response = requests.get(
                f"{self.base_url}{endpoint}",
                timeout=self.timeout,
                headers={"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logging.error(f"GET error: {e}")
            return None

    def post(self, endpoint: str, data: dict):
        try:
            response = requests.post(
                f"{self.base_url}{endpoint}",
                json=data,
                timeout=self.timeout,
                headers={"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logging.error(f"POST error: {e}")
            return None
```

## SECTION 5 — Testing the Client with a Demo Script

demo.py

```python
from client import ApiClient

api = ApiClient("https://jsonplaceholder.typicode.com")

print(api.get("/posts/1"))
print(api.post("/posts", {"title": "Hello", "body": "World"}))
```

"This confirms that the client works, handles JSON correctly, and logs errors when something goes wrong."

## SECTION 6 — Recap & Next Video

"Quick recap:

We installed the required packages, created the project structure, prepared the environment file, built the ApiClient class, tested the module with a demo script, and prepared the foundation for all future Real Projects."

"In the next video, we'll build the Websocket Client — the real‑time counterpart of this REST client."

"If this helped you, leave a like and subscribe. And tell me in the comments what Real Project you want next."

## 📌 Timestamps

- 00:00 – Intro
- 00:28 – Required installs
- 01:20 – Project structure
- 03:40 – Building the ApiClient class
- 04:45 – Testing the client
- 05:20 – Adding environment variables
- 06:18 – Recap & next video

## Key Takeaways

✅ REST API client foundation for all future Real Projects
✅ Handles GET and POST requests with proper error handling
✅ Environment variable support for secure API key management
✅ Logging infrastructure for debugging
✅ JSON parsing and response handling
✅ Timeout and exception management

## Requirements

- Python 3.8+
- pip package manager
- requests library
- python-dotenv library
- rich library
