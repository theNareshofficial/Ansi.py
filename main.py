#!/usr/bin/env python3

import os
from ansi import *


def text_style():

    print(f"\n{BOLD}=-=-=-=-=-=- TEXT-STYLE =-==-=-==-=\n")

    print(f"{RESET}This is RESET")
    print(f"{ITALIC}This is ITALIC")
    print(f"{UNDERLINE}This is UNDERLINE")
    print(f"{BLINK}This is BLINK")
    print(f"{REVERSE}This is REVERSE")
    print(f"{HIDDEN}This is HIDDEN")
    print(f"{STRIKETHROUGH}This is STRIKETHROUGH")
    print(f"{DOUBLE_UNDERLINE}This is DOUBLE_UNDERLINE")
    print(f"{NORMAL_INTENSITY}This is NORMAL_INTENSITY")


def foreground_color():

    print(f"\n{BOLD}=-=-=-=-=-=- FOREGROUND COLOR =-==-=-==-=\n")

    print(f"{BLACK}This is BLACK")
    print(f"{RED}This is RED")
    print(f"{GREEN}This is GREEN")
    print(f"{YELLOW}This is YELLOW")
    print(f"{CYAN}This is CYAN")
    print(f"{WHITE}This is WHITE")
    print(f"{BRIGHT_BLACK}This is BRIGHT_BLACK")
    print(f"{BRIGHT_RED}This is BRIGHT_RED")
    print(f"{BRIGHT_YELLOW}This is BRIGHT_YELLOW")
    print(f"{BRIGHT_BLUE}This is BRIGHT_BLUE")
    print(f"{BRIGHT_MAGENTA}This is BRIGHT_MAGENTA")
    print(f"{BRIGHT_CYAN}This is BRIGHT_CYAN")
    print(f"{BRIGHT_WHITE}This is BRIGHT_WHITE")


def bg_color():

    print(f"\n{BOLD}=-=-=-=-=-=- BACKGROUND COLOR =-==-=-==-=\n")

    print(f"{BG_BLACK}This is BG_BLACK")
    print(f"{BG_RED}This is BG_RED")
    print(f"{BG_GREEN}This is BG_GREEN")
    print(f"{BG_YELLOW}This is BG_YELLOW")
    print(f"{BG_BLUE}This is BG_BLUE")
    print(f"{BG_WHITE}This is BG_WHITE")
    print(f"{BG_BRIGHT_RED}This is BG_BRIGHT_RED")
    print(f"{BG_BRIGHT_BLACK}This is BG_BRIGHT_BLACK")
    print(f"{BG_BRIGHT_GREEN}This is BG_BRIGHT_GREEN")
    print(f"{BG_BRIGHT_YELLOW}This is BG_BRIGHT_YELLOW")
    print(f"{BG_BRIGHT_BLUE}This is BG_BRIGHT_BLUE")
    print(f"{BG_BRIGHT_MAGENTA}This is BG_BRIGHT_MAGENTA")
    print(f"{BG_BRIGHT_WHITE}This is BG_BRIGHT_WHITE")


name = os.name

if name == "nt":
    os.system("cls")
else:
    os.system("clear")

print(f"""{GREEN}{ITALIC}

1.) Text Style
2.) Foreground color
3.) Background color

""")

while True:
    choice = int(input(f"\n{YELLOW}{BOLD}Enter Your Choice : "))

    try:
        if choice == 1:
            text_style()
        elif choice == 2:
            foreground_color()
        elif choice == 3:
            bg_color()
        else:
            print(f"{RED}oops Invalid input!!!")

    except ValueError:
        print("oops Invalid input!!!")
    except KeyboardInterrupt:
        pass
    except EOFError:
        print(f"{RED}oops Invalid input!!!")
