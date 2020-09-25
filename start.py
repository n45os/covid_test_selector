#!/usr/bin/env python3
# encoding: utf-8
import settings

print("You are about to make a Test List. Choose an option.")


def get_input():
    inputt = input(f"\nPress {settings.OKGREEN}enter{settings.ENDC}"
                   f" {settings.OKGREEN}to make a List.{settings.ENDC}\n"
                   f"Type:\n{settings.OKBLUE}s{settings.ENDC} to "
                   f"{settings.OKBLUE}change settings{settings.ENDC}\n"
                   f"{settings.FAIL}x {settings.ENDC}"
                   f"to{settings.FAIL} quit the application{settings.ENDC}\n"
                   f"then press{settings.OKGREEN} enter{settings.ENDC}\n")
    if inputt == '':
        from main import run
        if run() is False:
            while True:
                ans = input(f"You have already produced a list today, "
                            f"do you want to{settings.OKBLUE} make another list?{settings.ENDC}[y/n]\n")
                if ans == "y":
                    run(anyway=True)
                    import sys
                    sys.exit()
                elif ans == "n":
                    get_input()
                else:
                    print(f"{settings.WARNING}GIVE AN ANSWER.{settings.ENDC}")


    elif inputt == 's':
        settings.change_settings()
        get_input()
    elif inputt == "x":
        import sys
        print("run again to apply changes")
        sys.exit()
    else:
        print(f"\n{settings.WARNING}CHOOSE SOMETHING{settings.ENDC}")
        get_input()


get_input()
