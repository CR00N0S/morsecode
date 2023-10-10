morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

user_input = input("enter the massage to be converted").upper()


def text_to_morse(text):
    final_output = ""
    for chars in text:
        final_output += morse_code_dict[chars]
    return final_output


def morse_to_test(moese):
    output = ''
    morse_code_list = moese.split(' ')
    for c in morse_code_list:
        for key, value in morse_code_dict.items():
            if c == value:
                output += key
                break
    return output


code = text_to_morse(user_input)
print(code)
print(morse_to_test(code))
