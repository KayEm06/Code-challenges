morse_codes = {
    "A":".- ",
    "B":"-... ",
    "C":"-.-. ",
    "D":"-.. ",
    "E":". ",
    "F":"..-. ",
    "G":"--. ",
    "H":".... ",
    "I":".. ",
    "J":".--- ",
    "K":"-.- ",
    "L":".-.. ",
    "M":"-- ",
    "N":"-. ",
    "O":"--- ",
    "P":".--. ",
    "Q":"--.- ",
    "R":".-. ",
    "S":"... ",
    "T":"- ",
    "U":"..- ",
    "V":"...- ",
    "W":".-- ",
    "X":"-..- ",
    "Y":"-.-- ",
    "Z":"--.. ",
    "1":".---- ",
    "2":"..--- ",
    "3":"....- ",
    "4":"....- ",
    "5":"..... ",
    "6":"-.... ",
    "7":"--... ",
    "8":"---.. ",
    "9":"----. ",
    "0":"----- ",
    "?":"..--.. ",
    "!":"-.-.-- ",
    ",":"--..-- ",
    "+":".-.-. ",
}

def main():
    option = input("Would you like to translate to or from morse code, or quit? ")
    if option.lower() == "quit":
        print("Quitting")
        quit()
    elif option.lower() == "to":
        print(morse_code_to())
    elif option.lower() == "from":
        print(morse_code_from())
    else:
        print("I don't recognise that option")

def morse_code_to():
    string = input("Enter the string you want to encode: ").upper()
    string = string.replace(" ", "|")
    for key,value in morse_codes.items():
        for char in string:
            if char == key:
                string = string.replace(char, value)
    
    return string

def morse_code_from():
    encoded_string = input("Enter the encoded string you want to decode (separate words with a '|'): ")
    reversed_dict = {value: key for key, value in morse_codes.items()}

    encoded_string = encoded_string.split()

    result = ""
    for seq1 in encoded_string:
        for seq2 in reversed_dict:
            seq2 = seq2.strip()
            if seq1 == seq2:
                result += reversed_dict[seq2 + " "]
            elif seq1 == "|":
                result += " "
                break
    return result

main()