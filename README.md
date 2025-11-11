# 📈 Stock Price Notifier — Real-Time Automated Stock Alert System

The **Stock Price Notifier** is a Python-based automation tool that tracks live stock prices and instantly alerts you when they cross your defined threshold.  
It demonstrates the practical use of **Selenium**, **BeautifulSoup**, and **Win10Toast** to fetch data, monitor thresholds, and send desktop notifications — all in real-time.

---

## 🧭 Overview

This project continuously monitors selected stocks (e.g., Reliance, TCS, Infosys) using data scraped from **Google Finance**.  
When a stock’s price reaches or exceeds your target, the system triggers a **Windows desktop notification**, so you never miss your ideal buy/sell point.

This makes it an excellent project for learning:
- Real-time data scraping
- Background scheduling
- System notifications
- Modular automation in Python

---

## 🚀 Features

✅ Real-time price monitoring via **Selenium**  
✅ Configurable stock list and price thresholds  
✅ Instant Windows desktop alerts via **Win10Toast**  
✅ Modular structure (`fetchers.py`, `watch.py`, `notifiers.py`)  
✅ Easy to extend for **Telegram** or **Email alerts**  
✅ Lightweight — no heavy APIs or dashboards needed

---

## 🧱 Project Structure

stock_price_notifier/
│
├── assets/
│ ├── 1.png # Terminal output proof
│ └── 2.png # Desktop notification proof
│
├── config.py # Watchlist & notification settings
├── fetchers.py # Data fetching logic
├── notifiers.py # Notification functions
├── watch.py # Main script that ties everything
└── pycache/ # Cache folder (auto-created)

yaml
Copy code

---

## ⚙️ Configuration Example (`config.py`)

```python
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
    "toast": True,      # Enable Windows notifications
    "email": False,     # Optional - can be enabled later
    "telegram": False   # Optional - for mobile alerts
}
🧰 Installation & Setup
1️⃣ Clone the Repository
bash
Copy code
git clone https://github.com/SOHAN562001/stock_price_notifier.git
cd stock_price_notifier
2️⃣ Install Required Packages
bash
Copy code
pip install selenium webdriver-manager beautifulsoup4 lxml requests win10toast apscheduler
3️⃣ Run the Script
bash
Copy code
python watch.py
You’ll see logs like this:

bash
Copy code
Stock Price Notifier started...
[checking] RELIANCE
[debug] found price text: ₹1,485.00
[notify] RELIANCE reached ₹1485.00 (>= 1482.0)
…and you’ll receive a Windows notification instantly.

🧾 Proof of Work
Below are screenshots from the actual working version of this project:

Screenshot	Description
Terminal output showing price fetch and threshold trigger
Windows desktop notification alert confirming trigger

🧠 Learning Highlights
Through this project, you’ll learn how to:

Automate websites using Selenium WebDriver

Use CSS selectors to extract live data dynamically

Send desktop notifications using Win10Toast

Build a modular, event-driven workflow

Apply real-world automation principles in Python

🧭 Future Enhancements
Add Telegram & Email alert integrations

Log triggered prices to CSV/SQLite

Add a Streamlit dashboard for visualization

Integrate with APIs (e.g., Yahoo Finance, NSE API)

🛠️ Tech Stack
Category	Tools / Libraries
Language	Python 3.12
Web Automation	Selenium, WebDriver Manager
Scraping	BeautifulSoup, lxml
Notifications	Win10Toast, Telegram Bot API
OS	Windows 10 / 11

👨‍💻 Author
Sohan Ghosh
M.Sc. in Data Science & Artificial Intelligence
Ramakrishna Mission Residential College (University of Calcutta)

🔗 LinkedIn: linkedin.com/in/sohanghosh562001
💻 GitHub: github.com/SOHAN562001

