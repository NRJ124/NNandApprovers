# main.py
import logging
from driver_service import setup_driver, quit_driver
from excel_service import load_excel_data, write_to_excel
from form_service import process_nn_list, prevent_sleep, restore_sleep
from notification_service import show_popup
import config

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Prevents sleep
prevent_sleep()

def main():
    try:
        # Setup the WebDriver
        driver = setup_driver(config.webdriver_path, config.URL)

        # Load NN list from Excel
        nn_list = load_excel_data(config.DtlShtPath, config.DtlShtName, config.columns_to_keep)

        # Process the NN list
        nn_status_map = process_nn_list(driver, nn_list)

        # Write results to Excel
        write_to_excel(config.DtlShtPath, config.DtlShtName, nn_status_map, nn_status_map['ApproverName'])

        # Show popup notification
        show_popup()

    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        quit_driver(driver)


if __name__ == "__main__":
    main()

restore_sleep()  # Restores sleep after tests