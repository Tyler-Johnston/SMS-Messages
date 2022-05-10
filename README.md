# SMS-Messaging Using Twilio
This is a simple command-line program that lets you text custom messages to registered Twilio accounts.

## Setup
1. To use this program, you need to create a free [Twilio account](https://www.twilio.com/). Follow the on-screen instructions necessary to register a Twilio phone number and to connect the phone number you wish to send messages to. Afterwords, locate your Account Sid and Auth Token under the Twilio console.

2. Navigate to this project's "src" subdirectory and run Users.py. This is where you will register your Account Sid, your Auth Token, your chosen personal number, and your given Twilio phone number with this project. When entering phone numbers in this program, make sure to include the international dialing prefix.
For example, if you are based in the US, you will need to enter +1 at the start of the phone numbers you are registering. If you made a mistake entering your information, follow the on-screen instructions provided in Users.py to delete a user and re-add a user.

## Usage
The syntax to run this program is:

    python main.py {name} {-flag} {"message"}
    
Lets break down what "name", "flag", and "message" means.
- Name: The name of the user you registered in Users.py.
- Flag: Each flag serves a unique purpose when sending messages.
    - -C: Custom Text Message. Use this flag when you wish to only send a custom message directly from the command line
    - -F1 (or simply -F): Text File Message (1). Use this flag when you wish to send the entire contents of a text file. Make sure to provide a relative
    path in the message body when choosing this flag.
    - -F2: Text File Message (2). Use this when you wish to send the first line of a text file and delete it from the text file after it is sent. Perfect if each line is only needed once.
    - -F3: Text File Message (3). Use this when you wish to send the first line of a text file and place its position at the very end of the text file. Perfect if you wish to cycle through content.
    - -M: Media File Message. Use this flag when you wish to send an image you found on the internet. Make sure to provide a link
    to the source in the message body when choosing this flag.
- Message: the content you are sending to the user. The information provided here depends on the chosen flag
    - For "C": the message is the content that you are sending to the user
    - For "F": the message is the relative path to the text file you are trying to send the contents of.
    - For "M": the message is the link of the image you found online.

For example, if you wanted to send the custom message "hello world!" to a user registered as "Tom", you would run the following command:

    python main.py tom -c "hello world"

If you had a text file called "recipe.txt", you would write down its relative path as the "message body". Sending the contents of a text file may look like the following:

    python main.py tom -f "../recipe.txt"

Lastly, if you wanted to send an image of a cat, you could run the following:

    python main.py tom -m "https://i.natgeofe.com/n/46b07b5e-1264-42e1-ae4b-8a021226e2d0/domestic-cat_thumb_square.jpg"

## Scheduling Messages with Crontabs (Linux/MacOS)

One of the reasons you may want to have an SMS command line program is to schedule text messages to be sent at certain times of the day. This can easily be accomplished with crontabs.

Open your terminal and run crontab -e to create a new crontab. Scroll to the bottom and add a line to correspond with the time you wish to have your message sent, along with the command you wish you run.

Visit [crontab.guru](https://crontab.guru/#) for help creating crontab scheduling expressions. The syntax of this expression is "minute hour day_of_month day_of_week command". The command is the usage syntax you would normally run with this Twilio program; this time however, it needs to include the absolute path of "python" and the absolute path of "main.py". If you do not know what the absolute path for python is on your computer, try running the command "which python" and it will return this for you. If you do not know the absolute path of main.py, run absolute.py in the "scripts" subdirectory and it will return this for you.

## Scripting with APIs

While you can send custom messages or images using this command directly from your personal computer, the beauty of this project comes with creating scripts and combining it with different APIs. If you set this up with crontabs or some other scheduler, you will be able to send/receive custom messages using any of the thousands of free APIs available online.

The scripts subdirectory contains the script "api.sh". You can use this to send text messages using any compatible API found online. For example, you can use this script to send the word of the day, quotes, insults, etc., as long as there is an API that provides this information for you.

Before you can run this, however, you will need to run the following commands:

1. chmod +x api.sh

    This will make the script executable.

2. absolute.py

    The script requires it to be linked with the absolute path of main.py. Instead of having you find the absolute path of main.py yourself and editing each of these files manually, this program will fill in the details for you.

    If you ever mess up the absolute path and you wish to run the program again, you will need to edit the file, replace the corrupted absolute path with "absolute_path_to_main.py", and run absolute.py again.

The syntax of api.sh is as follows:

    ./api.sh {user} {-flag} {"link to the API call"}

For example, api.sh can be used to send an insult. The syntax of this looks like the following (using an insult API):

    ./api.sh tom -c "https://insult.mattbas.org/api/insult"

Add your own scripts to this subdirectory too!

## Trouble Shooting

1. If "python" doesn't work, try running "python3". 

2. Make sure you are running this command while you are within the "src" subdirectory. Or, if you are running a script, make sure that it is being run inside the "scripts" subdirectory. Otherwise, you may run into the following error message:
   
        Traceback (most recent call last):
        File "src/Users.py", line 5, in <module>
            connection = sqlite3.connect(os.path.abspath("../database/userinfo.db"))
        sqlite3.OperationalError: unable to open database file

3. If you are entering a message in the message body and **dquote>** appears instead, you will need to finish the quote by entering the quote symbol (") in again. This most commonly occurs when you are missing the end of your quotation, or you are adding an exclamation mark at the end of your messasge. (For example, if you wanted to send the message "Hello world!") To fix this, use single quotes instead ('Hello world!').