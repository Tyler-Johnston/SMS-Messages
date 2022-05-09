import sys
from SendMessages import SendMessages
from Usage import usage
from Users import getUserList

messageType = ["c", "f", "m"]

if len(sys.argv) == 1:
    usage("Too few arguments")
    sys.exit()
elif sys.argv[1].lower() not in getUserList():
    usage("Missing or incorrect user")
    sys.exit()
elif sys.argv[2].lower() not in messageType:
    usage("Missing or incorrect message type")
    sys.exit()
elif len(sys.argv) == 3:
    usage("Missing message body")
    sys.exit()

s = SendMessages(sys.argv[1])
if sys.argv[2].lower() == "c":
    s.customText(sys.argv[3])
elif sys.argv[2].lower() == "f":
    s.textFile(sys.argv[3])
elif sys.argv[2].lower() == "m":
    s.textMedia(sys.argv[3])