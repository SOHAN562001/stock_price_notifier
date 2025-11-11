# watch.py
import time
from fetchers import make_driver, fetch_price_selenium
from config import WATCHLIST
from notifiers import send_notification


def check_once(headless=True):
    """Check prices once for all stocks in the WATCHLIST."""
    driver = None
    try:
        # Only make driver if at least one stock uses selenium
        needs_selenium = any(stock["mode"] == "selenium" for stock in WATCHLIST)
        driver = make_driver(headless=headless) if needs_selenium else None

        for stock in WATCHLIST:
            try:
                print()
                print("=" * 70)
                print(f"[checking] {stock['name']}")

                if stock["mode"] == "selenium":
                    price = fetch_price_selenium(driver, stock["url"], stock["css_selector"])
                else:
                    raise ValueError("Only selenium mode implemented in this version")

                print(f"[{time.strftime('%H:%M:%S')}] {stock['name']}: {price} (thr={stock['threshold']})")

                # ✅ Trigger notification if threshold reached
                if price >= stock["threshold"]:
                    print(f"[notify] {stock['name']} reached ₹{price} (>= {stock['threshold']})")
                    send_notification(stock["name"], price, stock["threshold"])

            except Exception as e:
                print(f"[error] {stock['name']}: {e}")
                continue

    finally:
        if driver:
            driver.quit()


def main(interval_seconds=30, headless=True):
    """Continuously monitor stocks with periodic checking."""
    print("📊 Stock Price Notifier started...")
    print("Press Ctrl+C to stop.\n")

    while True:
        check_once(headless=headless)
        print("-" * 70)
        print(f"[sleeping] Waiting {interval_seconds} sec for next check...")
        time.sleep(interval_seconds)


if __name__ == "__main__":
    # Change interval_seconds for how often to check (e.g., 1800 for 30 mins)
    # Use headless=False once to visually test the browser.
    main(interval_seconds=30, headless=True)
