#sel.deselect_all()
#sel.deselect_by_index()

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class MultiSelectDropdown():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()

        elements = driver.find_element(By.ID,"multiple-select-example")
        sel = Select(elements)

        #check whether dropdown is multi select or not
        checkMulti = sel.is_multiple
        if checkMulti:
            print('It is multiselect ')

        # select any option
        sel.select_by_visible_text("Peach")

        # fetch all option of dropdown
        options =sel.options
            # loop over all options and print option name
        # for i in options:
        #     print(i.text)
        #
        #     #select all option
        #     sel.select_by_visible_text(i.text)
        # time.sleep(4)

        #fetch first selected option
        selectedOption = sel.first_selected_option
        print("first select opt "+ selectedOption.text)

        #select index 0 or 2
        toCheck = [0,2]
        for i in toCheck:
            sel.select_by_index(i)
            time.sleep(4)




a = MultiSelectDropdown()
a.test()



