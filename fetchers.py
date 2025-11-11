# fetchers.py
import time
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
def make_driver(headless=True):
    opts = Options()
    if headless:
        opts.add_argument("--headless=new")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--window-size=1200,800")
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    opts.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)

    return driver

def _clean_price_text(raw: str) -> float:
    raw = raw.strip().replace(",", "").replace("₹", "").replace("$", "")
    token = raw.split()[0]
    num = "".join(ch for ch in token if ch.isdigit() or ch == ".")
    return float(num)

def fetch_price_selenium(driver, url: str, css_selector: str, wait_secs: int = 15) -> float:
    try:
        driver.get(url)
        time.sleep(3)  # wait for page load
        elem = WebDriverWait(driver, wait_secs).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
        )
        price_text = elem.text.strip()
        print("[debug] found price text:", price_text)
        price_text = price_text.replace(",", "").replace("₹", "").replace("$", "")
        return float(price_text)
    except Exception as e:
        driver.save_screenshot("error_page.png")
        raise RuntimeError(f"Failed to fetch price from {url} ({e})")




def fetch_price_requests(url: str, css_selector: str, timeout: int = 10) -> float:
    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/121.0.0.0 Safari/537.36")
    }
    resp = requests.get(url, headers=headers, timeout=timeout)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "lxml")
    el = soup.select_one(css_selector)
    if not el:
        raise ValueError("CSS selector not found on static page (try Selenium mode).")
    return _clean_price_text(el.get_text())
