import pyttsx3
from os import system

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# get the words from user
def get_words():
    user_words = input("Enter the words: ")
    return user_words


# get the file from user
def open_file():
    while True:
        file_folder = input("""If file and app in same folder ? 
if yes - y
if no - n
Enter your answer: """).lower()
        if file_folder == "y":
            file_name = input("Enter file name with extension: ")
            break
        elif file_folder == "n":
            file_name = input("Enter the entire file location: ")
            break
        else:
            print("Please, enter correct value")
    text_file = open(file_name, "r")
    user_words = text_file.read()
    text_file.close()
    return user_words


# Function to convert words into speech
def convert_to_speech(given_words):
    engine.say(given_words)
    engine.runAndWait()


running = True
while running:
    is_file_or_words = input("""Are you going to type or take already typed file ?
Going to type           - 't'
take Already typed file - 'o'
Enter your answer: """).lower()

    # check the user input
    if is_file_or_words == 't':
        system('cls')
        words = get_words()
        convert_to_speech(words)

    elif is_file_or_words == 'o':
        system('cls')
        words = open_file()
        convert_to_speech(words)

    else:
        print("Please enter the correct value")
        continue

    while True:
        system("cls")
        running = input("""Want to Continue? 
Yes - 's'
No  - 'n'
Enter Your Answer: """).lower()
        if running == 's':
            system("cls")
            break

        elif running == 'n':
            running = False
            system("cls")
            break

        else:
            print("Please enter correct value")
