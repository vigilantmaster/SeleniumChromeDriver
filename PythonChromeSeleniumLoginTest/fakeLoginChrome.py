import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tempfile
import shutil

class ChromeLoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.temp_user_data_dir = tempfile.mkdtemp()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f"--user-data-dir={cls.temp_user_data_dir}")
        chrome_service = ChromeService(executable_path="F:\ChromeDriver\chromedriver\chromedriver-win64\chromedriver.exe")  # Replace with your actual chromedriver path
        cls.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        cls.wait = WebDriverWait(cls.driver, 10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        shutil.rmtree(cls.temp_user_data_dir)

    def setUp(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

    def tearDown(self):
        pass  # Not needed because driver is handled in class methods

    def test_login_success(self):
        driver = self.driver
        wait = self.wait

        username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
        login_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))

        username_field.send_keys("student")
        password_field.send_keys("Password123")
        login_button.click()

        # Check for successful login (replace with your actual success condition)
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Logged In Successfully')]")))
        self.assertTrue(success_message.is_displayed(), "Login successful: Success message displayed")

    def test_login_failure_invalid_credentials(self):
        driver = self.driver
        wait = self.wait

        username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
        login_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))

        username_field.send_keys("invalid_user")
        password_field.send_keys("invalid_password")
        login_button.click()

        # Check for the presence of the error element
        error_element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "error")))
        self.assertTrue(error_element.is_displayed(), "Login failed: Error element displayed")

        

if __name__ == "__main__":
    unittest.main()