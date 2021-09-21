import logging
class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="//logs//automation.Log",
                            format='%(asctime)s: %(levelname)s: %(messages)s:', datefmt='%m-%d-%Y %I:%M:%S %p'
                            )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        return logger
