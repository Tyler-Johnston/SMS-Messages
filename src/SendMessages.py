from Twilio import Twilio

class SendMessages:
    def __init__(self,name):
        self.__t = Twilio(name)

    # text a custom message
    def customText(self, custom):
        self.__t.textMessage(custom)

    # text the entire contents of a text file
    def textFileEntirety(self, path):
        textFile = open(path)
        message = ""
        for line in textFile:
            if line.strip() != "":
                message += line.strip() + "\n"
        self.__t.textMessage(message)

    # text the first line in a text file. Afterwords, remove that line from the text file
    def textFileFirstLineAndDelete(self, path):
        with open(path, "r") as textRead:
            message = textRead.readline()
            file = textRead.readlines()[0:]
            self.__t.textMessage(message)

            with open(path, "w") as textWrite:
                for line in file:
                    line = line.replace("\n", "")
                    textWrite.write(line + "\n")

    # text the first line in a text file. Afterwords, place that line at the very end of the text file.
    def textFileFirstLineAndSwap(self, path):
        with open(path, "r") as textRead:
            message = textRead.readline()
            file = textRead.readlines()[0:]
            self.__t.textMessage(message)

            with open(path, "w") as textWrite:
                for line in file:
                    line = line.replace("\n", "")
                    textWrite.write(line + "\n")
                textWrite.write(message)

    # text an image
    def textMedia(self, link, msg=""):
        self.__t.textMedia(msg, link)