# driver_service.py
from selenium import webdriver
from selenium.webdriver.edge.service import Service  # Import the Service class
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)


def setup_driver(webdriver_path, url):
    # Setup Edge driver with Service
    service = Service(webdriver_path)
    edge_options = webdriver.EdgeOptions()
    edge_options.add_experimental_option("detach", True)
    edge_options.add_argument("--start-maximized")

    driver = webdriver.Edge(service=service, options=edge_options)

    driver.get(url)
    WebDriverWait(driver, 30).until(EC.title_contains("Intercompany"))
    logger.info("Fiori page opened successfully")

    return driver


def quit_driver(driver):
    driver.quit()
    logger.info("Driver closed successfully")
