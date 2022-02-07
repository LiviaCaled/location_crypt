#!/usr/bin/env python3
import time
import crypt_lib
import gps

def print_main_menu():
    print("q: (or 0) Quit program")
    print("e: Encrypt current timestamp and given location")
    print("d: Decrypt hash")


if __name__ == "__main__":
    print("Location and timestamp encryption")

    while True:
        print_main_menu()
        choice = input("> ")
        if choice == "e":
            result = crypt_lib.encrypt(time.mktime(time.localtime()), gps.get_location()) 
            print("Location hash: %s" % result)
        if choice == "d":
            result = crypt_lib.decrypt()
        if choice in ("0", "q"):
            break
