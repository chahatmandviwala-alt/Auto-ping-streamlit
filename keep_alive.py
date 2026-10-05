import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# The URL is passed from the GitHub Action
app_url = sys.argv[1]

# Configure Chrome to run invisibly (headless)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize the browser
driver = webdriver.Chrome(options=chrome_options)

print(f"Pinging {app_url}...")
driver.get(app_url)

# Wait 10 seconds to ensure Streamlit's WebSockets fully connect
time.sleep(10)

print("Ping successful! Closing browser.")
driver.quit()
