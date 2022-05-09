# Twilio Side Project
This is a simple program that lets you text custom messages to registered Twilio accounts.

## Setup
To use this program, you need to create a free [Twilio account](https://www.twilio.com/). Follow the on-screen instructions necessary to register a Twilio phone number and to connect the phone number you wish to send messages to. Afterwords, locate your Account Sid and Auth Token under the Twilio console.

Navigate to this project's src subdirectory and run Users.py. This is where you will register your Account Sid, your Auth Token, your chosen personal number, and your given Twilio phone number with this project. When entering phone numbers in this program, make sure to include the international dialing prefix.
For example, if you are based in the US, you will need to enter +1 at the start of the phone numbers you are registering. If you made a mistake entering your information, follow the on-screen instructions provided in Users.py to delete a user and re-add a user.

## Usage
The syntax to run this program is:
- python3 main.py {name} {flag} {"message"}

Lets break down what name, flag, and message means.
- Name: The name of the user you registered in Users.py.
- Flag: One of three options: c, f, or m. 
    - C: Custom Text Message. Use this flag when you wish to only send a custom message directly from the command line
    - F: Text File Message. Use this flag when you wish to send the contents of a text file. Make sure to provide a relative
    path in the message body when choosing this flag.
    - M: Media File Message. Use this flag when you wish to send an image you found on the internet. Make sure to provide a link
    to the source in the message body when choosing this flag.
- Message: the content you are sending to the user. The information provided here depends on the chosen flag
    - For "C": the message is the content that you are sending to the user
    - For "F": the message is the relative path to the text file you are trying to send the contents of.
    - For "M": the message is the link of the image you found online.

## Scheduling Messages with Crontabs (Linux/MacOS)

Open your terminal and run crontab -e to create a new crontab. Scroll to the bottom and add a line to correspond with the time you wish to have your message sent, along with the command you wish you run.

Visit [crontab.guru](https://crontab.guru/#) for help creating crontab scheduling expressions. The syntax of this expression is "minute hour day_of_month day_of_week command". The command is the usage syntax you would normally run with this Twilio program. However, be sure to include the entire path of python and the entire path main.py. If you do not know what the path is to python on your computer, try running "which python" and it will return this for you.


## Scripting with APIs