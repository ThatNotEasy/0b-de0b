import os, time
import marshal
import secrets
from colorama import init, Fore

# Initialize Colorama
init(autoreset=True)

def generate_secret_key():
    """Generates and saves a 256-bit secret key in 'dist' directory."""
    os.makedirs('dist', exist_ok=True)
    secret_key = secrets.token_bytes(32)
    with open(os.path.join('dist', 'secret_key.key'), 'wb') as key_file:
        key_file.write(secret_key)
    print(f"{Fore.YELLOW}[INFO]: {Fore.GREEN}SECRET KEY GENERATED AND SAVED TO {Fore.CYAN}dist/secret_key.key")

def load_secret_key():
    """Loads the secret key from 'dist/secret_key.key'."""
    key_path = os.path.join('dist', 'secret_key.key')
    if not os.path.exists(key_path):
        raise FileNotFoundError("SECRET KEY NOT FOUND. RUN `GENERATE_SECRET_KEY()` FIRST.")
    with open(key_path, 'rb') as key_file:
        return key_file.read()

def xor_encrypt_decrypt(data, key):
    """Encrypts/decrypts data using XOR with the given key."""
    return bytearray(b ^ key[i % len(key)] for i, b in enumerate(data))

def ob_marshal(filename):
    os.makedirs('dist', exist_ok=True)
    key = load_secret_key()

    try:
        with open(filename, 'r') as file:
            code_content = file.read()
            print(f"{Fore.YELLOW}[INFO]: {Fore.GREEN}SUCCESSFULLY READ THE FILE: {Fore.CYAN}{filename}")
        
        compiled_code = compile(code_content, filename, 'exec')
        marshaled_code = marshal.dumps(compiled_code)
        encrypted_code = xor_encrypt_decrypt(marshaled_code, key)
        
        output_filename = os.path.join('dist', 'ob_' + filename)
        with open(output_filename, 'wb') as output_file:
            output_file.write(encrypted_code)
        
        time.sleep(2)
        print(f"\n{Fore.YELLOW}[SUCCESS]: {Fore.GREEN}OBFUSCATED CODE SAVED TO: {Fore.CYAN}{output_filename}\n")

    except FileNotFoundError:
        print(f"{Fore.RED}[ERROR]: THE FILE '{filename}' WAS NOT FOUND. PLEASE CHECK THE FILENAME AND TRY AGAIN.")
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: AN ERROR OCCURRED: {str(e)}")