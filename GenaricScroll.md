# HANdlefiles
while next_value<300000:
    driver.execute_script("window.scrollTo({},{});".format(initial_value, next_value))
    browser.find_element_by_link_text("Read More...").click()
    initial_value=next_value
    next_value+=300
