from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path='/usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
# Make sure page loads completely
time.sleep(3)
print(driver.find_element_by_id("content").text)
driver.close()
