from Twilio import Twilio

class SendMessages:
    def __init__(self,name):
        self.__t = Twilio(name)

    def customText(self, custom):
        self.__t.textMessage(custom)

    def textFile(self, path):
        textFile = open(path)
        message = ""
        for line in textFile:
            if line.strip() != "":
                message += line.strip() + "\n"
        self.__t.textMessage(message)

    def textMedia(self, link, msg=""):
        self.__t.textMedia(msg, link)