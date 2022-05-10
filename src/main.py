import sys
from SendMessages import SendMessages
from Usage import usage
from Users import getUserList

messageType = ["-c", "-f", "-f1", "-f2", "-f3", "-m"]

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
if sys.argv[2].lower() == "-c":
    s.customText(sys.argv[3])
elif sys.argv[2].lower() == "-f" or sys.argv[2].lower == "-f1":
    s.textFileEntirety(sys.argv[3])
elif sys.argv[2].lower() == "-f2":
    s.textFileFirstLineAndDelete(sys.argv[3])
elif sys.argv[2].lower() == "-f3":
    s.textFileFirstLineAndSwap(sys.argv[3])
elif sys.argv[2].lower() == "-m":
    s.textMedia(sys.argv[3])