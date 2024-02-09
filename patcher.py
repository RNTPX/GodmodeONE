import os
import shutil

def print_welcome_message():
    print("Welcome to GodmodeONE for Xbox One/Xbox One S & X/Xbox Series S & X")
    print("This is a custom firmware to allow your Xbox to load homebrew applications")
    print("NOTE: THIS DOES NOT ENABLE PIRACY! PIRACY IS ILLEGAL, AND HOMEBREW APPLICATIONS THAT ENABLE PIRACY WILL NOT WORK!")
def print_install_menu():
    print("To install GodmodeONE:\n")
    print("  X - Install GodmodeONE\n")
    print("  F - Exit Patcher\n")

def main():
    print_welcome_message()
    print_install_menu()

    while True:
        select = input("Please choose an option (X/F): ")

        if select.upper() == "X":
            install_godmode()
            break
        elif select.upper() == "F":
            print("Exiting Patcher. Goodbye!")
            break
        else:
            print("Invalid option. Please choose either 'X' or 'F'.")

def install_godmode():
    print("\nPlease enter the path of your USB device:")
    usb = input("> ")

    if os.path.isdir(usb):
        print("\nInstalling GodmodeONE...")

        firm_file = "gmo.firm"
        bin_file = "gmo.bin"
        config_file = "gmo.cfg"

        # Check if files exist
        if os.path.isfile(firm_file) and os.path.isfile(bin_file) and os.path.isfile(config_file):
            
            # Move the files to the USB device
            shutil.copy(firm_file, usb)
            shutil.copy(bin_file, usb)
            shutil.copy(config_file, usb)
            os.mkdir(os.path.join(usb, "apps"))

            print("\nGodmodeONE Files have been successfully copied to the USB device.")
            print("Remove your USB device and insert it into your Xbox One/Xbox One S & X.")
            input("Press Enter to exit...")
        else:
            print("MISSING FILES. Exiting installation.")
            input("Press Enter to exit...")
            exit()
    else:
        print("Invalid device path. Exiting installation.")

if __name__ == "__main__":
    main()
