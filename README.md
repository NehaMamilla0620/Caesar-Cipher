# Caesar Cipher Project

A simple and efficient Python implementation of the classic **Caesar Cipher**. This tool allows you to encrypt and decrypt messages by shifting the alphabet by a specified number of positions.

## 🚀 Features
*   **Case Sensitivity:** Correctly handles both uppercase and lowercase letters.
*   **Preservation:** Spaces, numbers, and symbols remain untouched.
*   **Smart Shifting:** Automatically handles large shift numbers using modulo arithmetic.
*   **Continuous Play:** Option to restart the program without having to re-run the script.

## 🛠️ How it Works
The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is replaced by a letter a fixed number of positions down the alphabet. For example, with a shift of **1**:
*   `A` becomes `B`
*   `Z` wraps around to `A`

## 💻 Usage
1. Make sure you have **Python 3** installed.
2. Copy the code into a file named `CaesarCipher.py`.
3. Run the script in your terminal:
   ```bash
   python CaesarCipher.py
   ```
4. Follow the on-screen prompts to encrypt or decrypt your message.

## 📄 Example
**Input:**
*   **Action:** `encrypt`
*   **Message:** `Hello World!`
*   **Shift:** `5`

**Output:**
*   `Mjqqt Btwqi!`

## 📜 License
This project is open-source and free to use for educational purposes.
