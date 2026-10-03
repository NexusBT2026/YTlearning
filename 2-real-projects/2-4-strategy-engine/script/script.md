# Real Projects — Episode 4 — Building a Python Strategy Engine (Processing REST + Websocket Data)

## INTRO

"Welcome back!
In the last video, we built the Data Collector — a module that fetches historical REST data and listens to real‑time websocket updates.

Today we're building the Strategy Engine: the module that processes incoming data, evaluates conditions, and makes decisions.
This is the core logic layer used in automation tools, dashboards, and trading bots.

No theory — only real, practical code that works."

---

## SECTION 1 — Required Installs (pip + environment)

"Before we start coding, let's install the required packages.

If you followed Episode 1–3, you already have python-dotenv and rich installed.
If you're jumping in from this video, install everything below."

### 📦 Windows / macOS / Linux (pip)

```bash
pip install python-dotenv
pip install rich
```

### 🐧 Linux/macOS note (pip3)

```bash
pip3 install python-dotenv
pip3 install rich
```

### ⚡ uv (recommended for faster installs)

```bash
uv add python-dotenv
uv add rich
```

---

## SECTION 2 — Project Structure

"Let's create the project structure for this module."

### 📁 Create folders

```bash
mkdir -p 2-real-projects/2-4-strategy-engine
mkdir -p 2-real-projects/2-4-strategy-engine/code
```

### 📄 Create files (Linux/macOS)

```bash
touch 2-real-projects/2-4-strategy-engine/code/engine.py
touch 2-real-projects/2-4-strategy-engine/code/demo.py
```

### 📄 Create files (Windows PowerShell)

```powershell
New-Item -Path 2-real-projects/2-4-strategy-engine/code/engine.py -ItemType File
New-Item -Path 2-real-projects/2-4-strategy-engine/code/demo.py -ItemType File
```

### 📄 Or shorter (PowerShell)

```powershell
ni 2-real-projects/2-4-strategy-engine/code/engine.py
ni 2-real-projects/2-4-strategy-engine/code/demo.py
```

### 📄 Or simplest (PowerShell)

```powershell
echo "" > 2-real-projects/2-4-strategy-engine/code/engine.py
echo "" > 2-real-projects/2-4-strategy-engine/code/demo.py
```

### 📦 Final structure

```
YTlearning/
    .env
    2-real-projects/
    2-1-reusable-api/
    2-2-websocket-client/
    2-3-data-collector/
    2-4-strategy-engine/
            assets/
                ASSETS.md
            code/
                demo.py
                engine.py
    shared/
        src/
            data/               
                ohlcv_data/
                pipeline/
                    collector.py
                rest_api/
                    api_client.py
                trades/
                websockets/
                    ws_client.py   
```

---

## SECTION 3 — Creating the Strategy Engine Class

"Now that the structure is ready, let's build the Strategy Engine.

We'll create a class that:
- evaluates incoming trade data
- checks conditions against thresholds
- triggers actions when conditions are met
- logs all decisions for debugging
- loads settings from the root .env
- uses Rich for clean output"

### **File: engine.py**

