import os

class VirtualDisk:
    def __init__(self, path, size):
        self.path = path
        self.size = size 
        self.fat_offset = 8 
        self.fat_size = self.size // 2  
        self.data_offset = self.fat_offset + self.fat_size * 2  

    def create(self):
        with open(self.path, 'wb') as disk:
            disk.seek(self.size - 1)
            disk.write(b'\0') 

    def read(self, offset, length):
        with open(self.path, 'rb') as disk:
            disk.seek(offset)
            return disk.read(length)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_ui():
    clear_screen()
    print("========== VRHD DISK CREATOR TOOL ==========\n")
    name = input("Enter Disk Name: ").strip()
    if not name:
        print("Error: Disk name cannot be empty.")
        return
    
    try:
        size_mb = int(input("Enter Disk Size (in MB): "))
    except ValueError:
        print("Error: Invalid size. Please enter a number.")
        return
    
    if size_mb > 64000:
        clear_screen()
        print("\nWARNING: Creating a disk larger than 64GB might take a long time.")
        print("Are you sure you want to continue?")
        print("1. Yes    2. No")
        choice = input("> ").strip()
        if choice != "1":
            return
    
    size_bytes = size_mb * 1024 * 1024
    disk = VirtualDisk(f"{name}.vrhd", size_bytes)
    print(f"\nCreating disk '{name}.vrhd' of size {size_mb} MB...")
    disk.create()
    print("Disk created successfully!")

def main_menu():
    while True:
        clear_screen()
        print("========== VRHD DISK CREATOR TOOL ==========\n")
        print("1. Create Disk")
        print("2. Exit\n")
        
        choice = input("> ").strip()
        if choice == "1":
            create_ui()
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
