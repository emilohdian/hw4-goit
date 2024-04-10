import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def list_files(directory):
    try:
        for item in directory.iterdir():
            if item.is_dir():
                print(Fore.BLUE + f"📁 {item.name}")
                list_files(item)
            else:
                print(Fore.GREEN + f"<📄 {item.name}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py directory_path")
        sys.exit(1)

    directory_path = Path(sys.argv[1])
    if not directory_path.is_dir():
        print("Error: Invalid directory path.")
        sys.exit(1)

    list_files(directory_path)