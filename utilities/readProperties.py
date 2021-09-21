import configparser

config = configparser.RawConfigParser()
config.read("C://Users//nveenrm//PycharmProjects//pythonProject//ProjectDemo//configurations//config.ini")

class  ReadConfig:

    @staticmethod
    def getURL():
        appURL = config.get('common info', 'baseUrl')
        return appURL

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password