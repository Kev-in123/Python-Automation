from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSc3Wp9C6pR2g4KpPgclcJCsN_U7jdc0rWRLk1R4jkj3uxyUpA/viewform")
time.sleep(3)

discord_tag = driver.find_element(By.CSS_SELECTOR, "div.freebirdFormviewerViewNumberedItemContainer:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
discord_tag.send_keys("!!!ahhhhh!!!#7441")
repo = driver.find_element(By.CSS_SELECTOR, ".freebirdFormviewerComponentsQuestionTextUrl > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
repo.send_keys("https://github.com/Kev-in123/Python-Automation-Thingy")
something = driver.find_element(By.CSS_SELECTOR, "div.freebirdFormviewerComponentsQuestionRadioChoice:nth-child(1) > label:nth-child(1)")
something.click()
tags1 = driver.find_element(By.CSS_SELECTOR, "div.freebirdFormviewerComponentsQuestionCheckboxChoice:nth-child(1) > label:nth-child(1)")
tags1.click()
tags2 = driver.find_element(By.CSS_SELECTOR, "div.freebirdFormviewerComponentsQuestionCheckboxChoice:nth-child(2) > label:nth-child(1)")
tags2.click()
type = driver.find_element(By.CSS_SELECTOR, "div.freebirdFormviewerViewNumberedItemContainer:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
type.send_keys("something")
pick = driver.find_element(By.CSS_SELECTOR, ".quantumWizMenuPaperselectEl")
pick.click()
option1 = driver.find_element(By.CSS_SELECTOR, ".exportSelectPopup > div:nth-child(3) > span:nth-child(2)")
option1.click()
submit = driver.find_element(By.CSS_SELECTOR, ".appsMaterialWizButtonPaperbuttonFilled > span:nth-child(3)")
submit.click()

time.sleep(3)
driver.close()
