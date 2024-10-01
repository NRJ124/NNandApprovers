# excel_service.py
import pandas as pd
import xlwings as xw
import logging
import openpyxl
logger = logging.getLogger(__name__)

def load_excel_data(sheet_path, sheet_name, columns):
    data = pd.read_excel(sheet_path, sheet_name)
    filtered_data = data[columns].drop_duplicates()
    logger.info(f"Total number of NN : {len(filtered_data)}")
    return filtered_data['NN'].tolist()

def write_to_excel(sheet_path, sheet_name, status_data, approver_data):
    wb = xw.Book(sheet_path)
    sheet = wb.sheets[sheet_name]
    for idx, (status, approver) in enumerate(zip(status_data['Status'], status_data['ApproverName']), start=2):
        sheet.range((idx, 2)).value = status
        sheet.range((idx, 3)).value = approver
    wb.save()
    wb.close()
    logger.info(f"Data written successfully to {sheet_name}")
