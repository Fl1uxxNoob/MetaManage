import subprocess
import os
from colorama import Fore, init

os.system("cls")

init(autoreset=False)

#COLORS
white = Fore.WHITE
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blu = Fore.BLUE

title = f"""{red}
  __  __ _____ _____  _      __  __    _    _   _    _    ____ _____ ____  
 |  \/  | ____|_   _|/ \    |  \/  |  / \  | \ | |  / \  / ___| ____|  _ \ 
 | |\/| |  _|   | | / _ \   | |\/| | / _ \ |  \| | / _ \| |  _|  _| | |_) |
 | |  | | |___  | |/ ___ \  | |  | |/ ___ \| |\  |/ ___ \ |_| | |___|  _ < 
 |_|  |_|_____| |_/_/   \_\ |_|  |_/_/   \_\_| \_/_/   \_\____|_____|_| \_\
"""

print(title)

def list_all_metadata(file_path):
    try:
        result = subprocess.run(['exiftool', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.stdout:
            print(f"{yellow}\n--- Metadata ---{red}")
            print(result.stdout)
        else:
            print(f"{red}[!] No metadata found.")
    except Exception as e:
        print(f"Error while opening the file: {e}")

def clear_all_metadata(file_path):
    try:
        result = subprocess.run(['exiftool', '-all=', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.stderr:
            print(f"{red}[!] Error during metadata removal: {result.stderr}")
        else:
            print(f"{green}[!] Metadata has been removed from the image {file_path}.")
    except Exception as e:
        print(f"{red}[!] Error while opening the file: {e}")

def main():
    while True:
        print(f"{red}\n--- Menu ---")
        print(f"1) List Metadata")
        print(f"2) Clear Metadata")
        print(f"3) Clear GUI")
        print(f"4) Exit")
        choice = input(f"Choose an option (1, 2, 3, 4): {yellow}")
        
        if choice == '1':
            file_path = input(f"{blu}Enter the path to the file: {yellow}").strip('"')
            list_all_metadata(file_path)
        elif choice == '2':
            file_path = input(f"{blu}Enter the path to the file: {yellow}").strip('"')
            clear_all_metadata(file_path)
        elif choice == '3':
            os.system("cls")
            print(title)
        elif choice == '4':
            print(f"{red}Program exit.")
            break
        else:
            print(f"{red}[!] Invalid choice. Please select 1, 2, 3 or 4.")

if __name__ == "__main__":
    main()
