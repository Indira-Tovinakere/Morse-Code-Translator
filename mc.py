class MorseCodeTranslator:
    def __init__(self):
        self.morse_code_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..',
            '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
            ' ': ' '
        }
    
    def text_to_morse(self, text):
        morse_code = []
        for char in text.upper():
            if char in self.morse_code_dict:
                morse_code.append(self.morse_code_dict[char])
        return ' '.join(morse_code)
    
    def morse_to_text(self, morse_code):
        inverted_dict = {value: key for key, value in self.morse_code_dict.items()}
        decoded_text = []
        for code in morse_code.split(' '):
            if code in inverted_dict:
                decoded_text.append(inverted_dict[code])
        return ''.join(decoded_text)


def main():
    translator = MorseCodeTranslator()
    
    while True:
        print("1. Text to Morse Code")
        print("2. Morse Code to Text")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            text = input("Enter the text: ")
            morse_code = translator.text_to_morse(text)
            print("Morse Code:", morse_code)
        elif choice == '2':
            morse_code = input("Enter the Morse code: ")
            text = translator.morse_to_text(morse_code)
            print("Decoded Text:", text)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
