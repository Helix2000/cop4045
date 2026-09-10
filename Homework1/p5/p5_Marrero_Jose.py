import string
# A)
def caesar_cipher(text, shift):
    letters = string.ascii_lowercase
    result = ""

    for char in text:
        if char in letters:
            old_index = letters.index(char)
            new_index = (old_index + shift) % 26
            result += letters[new_index]

        elif char in letters.upper():
            old_index = letters.upper().index(char)
            new_index = (old_index + shift) % 26
            result += letters.upper()[new_index]
        else:   
            result += char
    return result

# B)
def caesar_decipher(cyphertext, shift):
    og_text = caesar_cipher(cyphertext, -shift)
    return og_text

# C)
def  letter_frequency(text):
    letters = string.ascii_lowercase
    frequency = {}

    for letter in letters:
        frequency[letter] = 0

    for char in text.lower():
        if char in letters:
            frequency[char] += 1

    return frequency

# D) 
def main():
    while True:
        print("Caeser Cipher Menu:")
        print("1. Encrypt, Decrypt, or Analyze Text")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            message = input("Enter your message: ")

            try:
                shift = int(input("Enter Shift Value: "))
            except ValueError:
                print("Invalid shift value. Please enter an integer.")
                continue

            ciphertext = caesar_cipher(message, shift)
            frequency = letter_frequency(message)
            deciphered_text = caesar_decipher(ciphertext, shift)

            print('Cybertext:', ciphertext)
            print('Letter Frequency:', frequency)

            for letter, count in frequency.items():
                print(letter, ":", count)
                print("Deciphered Text:", deciphered_text)
        elif choice == "2":
            print("Exiting")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()