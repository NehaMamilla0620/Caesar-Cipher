# Caesar-Cipher
Caesar Cipher Tool
A lightweight, efficient Python implementation of the classic Caesar Cipher. This tool allows users to encrypt or decrypt messages by shifting letters along the alphabet while preserving the original case (uppercase/lowercase) and leaving symbols/numbers untouched.
🚀 Features
Dual Mode: Easily switch between encrypt and decrypt.
Case Sensitive: Maintains the casing of your original message (e.g., "Hello" becomes "Khoor").
Special Character Support: Spaces, numbers, and punctuation remain unchanged.
Large Shift Handling: Uses the modulo operator to handle shift numbers greater than 26.
User-Friendly Loop: Run multiple transformations without restarting the script.
🛠️ How It Works
The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
For example, with a shift of 3:
A becomes D
B becomes E
z becomes c (wraps around)
💻 Installation
Ensure you have Python 3.x installed.
Clone this repository or download the source code.
No external libraries are required (uses built-in string module).
📖 Usage
Run the script using your terminal:
bash
python CaesarCipher.py


Example:
text
Type 'encrypt' or 'decrypt': encrypt
Type your message: Hello World!
Type the shift number: 5

Here is the encrypted result: Mjqqt Btwqi!

📝 License
This project is open-source and free to use.
