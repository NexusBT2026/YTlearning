# Story 2-4: Strategy Engine

## Overview

This episode teaches building a production-ready Strategy Engine in Python that evaluates incoming data and makes automated decisions based on configurable conditions. Viewers learn how to build the decision/action layer in data-driven systems.

Viewers learn how to:
- Evaluate incoming data against conditions
- Configure thresholds via environment variables
- Trigger actions when conditions are met
- Log all decisions with timestamps
- Handle different data formats
- Integrate with Story 2-3's Data Collector
- Build automation foundations for dashboards and trading systems

## Key Concepts

### Decision Engine Architecture

**Core Pattern:**
1. **Evaluate**: Check incoming data against conditions
2. **Decide**: Determine if action threshold is met
3. **Act**: Trigger actions and log results

**Real-World Use Cases:**
- Trading systems: "Buy if price > $60,000"
- Dashboards: "Alert if value exceeds threshold"
- Automation: "Execute action when condition met"
- Monitoring: "Log and action on metric spikes"

### Threshold-Based Conditions

**Simple Threshold Pattern:**
```python
if price > threshold:
    trigger_action()
else:
    log_no_action()
```

**Configurable via Environment:**
- Store THRESHOLD in .env
- Load at startup with `os.getenv()`
- Change without code modification
- Easy to test different thresholds

### Action Triggering

**When Condition Met:**
1. Record the decision
2. Execute action
3. Log with context (price, quantity, timestamp)
4. Return result for downstream use

**Logging Strategy:**
- Log every decision (both met and not met)
- Include context data (price, quantity, threshold)
- Timestamp all actions
- Enable audit trail

### Statistics & Monitoring

**Track System State:**
- Total decisions evaluated
- Actions triggered count
- Current threshold
- Supports integration with dashboards

## Code Structure

### File: `code/engine.py`

**StrategyEngine class** with decision logic:
- `__init__(threshold)`: Initialize with configurable threshold from .env
- `evaluate(trade)`: Evaluate trade data, return action if condition met
- `trigger_action(price, qty)`: Execute action when condition met
- `get_statistics()`: Return decision/action counts
- `set_threshold(new_threshold)`: Dynamically update threshold
- Full logging for audit trail
- Rich console output for formatted display
- Error handling for malformed data

**Key Features:**
- Threshold from .env or default value
- Tracks decisions and actions
- Proper error handling
- Logging at INFO level
- Rich output formatting

### File: `code/demo.py`

**Test script** that reads REAL trade data from Story 2-3 (DataCollector) CSV file and processes it through the engine:
- Loads the actual CSV file created by the DataCollector
- Processes each real trade through the decision engine
- Displays which trades triggered actions
- Shows statistics (total trades, actions triggered, threshold)
- Handles file not found error with helpful message

**Features:**
- Reads real data from Story 2-3
- Processes actual Binance trade format (CSV with price/quantity columns)
- Colored output using Rich
- Statistics summary
- Success confirmation

**Prerequisites:**
- Story 2-3 (DataCollector) must be run first to generate btcusdt_trades.csv

### File: `code/requirements.txt`

**Python dependencies:**
- `python-dotenv >= 1.0.0` — Load .env configuration
- `rich >= 13.0.0` — Terminal formatting

### File: `code/.env.example`

**Environment template** showing THRESHOLD configuration.
Default: 60000 (adjustable for any price threshold)

## Dependencies on Previous Stories

### Story 2-1 (REST API Client):
- Uses same .env location: `YTlearning/.env`
- Follows same logging pattern: `logging.basicConfig(...)`
- Uses same Rich formatting: `[green]`, `[red]`, `[cyan]` tags
- Shares error handling philosophy

### Story 2-2 (WebSocket Client):
- Uses Rich output patterns
- Follows same logging approach
- Same environment configuration location

### Story 2-3 (Data Collector):
- StrategyEngine processes output from DataCollector
- Uses same data formats (trade dictionaries)
- Shared .env file and logging configuration
- Direct integration: Collector → Strategy Engine → Actions

### Shared Patterns Across All:
```python
from dotenv import load_dotenv
from rich import print
import logging

load_dotenv()
logging.basicConfig(format="%(asctime)s — %(levelname)s — %(message)s")
```

## Project Structure

