from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time


chromedriver_autoinstaller.install()

driver = webdriver.Chrome()


driver.get("http://localhost:8000/dz.html")

try:
    driver.switch_to.frame(driver.find_element(By.ID, "frame1"))
    input1 = driver.find_element(By.ID, 'input1')
    input1.send_keys("Frame1_Secret")
    button_check = driver.find_element(By.XPATH, "/html/body/button")
    button_check.click()
    alert = Alert(driver)
    time.sleep(1)
    alert_text = alert.text
    if "Верифікація пройшла успішно!" in alert_text:
        print("Frame 1 verification successful.")
    else:
        print("Frame 1 verification failed.")
    alert.accept()
    time.sleep(1)
    driver.switch_to.default_content()

    driver.switch_to.frame(driver.find_element(By.ID, "frame2"))
    input2 = driver.find_element(By.ID, 'input2')
    input2.send_keys("Frame2_Secret")
    button_check = driver.find_element(By.XPATH, "/html/body/button")
    button_check.click()
    alert = Alert(driver)
    time.sleep(1)
    alert_text = alert.text
    if "Верифікація пройшла успішно!" in alert_text:
        print("Frame 2 verification successful.")
    else:
        print("Frame 2 verification failed.")
    alert.accept()
    time.sleep(1)
    driver.switch_to.default_content()

finally:
    time.sleep(2)
    driver.quit()
