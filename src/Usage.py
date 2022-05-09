c = """Custom Text Message:
    Use this flag when you wish to only send a custom message directly from the command line"""
f = """Text File Message:
    Use this flag when you wish to send the contents of a text file. Make sure to provide a relative
    path in the message body when choosing this flag."""
m = """Media File Message:
    Use this flag when you wish to send an image/video/etc you found on the internet. Make sure to provide a link
    to the source in the message body when choosing this flag."""

def usage(error):
    print(f"Error! {error}.")
    print("Program syntax: python3 main.py {name} {flag} {\"message\"}")
    print("Name: the user you wish to send a message to."
          " Make you registered their twilio information using Users.py")
    print(f"Flag:\nc: {c}\nf: {f}\nm: {m}")
    print(f"Message: the content you are sending to the user. The information provided here depends on the chosen flag.")
    print("Refer to README.md for clarification on how to use this program")