```
YTlearning/
├── .env                                    # Shared configuration
├── 2-real-projects/
│   ├── api_client/
│   │   └── code/
│   │       ├── client.py                  # Story 2-1
│   │       └── demo.py
│   │
│   ├── websocket_client/
│   │   └── code/
│   │       ├── client.py                  # Story 2-2
│   │       └── demo.py
│   │
│   ├── data_collector/
│   │   └── code/
│   │       ├── collector.py               # Story 2-3
│   │       └── demo.py
│   │
│   └── strategy_engine/                   # Story 2-4
│       ├── code/
│       │   ├── engine.py                  # StrategyEngine class
│       │   ├── demo.py                    # Test script
│       │   ├── requirements.txt           # Dependencies
│       │   └── .env.example               # Config template
│       ├── script/
│       │   └── script.md                  # Video script
│       ├── assets/
│       │   └── ASSETS.md                  # Production checklist
│       └── README.md                      # This file
|
├── shared/
│   └── src/
│       └── data/               
│           ├── ohlcv_data/
│           ├── pipeline/
│           │   └── collector.py
│           ├── rest_api/
│           │   └── api_client.py
│           ├── trades/
│           └── websockets/
│               └── ws_client.py
```

## Acceptance Criteria Coverage

✅ **Understand decision engines** — Explains pattern and use cases  
✅ **Implement StrategyEngine** — Class with evaluate() and trigger_action()  
✅ **Configure thresholds** — Via environment variables (THRESHOLD)  
✅ **Evaluate data** — Processes incoming trade dictionaries  
✅ **Trigger actions** — When conditions are met  
✅ **Handle data formats** — From REST/WebSocket/DataCollector  
✅ **Log decisions** — With timestamps and context  
✅ **Track statistics** — Decisions and actions count  
✅ **Test with demo** — demo.py uses real Binance trade format  

## Testing Recommendations

### Manual Testing

**Prerequisites:**
```bash
# First, run Story 2-3 (DataCollector) to generate the CSV file
cd 2-real-projects/2-3-data-collector/code
python demo.py
# This creates btcusdt_trades.csv

# Then proceed with Story 2-4
```

**Setup:**
```bash
# Install dependencies
pip install -r 2-real-projects/2-4-strategy-engine/code/requirements.txt

# Verify .env is configured
cat YTlearning/.env | grep THRESHOLD

# Navigate to code folder
cd 2-real-projects/2-4-strategy-engine/code
```

**Run Demo with Real Data:**
```bash
python demo.py
```

**Expected Output (Example):**
```
═══════════════════════════════════════
Strategy Engine Demo
Processing Real Binance Trade Data
═══════════════════════════════════════

Trade 1: Price=81182.02000000, Qty=0.00127000
Evaluating trade...
2026-10-03 04:10:01,014 — INFO — Evaluating: price=81182.02, qty=0.00127, threshold=81000.0
✓ Condition met: 81182.02 > 81000.0
2026-10-03 04:10:01,014 — INFO — Condition met for trade: price=81182.02
✓ Action triggered: price=81182.02, qty=0.00127
2026-10-03 04:10:01,014 — INFO — Action triggered: {'action': 'triggered', 'price': 81182.02, 'qty': 0.00127, 'reason': 'price > 81000.0', 'action_count': 2915}
  ✓ Strategy decision: {'action': 'triggered', 'price': 81182.02, 'qty': 0.00127, 'reason': 'price > 81000.0', 'action_count': 2915}

Trade 2: Price=81182.02000000, Qty=0.00011000
Evaluating trade...
2026-10-03 04:10:01,015 — INFO — Evaluating: price=81182.02, qty=0.00011, threshold=81000.0
✓ Condition met: 81182.02 > 81000.0
2026-10-03 04:10:01,016 — INFO — Condition met for trade: price=81182.02
✓ Action triggered: price=81182.02, qty=0.00011
2026-10-03 04:10:01,016 — INFO — Action triggered: {'action': 'triggered', 'price': 81182.02, 'qty': 0.00011, 'reason': 'price > 81000.0', 'action_count': 2916}
  ✓ Strategy decision: {'action': 'triggered', 'price': 81182.02, 'qty': 0.00011, 'reason': 'price > 81000.0', 'action_count': 2916}

═══════════════════════════════════════
Execution Summary
═══════════════════════════════════════
Trades Processed: 2916
Total Decisions: 2916
Actions Triggered: 2916
Threshold: 81000.0
═══════════════════════════════════════

✓ Demo completed successfully!

[... more trades ...]

Trade 1: Price=81182.02000000, Qty=0.00127000
Evaluating trade...
2026-10-03 04:08:33,998 — INFO — Evaluating: price=81182.02, qty=0.00127, threshold=82000.0
✗ Condition not met: 81182.02 <= 82000.0
2026-10-03 04:08:33,998 — INFO — Condition not met for trade: price=81182.02

Trade 2: Price=81182.02000000, Qty=0.00011000
Evaluating trade...
2026-10-03 04:08:33,999 — INFO — Evaluating: price=81182.02, qty=0.00011, threshold=82000.0
✗ Condition not met: 81182.02 <= 82000.0
2026-10-03 04:08:33,999 — INFO — Condition not met for trade: price=81182.02

═══════════════════════════════════════
Execution Summary
═══════════════════════════════════════
Trades Processed: 2916
Total Decisions: 2916
Actions Triggered: 0
Threshold: 82000.0
═══════════════════════════════════════

✓ Demo completed successfully!

```

