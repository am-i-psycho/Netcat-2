import time
import subprocess

def print_with_pause(text, pause=2):
    print(text)
    time.sleep(pause)

try:
    # Ask if the user wants to hack ARC
    answer = input("Do you want to hack ARC? (y/n): ").strip().lower()
    if answer == "y":
        # Print each line with a pause
        print_with_pause("Hacking ARC")
        print_with_pause("0% completed")
        for i in range(20, 100, 20):
            print_with_pause(f"{i}% completed")
        print_with_pause("93% completed")
        time.sleep(3)
        print_with_pause("96% completed")
        print_with_pause("99% completed")
        subprocess.run(["python", "challenge.py"])

    else:
        print("Ok Then, Bye....")

except KeyboardInterrupt:
    print("\nStopping Hacking.....")
    print("\nOk, Then bye....")
    