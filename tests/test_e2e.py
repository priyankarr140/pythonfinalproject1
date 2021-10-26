import time
from pageObjects.HomePage import HomePage
from utilities.Base import BaseClass

#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_booktickets(self):
        try:
            logs = self.get_logger()
            logs.debug("Hello3")
            self.driver.implicitly_wait(20)
            self.callActiveElement(self.driver)
            homePage=HomePage(self.driver)
            homePage.cancel().click()
            homePage.searchBox().click()
            homePage.searchInput().send_keys("hon")
            homePage.searchInput().click()
            print("*******reached******")
            #time.sleep(10)
            self.explicitwait(self.driver,"sc-bbkauy")

           # homePage.selectDropdown().click()

            homePage.bookTicket().click()
            dates=homePage.selectDate()
            try:
                for date in dates:
                    if date.text == "21":
                        date.click()
            finally:
                time.sleep(10)
                homePage.selectTime().click()
                self.callActiveElement(self.driver)
                homePage.accept().click()
                self.callActiveElement(self.driver)
                homePage.numberOfSeats().click()
                homePage.selectSeat().click()
                homePage.selectSeat1().click()
                homePage.selectSeat2().click()
                homePage.selectSeat3().click()
                homePage.proceed().click()
                time.sleep(15)
                assert 1==1
                self.takescreenshot(self.driver)
        except:
            assert 1==0
            self.takescreenshot(self.driver)