**Note:** The exact output depends on the real Binance data collected by Story 2-3. Trades above the threshold will trigger actions.

### Testing Different Thresholds

**Test 1: High Threshold (Fewer Actions)**
```bash
# Edit .env
THRESHOLD=82000
python demo.py
# Expected: Fewer actions triggered (only trades > 82000)
```

**Test 2: Low Threshold (More Actions)**
```bash
# Edit .env
THRESHOLD=81000
python demo.py
# Expected: More actions triggered (more trades > 81000)
```

**Test 3: Custom Threshold via Code**
```python
from engine import StrategyEngine

engine = StrategyEngine(threshold=81000)  # Override default
# Now processes with custom threshold
```

### Troubleshooting

**Error: "Trades file not found"**
- First run Story 2-3 (DataCollector) to generate the CSV:
  ```bash
  cd 2-real-projects/2-3-data-collector/code && python demo.py
  ```

**Error: "No module named 'dotenv'"**
- Install: `pip install python-dotenv`

**Error: "No module named 'rich'"**
- Install: `pip install rich`

**Error: "THRESHOLD not found"**
- Add to .env: `THRESHOLD=81000`
- Or use default: 10.0

**Demo runs but shows 0 actions triggered**
- Check THRESHOLD value in .env vs. actual trade prices in CSV
- If THRESHOLD is very high, no trades will exceed it

## Integration Points

### Used By:
- **Story 2-5 (Dashboard):** Displays engine decisions visually
- **Future modules:** Any system needing decision logic

### Uses:
- **Story 2-3 (DataCollector):** Processes collected data

### Shared Resources:
- `.env` file: Root configuration (THRESHOLD setting)
- `logging`: Shared logging setup
- `rich`: Shared output formatting

## Next Story

Following this story is **Story 2-5: Dashboard**, which visualizes real-time data from the DataCollector and displays decisions from the StrategyEngine.

The pipeline becomes:
1. DataCollector (2-3): Gathers data
2. StrategyEngine (2-4): Makes decisions
3. Dashboard (2-5): Displays results
4. ... and more

## Quick Reference

### Run the Demo with Real Data:
```bash
cd 2-real-projects/2-4-strategy-engine/code && python demo.py
```

### Modify Threshold:
Edit `.env` and change `THRESHOLD=60000` to any value

### Custom Integration with Real CSV:
```python
import csv
from engine import StrategyEngine

engine = StrategyEngine(threshold=81000)

# Read real trades from CSV
with open('btcusdt_trades.csv', 'r') as f:
    reader = csv.DictReader(f)
    for trade in reader:
        result = engine.evaluate(trade)
        if result:
            print("Action triggered:", result)
```

### Direct Data Integration:
```python
from engine import StrategyEngine

# Process any trade dictionary (from CSV, API, WebSocket, etc.)
engine = StrategyEngine()
trade = {"price": "65000.00", "quantity": "0.001"}
result = engine.evaluate(trade)

if result:
    print("Action triggered:", result)
```

---

**Status:** ✅ Ready for Implementation  
**Duration:** 14-15 minutes
**Difficulty:** Intermediate  
**Prerequisites:** Story 2-1, 2-2, 2-3 completed
