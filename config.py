# config.py
URL = "https://erpbusinessapps.ericsson.net/sap/bc/ui2/flp#ZFIRRB-display&/NewSAFRequest"
DtlShtPath = r"C:\Users\enesine\Downloads\MOAI Tracker\Fiori_Automation\Update_Detailsheet_MELA.xlsm"
DtlShtName = "NNstatus"
webdriver_path = r'C:\Users\enesine\PycharmProjects\NNandApprovers\Drivers\msedgedriver.exe'
columns_to_keep = ['NN']


Element_Loading_xpath="//*[@id='__page0-busyIndicator']/div"
Inputbox_Description_xpath = "//*[contains(@id,'idDescription')]/input"
Inputbox_NWID_xpath = "//*[contains(@id,'idCopyCostObjectOrdering')]/input"
Element_Loading_xpath="//*[@id='__page0-busyIndicator']/div"
Inputbox_ActivityID_xpath = "//*[contains(@id,'idNavNetwToActvty')]/input"
CheckBox_idNoNewActivity_xpath = "//*[contains(@id,'idNoNewActivity-CbBg')]"
Inputbox_SLC_xpath = "//*[contains(@id,'idSupplyingCompanyInput')]/input"
Button_ContButton_xpath = "//*[@id='__button10-BDI-content']"
Button_NextPer_xpath = "//*[@id='__button1-inner']"
DropDown_ApproverDropDown_xpath = "//*[contains(@id,'idApprover-label') and contains(@class,'sapMSltLabel')]"
Link_ApproverNames_xpath = "//span[@style='width: 40%;']"
Textbox_Comment_xpath = "//*[contains(@id,'idComment')]/textarea"
Button_SaveAsDraft_xpath = "//*[@id='__button16-BDI-content']"
Button_Submit_xpath = "//*[@id='__button17-BDI-content']"
Text_FioriNo_xpath = "//span[contains(text(), 'Form successfully')]"
Button_CreateNewSAF_xpath = "//bdi[contains(text(), 'Create New SAF')]"
Text_approverPage_xpath = "//*[contains(text(),'agreement')]"



