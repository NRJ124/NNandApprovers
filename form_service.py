# form_service.py
import ctypes
from telnetlib import EC

import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import logging
import config

from selenium.webdriver.support.wait import WebDriverWait



from driver_service import setup_driver

logger = logging.getLogger(__name__)

def fill_form(driver, nn):
    driver.find_element(By.XPATH, config.Inputbox_Description_xpath).send_keys("Hello")
    driver.find_element(By.XPATH, config.Inputbox_NWID_xpath).send_keys(nn, Keys.ENTER)
    time.sleep(10)
    driver.find_element(By.XPATH, config.CheckBox_idNoNewActivity_xpath).click()
    driver.find_element(By.XPATH, config.Inputbox_SLC_xpath).send_keys(2828, Keys.ENTER)
    time.sleep(5)
    driver.find_element(By.XPATH, f'//*[@id="__input2-application-ZFIRRB-display-component---NewSAFRequest--idManHours-0-inner"]').send_keys(23543449, Keys.ENTER)
    time.sleep(5)
    try:
        driver.find_element(By.XPATH, f'//*[@id="__select0-application-ZFIRRB-display-component---NewSAFRequest--idManHours-0-label"]').click()
        driver.find_element(By.XPATH, f'//li[contains(@id,"idManHours-0") and contains(text(), "Remote")]').click()
    except Exception as exp:
        pass
    driver.find_element(By.XPATH, f'//*[@id="__selection0-application-ZFIRRB-display-component---NewSAFRequest--idManHours-0-inner"]').send_keys("05.09.2024  to  05.09.2024")
    driver.find_element(By.XPATH, f'//*[@id="__input3-application-ZFIRRB-display-component---NewSAFRequest--idManHours-0-inner"]').send_keys('1')
    driver.find_element(By.XPATH, config.Button_ContButton_xpath).click()
    time.sleep(2)
    logger.info(f"Driver moved to approver page")
    driver.find_element(By.XPATH, config.DropDown_ApproverDropDown_xpath).click()
    time.sleep(5)
    driver.find_element(By.XPATH, config.Link_ApproverNames_xpath).click()
    logger.info(f"Filled form for NN: {nn}")

def handle_approvers(driver):
    approvers = driver.find_elements(By.XPATH, "//span[@style='width: 40%;']")
    approver_list = ",".join([a.text for a in approvers])
    return approver_list or "No Approver Found"

#//span[@style='width: 40%;' and @class='sapMSelectListCell sapMSelectListLastCell']
def process_nn_list(driver, nn_list):
    nn_status = []
    approvers = []
    for nn in nn_list:
        logger.info(f"Processing NN: {int(nn)}")
        time.sleep(5)
        try:
            fill_form(driver, int(nn))
            approvers.append(handle_approvers(driver))
            nn_status.append("Valid NN")
            driver.get(config.URL)
            driver.refresh()
            # WebDriverWait(driver, 30).until(EC.title_contains("Intercompany"))
        except Exception as e:
            if 'idNoNewActivity' in str(e):
                logger.error(f"Invalid NN: {int(nn)}")
                nn_status.append("Invalid NN")
                approvers.append("")
                time.sleep(2)
                driver.find_element(By.XPATH, "//*[contains(@id,'idDescription')]/input").clear()
            else:
                raise e
    return pd.DataFrame({'NN': nn_list, 'Status': nn_status, 'ApproverName': approvers})


def prevent_sleep():
    # Prevents the system from sleeping or turning off the screen
    ES_CONTINUOUS = 0x80000000
    ES_SYSTEM_REQUIRED = 0x00000001
    ES_DISPLAY_REQUIRED = 0x00000002
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED)

def restore_sleep():
    # Allows the system to sleep again
    ES_CONTINUOUS = 0x80000000
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)