from ast import Import
from selenium import webdriver
import time
from LoginClass import LoginPage

# Import LoginPage class
from Page_Object_Model_Project import LoginPage  # Adjust this import path as needed

def test_login():
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # Make sure ChromeDriver is in PATH or specify the path here
    driver.get("https://apollo.zeuz.ai/Home/Login/")  # Open the login page

    # Create an instance of LoginPage with the driver
    login_page = LoginPage(driver)

    # Login credentials
    username = "urbashi"  # Replace with actual username
    password = "Silvy@apollo1"  # Replace with actual password

    # Perform login action
    login_page.login(username, password)

    # Optionally, you can add assertions here to verify login success, such as:
    # assert "Dashboard" in driver.title  # or other verification logic

    time.sleep(15)  # Pause to observe the result
    #driver.quit()  # Close the browser

# Run the test
if __name__ == "__main__":
    test_login()
