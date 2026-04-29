import string

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decrypt":
        shift_amount *= -1
        
    for char in start_text:
        if char.isalpha():
            start_alphabet = string.ascii_uppercase if char.isupper() else string.ascii_lowercase
            index = start_alphabet.index(char)
            new_char = start_alphabet[(index + shift_amount) % 26]
            end_text += new_char
        else:
            end_text += char
            
    print(f"Here is the {cipher_direction}ed result: {end_text}")

should_continue = True
while should_continue:
    direction = input("\nType 'encrypt' or 'decrypt': ").lower()
    text = input("Type your message: ") # Removed .lower() so we can see uppercase
    shift = int(input("Type the shift number: "))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    if input("Continue? (yes/no): ").lower() == "no":
        should_continue = False
        print("Goodbye!")
