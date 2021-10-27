from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://arithmetic.zetamac.com/game?key=72740d67")
time.sleep(3)

while 1:
  question = driver.find_element(By.CSS_SELECTOR, "html body div#game div.banner div.start span.problem") 
  answer = driver.find_element(By.CSS_SELECTOR, ".answer")
  question = question.text
  question = question.replace("÷", "/")
  question = question.replace("×", "*")
  question = question.replace("–", "-")
  answer.send_keys(int(eval(question)))
  answer.send_keys(Keys.RETURN)

time.sleep(3)
driver.close()
