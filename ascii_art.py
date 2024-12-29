import os
import time
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_delay(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def create_box_text(text):
    width = len(text) + 4
    box = [
        "+" + "-" * width + "+",
        "|  " + text + "  |",
        "+" + "-" * width + "+"
    ]
    return "\n".join(box)

def main():
    messages = [
        "PYTHON MAGIC",
        "FOLLOW ME",
        "@YourTikTok"
    ]

    # Main animation
    clear_screen()
    print_with_delay(" Watch this magic...")
    time.sleep(1)

    for message in messages:
        clear_screen()
        print("\n" * 2)
        print_with_delay(" " + "=" * 20 + " ")
        print("\n")
        print(create_box_text(message))
        print("\n")
        print_with_delay(" " + "=" * 20 + " ")
        time.sleep(2)

    # Final message
    clear_screen()
    print("\n" * 2)
    print_with_delay(" Follow for more Python magic! ")
    print_with_delay(" Don't forget to use trending sound! ")

if __name__ == "__main__":
    main()
