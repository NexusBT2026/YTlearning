import logging
from dotenv import load_dotenv
import os
from rich import print

# Load root .env so the engine can read configuration values (like THRESHOLD)
# This allows changing strategy behavior without modifying code.
load_dotenv()

# Configure logging: every decision/action gets timestamped for debugging + audit trail.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)

logger = logging.getLogger(__name__)


class StrategyEngine:
    """
    Strategy Engine for evaluating incoming data and making decisions.
    
    Processes trade data against configurable thresholds and triggers actions
    when conditions are met. Designed to work with data from the DataCollector.
    """
    
    def __init__(self, threshold=None):
        """
        Initialize the Strategy Engine with configurable threshold.
        
        Args:
            threshold: Price threshold for triggering actions (float)
                      If None, reads from .env THRESHOLD variable
                      Default: 10.0 if not specified
        """

        # If threshold is passed manually, use it. Otherwise load from .env.
        # This makes the engine flexible and configurable without code changes.
        if threshold is not None:
            self.threshold = float(threshold)
        else:
            self.threshold = float(os.getenv("THRESHOLD", 10.0))
        
        logger.info(f"Strategy Engine initialized with threshold: {self.threshold}")

        # Counters for statistics — useful for dashboards and automation modules.
        self.decisions_count = 0
        self.actions_triggered = 0

    def evaluate(self, trade):
        """
        Evaluate a trade against the strategy conditions.
        
        Args:
            trade: Dictionary with trade data containing 'price' and 'quantity'
                  Example: {"price": "81218.00", "quantity": "0.00273"}
        
        Returns:
            dict: Action result if condition met, None otherwise
        """

        # Count every evaluation — helps measure strategy performance.
        self.decisions_count += 1
        
        try:
            # Extract price and quantity from trade.
            # Binance sends numbers as strings, so we convert to float.
            price = float(trade.get("price", 0.0))
            qty = float(trade.get("quantity", 0.0))
            
            print("[yellow]Evaluating trade...[/yellow]")
            logger.info(f"Evaluating: price={price}, qty={qty}, threshold={self.threshold}")
            
            # Core strategy condition:
            # If price exceeds threshold → trigger action.
            # This is intentionally simple for teaching; later strategies can be more complex.
            if price > self.threshold:
                print(f"[green]✓ Condition met: {price} > {self.threshold}[/green]")
                logger.info(f"Condition met for trade: price={price}")

                # Trigger the action and return the result.
                return self.trigger_action(price, qty)
            else:
                # Condition not met — no action triggered.
                print(f"[red]✗ Condition not met: {price} <= {self.threshold}[/red]")
                logger.info(f"Condition not met for trade: price={price}")
                return None
                
        except (ValueError, TypeError) as e:
            # If trade data is malformed, catch the error so the engine doesn't crash.
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

        # Count how many actions were triggered — useful for dashboards.
        self.actions_triggered += 1
        
        # Build a structured result object — easy to log, display, or send to automation.
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
        """Return statistics about decisions and actions.
        
        Used by dashboards and automation modules to show engine performance.
        """
        return {
            "total_decisions": self.decisions_count,
            "actions_triggered": self.actions_triggered,
            "threshold": self.threshold
        }

    def set_threshold(self, new_threshold):
        """Dynamically update the threshold.
        
        Allows real-time strategy adjustments without restarting the engine.
        """
        self.threshold = float(new_threshold)
        logger.info(f"Threshold updated to: {self.threshold}")
        print(f"[yellow]Threshold updated to: {self.threshold}[/yellow]")


if __name__ == "__main__":
    # This runs only if the file is executed directly.
    # Useful for debugging or confirming the module loads correctly.
    logger.info("StrategyEngine module loaded")
