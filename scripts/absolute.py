import os

absolute_path = os.path.abspath("../src/main.py")

# add the absolute path of the user's PC to insult.sh
with open("insult.sh", "r") as file:
    data = file.read()
data = data.replace("absolute_path_to_main.py", absolute_path)
with open("insult.sh", "w") as file:
    file.write(data)

# add the absolute path of the user's PC to api.sh
with open("api.sh", "r") as file:
    data = file.read()
data = data.replace("absolute_path_to_main.py", absolute_path)
with open("api.sh", "w") as file:
    file.write(data)

print(f"Finished adding the absolute path {absolute_path} to api.sh and insult.sh")