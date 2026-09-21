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
