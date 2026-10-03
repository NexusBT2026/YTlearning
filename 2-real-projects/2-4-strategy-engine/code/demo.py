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

Run this to verify the engine works with real collected data.

Requirements:
- Python 3.7+
- All packages from requirements.txt installed
- .env file with THRESHOLD setting (or default 10.0)
- btcusdt_trades.csv from Story 2-3 DataCollector
"""

import csv
import os
from rich import print
from engine import StrategyEngine

# Path to the REAL trades file created by Story 2-3 (DataCollector)
TRADES_FILE = "2-real-projects/shared/src/data/trades/BTC_trades.csv"


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
