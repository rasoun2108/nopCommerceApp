from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import Login
from utilities.customLogger import LogGen

class Test_001:
    baseUrl = ReadConfig.getURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):

        self.logger.info("******** test_homepageTitle **********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.logger.info("******** verifying homepageTitle **********")
        act_title =  self.driver.title
        self.driver.save_screenshot("//screenshots//homePageTitle.png")
        self.driver.close()

        if act_title == "Your store. Login":
            assert True
            self.logger.info("******** homepageTitle is matched**********")
        else:
            self.logger.info("******** homepageTitle is not matched**********")
            self.driver.close()
            assert False

    def test_loginPage(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.logger.info("******** launching webseite **********")
        self.lp = Login(self.driver)

        self.lp.SetUserName(self.username)
        self.lp.SetPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("******** logging in **********")
        self.driver.save_screenshot("//screenshots//homePageTitle1.png")
        self.lp.clickLogout()
        self.logger.info("******** logging out **********")
        self.driver.close()

