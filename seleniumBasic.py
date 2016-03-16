from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='/usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
# driver = webdriver.firefox()
driver.set_window_size(1120, 550)
driver.get("https://duckduckgo.com/")
driver.find_element_by_id('search_form_input_homepage').send_keys("Search keyword here")
driver.find_element_by_id("search_button_homepage").click()
print(driver.current_url)
driver.quit()
