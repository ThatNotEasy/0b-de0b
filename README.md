**Purpose:** This tool is designed to secure and conceal Python code through obfuscation using marshal and XOR encryption. It allows users to store code safely and prevent unauthorized access.

## Key Features

1. **Code Obfuscation:**
   - Takes Python files, compiles them, and transforms them into encrypted marshaled forms.
   - Uses a generated secret key to encrypt the marshaled content, ensuring that only users with the key can decrypt and execute the code.

2. **Disassembly:**
   - Allows users to decode and disassemble obfuscated files.
   - Displays the resulting bytecode for further analysis.

3. **Secret Key Management:**
   - Generates a 256-bit secret key saved in a file, ensuring the key remains secure and is not shared.
   - Loads the secret key when needed for decryption.

4. **User-Friendly Interface:**
   - Clear interface with color coding to display information, success messages, and errors.
   - Provides interactive options to obfuscate, disassemble, and reconstruct code.

## Security Note
- Users are reminded to keep the secret key safe and not to share it to prevent unauthorized access to the code.

This tool is beneficial for developers looking to protect their work and complicate code understanding by unauthorized third parties.

### Image 1: Tool Interface
![Tool Interface](https://github.com/user-attachments/assets/7d50d673-71e1-4511-a7e1-bb79bccdbcbd)
- This image showcases the main interface of the obfuscation tool. It presents a clean and user-friendly layout, with clear options for users to choose from, such as obfuscating a file, disassembling an obfuscated file, and reconstructing disassembled code. The use of color coding enhances the visual experience, making it easy to navigate.

### Image 2: Disassembly Output
![Disassembly Output](https://github.com/user-attachments/assets/199e3e07-2f72-49f2-a77b-512dbedb9073)
- This image illustrates the output generated after disassembling an obfuscated file. It displays the disassembled bytecode, allowing users to analyze the inner workings of the obfuscated code. The output format is clear and organized, making it easy to review and understand the disassembled content.
