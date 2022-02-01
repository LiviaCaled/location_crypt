#!/usr/bin/env python3
import crypt_lib

def print_main_menu():
    print("q: (or 0) Quit program")
    print("e: Encrypt current timestamp and given location")
    print("d: Decrypt hash")

i
if __name__ == "__main__":
    print("Location and timestamp encryption")

    while True:
        print_main_menu()
        choice = input("> ")
        if choice == "e":
            encrypt()
        if choice == "d":
            decrypt()
        if choice in ("0", "q"):
            break
