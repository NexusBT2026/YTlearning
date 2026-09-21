#!/usr/bin/env python3
"""
Demo script for Story 2-3: Unified Data Collector

This demo verifies that the DataCollector correctly:
1. Fetches historical OHLCV candles via REST
2. Streams live OHLCV candles via WebSocket
3. Streams live trades via WebSocket
4. Updates and appends candles to CSV in real time

Run this file to confirm everything works together.
"""

import asyncio
import sys
import os
import logging

# Add parent directory to path so collector.py can be imported
sys.path.insert(0, os.path.dirname(__file__))

from collector import DataCollector

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(name)s — %(levelname)s — %(message)s"
)

logger = logging.getLogger(__name__)


async def main():
    """
    Run the unified data collector demo.

    This starts:
    - REST historical fetch
    - WebSocket OHLCV stream
    - WebSocket trade stream

    Both WebSocket streams run concurrently for 60 seconds.
    """

    collector = DataCollector(
        rest_url="https://api.binance.com",
        ws_url_kline="wss://stream.binance.com:9443/ws/btcusdt@kline_1m",
        ws_url_trades="wss://stream.binance.com:9443/ws/btcusdt@trade"
    )

    # Run the full pipeline for 60 seconds
    await collector.run(stream_duration=60)


if __name__ == "__main__":
    asyncio.run(main())
