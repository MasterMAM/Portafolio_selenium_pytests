import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(100)
    yield driver
    driver.quit()


def test_google_search(driver):
    driver.get("https://google.com")
    assert "Google" in driver.title