```python
import logging
from dotenv import load_dotenv
import os
from rich import print

# Load root .env
load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)

logger = logging.getLogger(__name__)


class StrategyEngine:
    """
    Strategy Engine for evaluating incoming data and making decisions.
    
    Processes trade data against configurable thresholds and triggers actions
    when conditions are met.
    """
    
    def __init__(self, threshold=None):
        """
        Initialize the Strategy Engine with configurable threshold.
        
        Args:
            threshold: Price threshold for triggering actions (float)
                      If None, reads from .env THRESHOLD variable
                      Default: 10.0 if not specified
        """
        if threshold is not None:
            self.threshold = float(threshold)
        else:
            self.threshold = float(os.getenv("THRESHOLD", 10.0))
        
        logger.info(f"Strategy Engine initialized with threshold: {self.threshold}")
        self.decisions_count = 0
        self.actions_triggered = 0

    def evaluate(self, trade):
        """
        Evaluate a trade against the strategy conditions.
        
        Args:
            trade: Dictionary with trade data containing 'price' and 'quantity'
        
        Returns:
            dict: Action result if condition met, None otherwise
        """
        self.decisions_count += 1
        
        try:
            price = float(trade.get("price", 0.0))
            qty = float(trade.get("quantity", 0.0))
            
            print("[yellow]Evaluating trade...[/yellow]")
            logger.info(f"Evaluating: price={price}, qty={qty}, threshold={self.threshold}")
            
            if price > self.threshold:
                print(f"[green]✓ Condition met: {price} > {self.threshold}[/green]")
                logger.info(f"Condition met for trade: price={price}")
                return self.trigger_action(price, qty)
            else:
                print(f"[red]✗ Condition not met: {price} <= {self.threshold}[/red]")
                logger.info(f"Condition not met for trade: price={price}")
                return None
                
        except (ValueError, TypeError) as e:
            print(f"[red]✗ Error evaluating trade:[/red] {e}")
            logger.error(f"Error evaluating trade: {e}")
            return None

    def trigger_action(self, price, qty):
        """
        Trigger an action when conditions are met.
        
        Args:
            price: Price value that triggered the action (float)
            qty: Quantity associated with the trade (float)
        
        Returns:
            dict: Action details and result
        """
        self.actions_triggered += 1
        
        action_result = {
            "action": "triggered",
            "price": price,
            "qty": qty,
            "reason": f"price > {self.threshold}",
            "action_count": self.actions_triggered
        }
        
        print(f"[cyan]✓ Action triggered: price={price}, qty={qty}[/cyan]")
        logger.info(f"Action triggered: {action_result}")
        
        return action_result

    def get_statistics(self):
        """Return statistics about decisions and actions."""
        return {
            "total_decisions": self.decisions_count,
            "actions_triggered": self.actions_triggered,
            "threshold": self.threshold
        }

    def set_threshold(self, new_threshold):
        """Dynamically update the threshold."""
        self.threshold = float(new_threshold)
        logger.info(f"Threshold updated to: {self.threshold}")
        print(f"[yellow]Threshold updated to: {self.threshold}[/yellow]")


if __name__ == "__main__":
    logger.info("StrategyEngine module loaded")
```

---

## SECTION 4 — Testing the Strategy Engine with Real Data

"Now let's test the engine by reading REAL trade data that was collected in Episode 3 (Story 2-3).

This is the key difference: we're not simulating trades or creating fake data.
We're reading the actual CSV file that the DataCollector saved."

### **File: demo.py**

