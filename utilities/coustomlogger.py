import logging

class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename="E:\\HANdlefile\\Log\\auto.log", mode = "a")
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s:", datefmt="%d%m%Y %I:%M:%S %p")
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger




