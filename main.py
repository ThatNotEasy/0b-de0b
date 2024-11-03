import os, time, random
from colorama import init, Fore, Style
from pyfiglet import figlet_format
from modules.ob_disassembly import ob_disassembly
from modules.ob_marshal import ob_marshal, generate_secret_key
from modules.ob_reconstruct import ob_reconstruct

# Initialize Colorama
init(autoreset=True)

def clear_terminal():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.WHITE]
    banner = figlet_format("0B-DE0B", font="slant")
    banner_color = random.choice(colors)
    print(f"{banner_color}{banner}{Fore.WHITE}{Style.DIM}Author: {Fore.GREEN}ThatNotEasy{Style.RESET_ALL}\n{Fore.RED}.++============================================++.\n")

def list_files(directory):
    """List all Python files in the given directory."""
    try:
        return [f for f in os.listdir(directory) if f.endswith('.py')]
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: UNABLE TO LIST FILES IN DIRECTORY: {e}")
        return []

def main():
    clear_terminal()  # Clear the terminal at the start
    print_banner()  # Print the banner
    
    print(f"{Fore.GREEN}SELECT AN OPTION:\n")
    print(f"{Fore.YELLOW}{Fore.RED}1.{Fore.YELLOW} OBFUSCATE A FILE")
    print(f"{Fore.YELLOW}{Fore.RED}2.{Fore.YELLOW} DISASSEMBLE AN OBFUSCATED FILE")
    print(f"{Fore.YELLOW}{Fore.RED}3.{Fore.YELLOW} RECONSTRUCT DISASSEMBLED CODE")
    
    choice = input(f"\n{Fore.WHITE}ENTER YOUR CHOICE {Fore.RED}(1-3): ")
    directory = '.'

    if choice == '1':
        clear_terminal()
        print_banner()
        print(f"\n{Fore.YELLOW}[INFO]: {Fore.GREEN}AVAILABLE PYTHON FILES FOR OBFUSCATION:\n")
        files = list_files(directory)
        for i, filename in enumerate(files):
            print(f"{Fore.GREEN}{Fore.RED}{i + 1}.{Fore.GREEN} {filename}")

        file_choice = int(input(f"\n{Fore.WHITE}SELECT THE FILE NUMBER TO OBFUSCATE: {Fore.RED}")) - 1
        if 0 <= file_choice < len(files):
            obfuscate_filename = files[file_choice]
            clear_terminal()
            print_banner()
            time.sleep(1)
            print(f"{Fore.YELLOW}\n[INFO]: {Fore.GREEN}OBFUSCATING THE FILE: {Fore.CYAN}{obfuscate_filename}")
            generate_secret_key()
            ob_marshal(obfuscate_filename)
        else:
            print(f"{Fore.RED}[ERROR]: INVALID FILE SELECTION.")

    elif choice == '2':
        clear_terminal()
        print_banner()
        print(f"{Fore.YELLOW}\n[INFO]: {Fore.GREEN}AVAILABLE OBFUSCATED FILES FOR DISASSEMBLY:\n")
        obfuscated_files = list_files("dist/")
        
        if not obfuscated_files:
            print(f"{Fore.RED}[ERROR]: No files available for disassembly in the 'dist/' directory.")
        else:
            for i, filename in enumerate(obfuscated_files):
                print(f"{Fore.RED}{i + 1}.{Fore.GREEN} {filename}")

            file_choice = int(input(f"\n{Fore.CYAN}SELECT THE FILE NUMBER TO DISASSEMBLE: ")) - 1
            if 0 <= file_choice < len(obfuscated_files):
                disassemble_filename = obfuscated_files[file_choice]
                clear_terminal()
                print_banner()
                time.sleep(1)
                print(f"{Fore.YELLOW}[INFO]: {Fore.GREEN}DISASSEMBLING THE FILE: {Fore.CYAN}{disassemble_filename}")
                ob_disassembly(os.path.join("dist", disassemble_filename))  # Pass the correct path
            else:
                print(f"{Fore.RED}[ERROR]: INVALID FILE SELECTION.")

    elif choice == '3':
        print(f"{Fore.YELLOW}\n[INFO]: {Fore.GREEN}RECONSTRUCTING DISASSEMBLED CODE...")
        disassemble_filename = input(f"{Fore.CYAN}ENTER THE FILENAME OF THE DISASSEMBLED CODE: ")
        
        if os.path.exists(disassemble_filename):
            with open(disassemble_filename, 'r') as file:
                disassembled_code = file.read()
            reconstructed_code = ob_reconstruct(disassembled_code)
            print(f"\n{Fore.GREEN}[INFO]: RECONSTRUCTED CODE:\n")
            print(reconstructed_code)
        else:
            print(f"{Fore.RED}[ERROR]:: FILE DOES NOT EXIST.")
            
    else:
        print(f"{Fore.RED}[ERROR]:: INVALID CHOICE. PLEASE SELECT A VALID OPTION.")

if __name__ == "__main__":
    main()