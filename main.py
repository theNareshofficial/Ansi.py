from ansi import *


def text_style():

    print(f"\n{BOLD}=-=-=-=-=-=- TEXT-STYLE =-==-=-==-=\n")

    print(f"{RESET}This is RESET")
    print(f"{ITALIC}This is ITALIC")
    print(f"{UNDERLINE}This is UNDERLINE")
    print(f"{BLINK}This is BLINK")
    print(f"{REVERSE}This is REVERSE")
    print(f"{HIDDEN}This is HIDDEN")


def foreground_color():

    print(f"\n{BOLD}=-=-=-=-=-=- FOREGROUND COLOR =-==-=-==-=\n")

    print(f"{BLACK}This is BLACK")
    print(f"{RED}This is RED")
    print(f"{GREEN}This is GREEN")
    print(f"{YELLOW}This is YELLOW")
    print(f"{CYAN}This is CYAN")
    print(f"{WHITE}This is WHITE")


def bg_color():

    print(f"\n{BOLD}=-=-=-=-=-=- BACKGROUND COLOR =-==-=-==-=\n")

    print(f"{BG_BLACK}This is BG_BLACK")
    print(f"{BG_RED}This is BG_RED")
    print(f"{BG_GREEN}This is BG_GREEN")
    print(f"{BG_YELLOW}This is BG_YELLOW")
    print(f"{BG_BLUE}This is BG_BLUE")
    print(f"{BG_WHITE}This is BG_WHITE")


print(f"""{GREEN}{ITALIC}

1.) Text Style
2.) Foreground color
3.) Background color

""")

choice = int(input(f"{YELLOW}{BOLD}Enter Your Choice : "))

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
    print(f"{RED}oops Invalid input!!!")
except EOFError:
    print(f"{RED}oops Invalid input!!!")
