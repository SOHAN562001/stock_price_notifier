Stock Price Notifier — Real-Time Automated Stock Alert System

Stock Price Notifier is a Python-based automation tool that tracks live stock prices and instantly alerts you when they cross your defined threshold.
It showcases how to use Selenium, BeautifulSoup, and Win10Toast together to fetch live market data, monitor thresholds, and trigger desktop notifications — all in real time.

Overview

This project continuously monitors selected stocks (for example: Reliance, TCS, Infosys) using data scraped from Google Finance.
Whenever a stock’s price reaches or exceeds your target, the system triggers a Windows desktop notification so you never miss your ideal buy or sell point.

It demonstrates key concepts such as:

Real-time data scraping

Background scheduling and monitoring

Event-driven notifications

Modular Python automation design

Key Features

Real-time price monitoring via Selenium

Configurable watchlist and thresholds for multiple stocks

Instant Windows desktop alerts using Win10Toast

Modular structure with independent scripts for fetching, notifications, and control

Extensible architecture — can be expanded to support Telegram or email alerts

Lightweight and dependency-minimal, avoiding complex APIs or dashboards

Project Structure
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
    "email": False,      # Optional - enable later if needed
    "telegram": False    # Optional - for mobile alerts
}

Installation and Setup
<details> <summary><b>Step-by-Step Setup</b></summary>
1. Clone the Repository
git clone https://github.com/SOHAN562001/stock_price_notifier.git
cd stock_price_notifier

2. Install Dependencies
pip install selenium webdriver-manager beautifulsoup4 lxml requests win10toast apscheduler

3. Run the Script
python watch.py


Example Output:

Stock Price Notifier started...
[checking] RELIANCE
[debug] found price text: ₹1,485.00
[notify] RELIANCE reached ₹1485.00 (>= 1482.0)


A Windows desktop notification will appear immediately once the price crosses your set limit.

</details>
Proof of Work
1. Terminal Output

This screenshot demonstrates the live stock price fetching and threshold detection process.

2. Desktop Notification

This screenshot confirms the instant Windows desktop alert once a price target is met.

Learning Outcomes

By completing this project, you will learn to:

Automate live data extraction using Selenium WebDriver

Utilize CSS selectors for dynamic data parsing

Send system notifications using Win10Toast

Build modular and maintainable Python scripts

Apply real-world automation workflows to financial data

Future Enhancements

Integrate Telegram and Email alerts

Log triggered alerts in CSV or SQLite

Add a Streamlit dashboard for price visualization

Extend support for official APIs (e.g., Yahoo Finance, NSE API)

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

LinkedIn: linkedin.com/in/sohanghosh562001

GitHub: github.com/SOHAN562001
