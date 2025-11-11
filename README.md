# Stock Price Notifier — Real-Time Automated Stock Alert System

**Stock Price Notifier** is a Python-based automation tool that tracks live stock prices and alerts you when they cross your defined threshold.  
It demonstrates how to use **Selenium**, **BeautifulSoup**, and **Win10Toast** together to fetch data, monitor thresholds, and trigger desktop notifications — all in real time.

---

## Overview

This project continuously monitors selected stocks (for example: Reliance, TCS, Infosys) using data scraped from **Google Finance**.  
Whenever a stock’s price reaches or exceeds your target, the system triggers a **Windows desktop notification**, so you never miss your ideal buy/sell point.

You’ll learn concepts like:
- Real-time web scraping  
- Background automation and scheduling  
- Modular Python architecture  
- System-level notification handling  

---

## Key Features

- **Real-Time Price Monitoring:** Live price tracking with Selenium  
- **Customizable Watchlist:** Set multiple stocks and thresholds  
- **Instant Alerts:** Windows desktop notifications via Win10Toast  
- **Modular Codebase:** Separate modules for fetching, notifying, and main control  
- **Lightweight:** No APIs or dashboards required  
- **Extensible:** Can easily integrate with Telegram or Email  

---

## Project Structure

```bash
stock_price_notifier/
│
├── assets/
│   ├── 1.png        # Terminal output proof
│   └── 2.png        # Desktop notification proof
│
├── config.py        # Watchlist and alert configuration
├── fetchers.py      # Data fetching logic
├── notifiers.py     # Notification functions
├── watch.py         # Main runner script
└── __pycache__/     # Auto-generated cache
Configuration Example (config.py)
python
Copy code
WATCHLIST = [
    {
        "name": "RELIANCE",
        "url": "https://www.google.com/finance/quote/RELIANCE:NSE",
        "css_selector": "div.YMlKec.fxKbKc",
        "threshold": 1482.0,
        "mode": "selenium"
    },
]

NOTIFY = {
    "toast": True,       # Enable Windows notifications
    "email": False,      # Optional - enable later
    "telegram": False    # Optional - for mobile alerts
}
Installation & Setup
1. Clone the Repository
bash
Copy code
git clone https://github.com/SOHAN562001/stock_price_notifier.git
cd stock_price_notifier
2. Install Dependencies
bash
Copy code
pip install selenium webdriver-manager beautifulsoup4 lxml requests win10toast apscheduler
3. Run the Script
bash
Copy code
python watch.py
Example Output:

csharp
Copy code
Stock Price Notifier started...
[checking] RELIANCE
[debug] found price text: ₹1,485.00
[notify] RELIANCE reached ₹1485.00 (>= 1482.0)
A desktop notification will appear instantly once your threshold is met.

Proof of Work
Terminal Output
This screenshot shows the live price fetch and threshold detection process.


Desktop Notification
This screenshot confirms the real-time alert triggered by the notifier.


Learning Outcomes
You will learn to:

Automate data extraction using Selenium WebDriver

Parse live HTML using BeautifulSoup

Send real-time Windows notifications

Build modular Python automation systems

Apply event-driven logic for monitoring tasks

Future Enhancements
Add Telegram and Email alert integrations

Save alerts in CSV/SQLite for history tracking

Build a Streamlit dashboard for visualization

Use official APIs (e.g., Yahoo Finance, NSE API) for better stability

Tech Stack
Category	Tools / Libraries
Language	Python 3.12
Web Automation	Selenium, WebDriver Manager
Scraping	BeautifulSoup, lxml
Notifications	Win10Toast, Telegram Bot API
OS	Windows 10 / 11

Author
Sohan Ghosh
M.Sc. in Data Science & Artificial Intelligence
Ramakrishna Mission Residential College (University of Calcutta)


GitHub: github.com/SOHAN562001
