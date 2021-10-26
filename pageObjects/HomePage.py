from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver = driver
    cancelButton=(By.ID,"wzrk-cancel")
    searchBoxButton=(By.ID,"4")
    searchInputButton=(By.CLASS_NAME,"eJZXli")
    selectDropdownButton=(By.CLASS_NAME,"sc-bbkauy")
    bookTicketButton=(By.CLASS_NAME,"cYhRUm")
    selectDateButton=(By.CLASS_NAME,"date-numeric")
    selectTimeButton=(By.XPATH,"//*[@data-date-time='08:00 PM']")
    acceptButton=(By.XPATH,"//*[text()='Accept']")
    numberOfSeatsButton=(By.XPATH,"//*[@id='pop_3']")
    seatButton=(By.XPATH,"//*[@id='proceed-Qty']")
    seat1Button=(By.ID,"A_1_012")
    seat2Button = (By.ID, "A_1_015")
    seat3Button = (By.ID, "A_1_017")
    proceedButton=(By.XPATH,"//*[@id='btnSTotal_reserve']")

    def cancel(self):
        return self.driver.find_element(*HomePage.cancelButton)

    def searchBox(self):
        return self.driver.find_element(*HomePage.searchBoxButton)

    def searchInput(self):
        return self.driver.find_element(*HomePage.searchInputButton)

    def selectDropdown(self):
        return self.driver.find_element(*HomePage.selectDropdownButton)

    def bookTicket(self):
        return self.driver.find_element(*HomePage.bookTicketButton)

    def selectDate(self):
        return self.driver.find_elements(*HomePage.selectDateButton)

    def selectTime(self):
        return self.driver.find_element(*HomePage.selectTimeButton)

    def accept(self):
        return self.driver.find_element(*HomePage.acceptButton)

    def numberOfSeats(self):
        return self.driver.find_element(*HomePage.numberOfSeatsButton)

    def selectSeat(self):
        return self.driver.find_element(*HomePage.seatButton)

    def selectSeat1(self):
        return self.driver.find_element(*HomePage.seat1Button)

    def selectSeat2(self):
        return self.driver.find_element(*HomePage.seat2Button)

    def selectSeat3(self):
        return self.driver.find_element(*HomePage.seat3Button)

    def proceed(self):
        return self.driver.find_element(*HomePage.proceedButton)








