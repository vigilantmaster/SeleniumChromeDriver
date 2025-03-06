from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import tempfile
import shutil

try:
    chrome_options = Options()
    temp_user_data_dir = tempfile.mkdtemp()
    chrome_options.add_argument(f"--user-data-dir={temp_user_data_dir}")
    chrome_service = Service(r"F:\ChromeDriver\chromedriver\chromedriver-win64\chromedriver.exe") # Replace with your chromedriver path
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    driver.get("https://www.google.com")

    # Your Selenium code here...

except Exception as e:
    print(f"Error: {e}")
finally:
    if 'driver' in locals() and driver is not None:
        driver.quit()
    try:
        shutil.rmtree(temp_user_data_dir) # Remove the temporary directory.
    except OSError as e:
        print (f"Error: {e}")