import marshal
import dis
import re
import sys
import io
import os
import contextlib
from colorama import init, Fore
from modules.ob_marshal import load_secret_key, xor_encrypt_decrypt

# Initialize Colorama
init(autoreset=True)

def ob_disassembly(obfuscated_file):
    key = load_secret_key()  # Load the secret key for decryption

    try:
        # Open the obfuscated file in binary mode
        with open(obfuscated_file, 'rb') as f:
            obfuscated_content = f.read()
        print(f"{Fore.GREEN}[INFO]: SUCCESSFULLY READ THE FILE: '{obfuscated_file}'")
    except FileNotFoundError:
        print(f"{Fore.RED}[ERROR]: THE FILE '{obfuscated_file}' DOES NOT EXIST.")
        sys.exit(1)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: ERROR READING THE FILE: {e}")
        sys.exit(1)

    try:
        # Decrypt the content
        decrypted_data = xor_encrypt_decrypt(obfuscated_content, key)
        code_object = marshal.loads(decrypted_data)
        print(f"{Fore.GREEN}[INFO]: SUCCESSFULLY DECRYPTED AND LOADED THE MARSHALLED DATA TO BYTECODE.")
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: ERROR DECRYPTING OR LOADING MARSHALLED DATA: {e}")
        sys.exit(1)

    # Capture the disassembled output
    disassembled_code = io.StringIO()
    with contextlib.redirect_stdout(disassembled_code):
        dis.dis(code_object)

    disassembled_output = disassembled_code.getvalue()
    
    # Print the disassembled code to console
    print(f"\n{Fore.GREEN}[INFO]: DISASSEMBLED CODE:")
    print(disassembled_output)
    
    # Save the disassembled code to a text file
    output_filename = os.path.join("dist", "disassembled_output.txt")
    with open(output_filename, 'w') as output_file:
        output_file.write(disassembled_output)
    
    print(f"{Fore.GREEN}[SUCCESS]: DISASSEMBLED CODE SAVED TO: {output_filename}")