from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import sys

path = sys.path[0] + '/chromedriver'
browerStatus = False

showLoginXPath = "/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/section[2]/div/ion-grid/ion-row[1]/ion-col[2]/ion-button"
APKeyInputXPath = "/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/section[2]/div/ion-grid/ion-row[2]/ion-col[1]/form/div/div[1]/ion-input/input"
passwordInputXPath = "/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/section[2]/div/ion-grid/ion-row[2]/ion-col[1]/form/div/div[2]/ion-input/input"
loginBtnXPath = "/html/body/app-root/ion-app/ion-router-outlet/app-login/ion-content/div/section[2]/div/ion-grid/ion-row[2]/ion-col[1]/form/div/div[3]/ion-button"
#signAttendanceXPath = "/html/body/app-root/ion-app/ion-router-outlet/app-tabs/ion-content/ion-tabs/div[1]/ion-router-outlet/app-dashboard/ion-content/div/ion-row/ion-col/ion-card[2]/ion-card-content/ion-row/ion-col[1]"
signAttendanceXPath = "/html/body/app-root/ion-app/ion-router-outlet/app-tabs/ion-content/ion-tabs/div[1]/ion-router-outlet/app-dashboard/ion-content/div/ion-row/ion-col[1]/ion-card[2]/ion-card-content/ion-row/ion-col[1]"
otpNum1XPath = "/html/body/app-root/ion-app/ion-router-outlet/app-student/ion-content/ion-grid/ion-row/ion-col/div/input[1]"
otpNum2XPath = "/html/body/app-root/ion-app/ion-router-outlet/app-student/ion-content/ion-grid/ion-row/ion-col/div/input[2]"
otpNum3XPath = "/html/body/app-root/ion-app/ion-router-outlet/app-student/ion-content/ion-grid/ion-row/ion-col/div/input[3]"


class Button():
    def __init__(self, xpath):
        self.xpath = xpath

    def click(self):
        wd.find_element(By.XPATH, self.xpath).click()


class Input():
    def __init__(self, xpath):
        self.xpath = xpath

    def send_keys(self, keys):
        wd.find_element(By.XPATH, self.xpath).send_keys(keys)


def initBrowser():
    global browerStatus
    if browerStatus == False:
        global wd
        # 禁止写屏
        options = webdriver.ChromeOptions()
        options.add_experimental_option(
            'excludeSwitches', ['enable-logging'])

        wd = webdriver.Chrome(service=Service(path), options=options)
        wd.get('https://apspace.apu.edu.my/login')
        # wd.get("https://apspace.apu.edu.my/tabs/dashboard")
        browerStatus = True
    else:
        wd.get('https://apspace.apu.edu.my/login')


def executeInLoginPage(APKey, password):
    showLoginButton = Button(showLoginXPath)
    showLoginButton.click()

    WebDriverWait(wd, 10).until(
        EC.element_to_be_clickable((By.XPATH, loginBtnXPath)))

    APKeyInput = Input(APKeyInputXPath)
    APKeyInput.send_keys(APKey)

    passwordInput = Input(passwordInputXPath)
    passwordInput.send_keys(password)

    loginBtn = Button(loginBtnXPath)
    loginBtn.click()


def executeInDashboardPage():
    WebDriverWait(wd, 10).until(
        EC.element_to_be_clickable((By.XPATH, signAttendanceXPath)))

    signAttendanceButton = Button(signAttendanceXPath)
    signAttendanceButton.click()


def executeInAttendancePage(code):
    WebDriverWait(wd, 10).until(
        EC.element_to_be_clickable((By.XPATH, otpNum3XPath)))

    otpNum1 = Input(otpNum1XPath)
    otpNum1.send_keys(code[0])

    otpNum2 = Input(otpNum2XPath)
    otpNum2.send_keys(code[1])

    otpNum3 = Input(otpNum3XPath)
    otpNum3.send_keys(code[2])


def finishAttend():
    # wd.delete_all_cookies()
    wd.execute_script("javascript:indexedDB.deleteDatabase('_ionicstorage');")
    sleep(0.5)


def main(Apkey, password, code):
    #print(Apkey, password, code)
    initBrowser()
    executeInLoginPage(Apkey, password)
    executeInDashboardPage()
    executeInAttendancePage(code)
    finishAttend()
