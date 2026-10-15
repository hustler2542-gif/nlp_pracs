# Experiment No. 1
# Aim: Perform Script Validation using Python

# Function to identify script
def validate_script(text):

    if text.isascii():
        print("\nScript Detected : English (ASCII)")
        print("Input contains only English characters.")

    elif all('\u0900' <= ch <= '\u097F' or ch.isspace() for ch in text):
        print("\nScript Detected : Devanagari")
        print("Input is written in Hindi/Marathi.")

    elif text.isdigit():
        print("\nInput contains only digits.")

    else:
        print("\nMixed or Other Unicode Script Detected.")

# Main Program
text = input("Enter any text : ")

print("\nEntered Text :", text)

validate_script(text)