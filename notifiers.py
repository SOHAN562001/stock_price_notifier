from win10toast import ToastNotifier
import smtplib
import requests
from email.mime.text import MIMEText
from config import NOTIFY, EMAIL_FROM, EMAIL_TO, EMAIL_APP_PASSWORD, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID


def send_notification(name, price, threshold):
    msg = f"{name} has reached ₹{price:.2f} (target: ₹{threshold})"
    print("[notify] Sending alert:", msg)

    if NOTIFY.get("toast"):
        try:
            ToastNotifier().show_toast(
                f"📈 {name} Alert",
                msg,
                duration=10,
                threaded=True
            )
        except Exception as e:
            print("[toast error]", e)

    if NOTIFY.get("email"):
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_FROM, EMAIL_APP_PASSWORD)
            message = MIMEText(msg)
            message["Subject"] = f"{name} Stock Alert"
            message["From"] = EMAIL_FROM
            message["To"] = EMAIL_TO
            server.sendmail(EMAIL_FROM, EMAIL_TO, message.as_string())
            server.quit()
            print("[email sent]")
        except Exception as e:
            print("[email error]", e)

    if NOTIFY.get("telegram"):
        try:
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            data = {"chat_id": TELEGRAM_CHAT_ID, "text": msg}
            requests.post(url, data=data)
            print("[telegram sent]")
        except Exception as e:
            print("[telegram error]", e)
