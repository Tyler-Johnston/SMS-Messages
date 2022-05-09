from twilio.rest import Client
from Users import getUserData

class Twilio():

    def __init__(self, name):
        self.__account_sid = getUserData(name)[0]
        self.__auth_token = getUserData(name)[1]
        self.__client = Client(self.__account_sid, self.__auth_token)
        self.__personalNum = getUserData(name)[2]
        self.__twilioNum = getUserData(name)[3]

    def textMessage(self, body):
        return self.__client.messages.create(
            to=self.__personalNum,
            from_=self.__twilioNum,
            body=body)

    def textMedia(self, body, link):
        return self.__client.messages.create(
            to=self.__personalNum,
            from_=self.__twilioNum,
            body=body,
            media_url=link)