```python
#!/usr/bin/env python3
"""
Demo script for Story 2-4: Strategy Engine

This script reads REAL trade data from the CSV file created by Story 2-3
(DataCollector) and evaluates it against the Strategy Engine.

Demonstrates:
1. Loading real Binance trade data from CSV
2. Processing each trade through the decision engine
3. Triggering actions when conditions are met
4. Logging all decisions with timestamps
"""

import csv
import os
from rich import print
from engine import StrategyEngine

# Path to the REAL trades file created by Story 2-3 (DataCollector)
TRADES_FILE = "../../shared/src/data/trades/BTC_trades.csv"


def main():
    """Run the Strategy Engine demo with real collected data."""
    print("[bold cyan]═══════════════════════════════════════[/bold cyan]")
    print("[bold cyan]Strategy Engine Demo[/bold cyan]")
    print("[bold cyan]Processing Real Binance Trade Data[/bold cyan]")
    print("[bold cyan]═══════════════════════════════════════[/bold cyan]\n")
    
    # Check if trades file exists
    if not os.path.exists(TRADES_FILE):
        print(f"[red]✗ Error: Trades file not found:[/red] {TRADES_FILE}")
        print("[yellow]First run Story 2-3 (DataCollector) to generate btcusdt_trades.csv[/yellow]")
        return
    
    # Create engine instance
    engine = StrategyEngine()
    
    # Read and process real trades from CSV
    try:
        with open(TRADES_FILE, "r") as f:
            reader = csv.DictReader(f)
            trade_count = 0
            
            for trade in reader:
                trade_count += 1
                print(f"[magenta]Trade {trade_count}:[/magenta] Price={trade.get('price')}, Qty={trade.get('quantity')}")
                
                result = engine.evaluate(trade)
                
                if result:
                    print(f"[magenta]  ✓ Strategy decision:[/magenta] {result}\n")
                else:
                    print("")
        
        # Display statistics
        stats = engine.get_statistics()
        print("[bold cyan]═══════════════════════════════════════[/bold cyan]")
        print("[bold cyan]Execution Summary[/bold cyan]")
        print("[bold cyan]═══════════════════════════════════════[/bold cyan]")
        print(f"[cyan]Trades Processed:[/cyan] {trade_count}")
        print(f"[cyan]Total Decisions:[/cyan] {stats['total_decisions']}")
        print(f"[cyan]Actions Triggered:[/cyan] {stats['actions_triggered']}")
        print(f"[cyan]Threshold:[/cyan] {stats['threshold']}")
        print("[bold cyan]═══════════════════════════════════════[/bold cyan]\n")
        
        print("✓ Demo completed successfully!")
        
    except FileNotFoundError:
        print(f"[red]✗ Error: Could not find {TRADES_FILE}[/red]")
        print("[yellow]Make sure Story 2-3 (DataCollector) has been run first[/yellow]")
    except Exception as e:
        print(f"[red]✗ Error processing trades:[/red] {e}")


if __name__ == "__main__":
    main()
```

**Run the demo:**

```bash
cd 2-real-projects/2-4-strategy-engine/code
python demo.py
```

"This reads the ACTUAL CSV file from Story 2-3 and evaluates each real trade. No fake data — only the actual Binance trades that were collected."

---

## SECTION 5 — Using Environment Variables

"Let's configure the threshold for our strategy in the .env file."

### Root .env (located at YTlearning/.env):

```bash
THRESHOLD=60000
```

"This keeps your strategy configuration clean and easily adjustable. Simply change THRESHOLD to modify when actions are triggered."

---

## SECTION 6 — Recap & Next Video

"Quick recap:

We installed the required packages, created the project structure, built the Strategy Engine class with decision logic and action triggering, added logging and environment variables, tested the module with a demo script using real Binance trade formats, and prepared the decision layer for all future Real Projects.

The Strategy Engine is now ready to:
- Evaluate any incoming data format
- Make automated decisions based on conditions
- Trigger actions and log them
- Integrate into dashboards and automation systems

In the next video, we'll build the Dashboard — a visual interface that displays REST data, websocket updates, and strategy decisions in real-time."

---

## 📌 Timestamps

- 00:00 – Intro
- 00:36 – Required installs
- 02:10 – Project structure
- 04:23 – Building the Strategy Engine class
- 09:15 – Testing the engine
- 12:05 – Adding environment variables
- 14:12 – Recap & next video

## Key Takeaways

✅ Strategy Engine architecture for automated decision-making
✅ Configurable thresholds via environment variables
✅ Decision evaluation logic — price conditions and action triggering
✅ Proper logging infrastructure for all decisions and actions
✅ Error handling for malformed trade data
✅ Rich console output for clear user feedback
✅ Statistics tracking — total decisions and actions triggered
✅ CSV integration — reads real trade data from Story 2-3
✅ Foundation for dashboards and automation systems
✅ Production-ready code patterns for real-world systems

## Requirements

- Python 3.7+
- pip package manager
- python-dotenv library
- rich library
- Real trade CSV from Story 2-3 (DataCollector)
