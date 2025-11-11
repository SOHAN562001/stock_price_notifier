# config.py

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
    "toast": True,    
    "email": False,   
    "telegram": False
}

EMAIL_FROM = "you@gmail.com"
EMAIL_TO = "you@gmail.com"
EMAIL_APP_PASSWORD = "xxxx xxxx xxxx xxxx"

TELEGRAM_BOT_TOKEN = "123456:ABCDEF..."
TELEGRAM_CHAT_ID = "123456789"
