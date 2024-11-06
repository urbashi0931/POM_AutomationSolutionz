import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import LoginClass

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize the WebDriver
        cls.driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH or specify the path
        cls.driver.implicitly_wait(10)  # Implicit wait to allow elements to load

    def test_valid_login(self):
        # Open the login page
        self.driver.get("https://apollo.zeuz.ai/Home/Login/")
        
        # Create an instance of LoginPage
        login_page = LoginClass.LoginPage(self.driver)

        # Login credentials
        username = "urbashi"  # Replace with actual username
        password = "Silvy@apollo1"  # Replace with actual password

        # Perform login action
        login_page.login(username, password)

        # Wait and verify login success
        WebDriverWait(self.driver, 10).until(
            EC.title_contains("Dashboard")  # Wait for the dashboard title
        )
        self.assertIn("Dashboard", self.driver.title)  # Check if the dashboard is displayed

    def test_invalid_login(self):
        # Open the login page
        self.driver.get("https://apollo.zeuz.ai/Home/Login/")
        
        # Create an instance of LoginPage
        login_page = LoginClass.LoginPage(self.driver)

        # Invalid login credentials
        username = "urbashi"  # Replace with an invalid username
        password = "invalid_"  # Replace with an invalid password

        # Perform login action
        login_page.login(username, password)

        # Verify error message
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "alertify-logs"))  # Adjust as necessary
        )
        self.assertTrue(self.driver.find_element(By.ID, "alertify-logs").is_displayed())  # Check if error message is displayed
    
    def test_allspace_login(self):
        # Open the login page
        self.driver.get("https://apollo.zeuz.ai/Home/Login/")
        
        # Create an instance of LoginPage
        login_page = LoginClass.LoginPage(self.driver)

        # Invalid login credentials
        username = "        "  # Replace with an invalid username
        password = "        "  # Replace with an invalid password

        # Perform login action
        login_page.login(username, password)

        # Verify error message
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "alertify-logs"))  # Adjust as necessary
        )
        self.assertTrue(self.driver.find_element(By.ID, "alertify-logs").is_displayed())  # Check if error message is displayed

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
