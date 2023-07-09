import time

def set_timer():
    while True:
        try:
            timer = int(input("Enter the timer duration in minutes: "))
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print("Your timer began at: " + current_time)            
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    return timer

def run_alarm(timer):
    while True:
        print("Alarm set for {} minutes.".format(timer))
        time.sleep(timer * 60)  # Convert minutes to seconds
        print("\n*** ALARM ***")

        choice = input("\nDo you want to change the timer? (Y/N): ")
        if choice.lower() == "y":
            timer = set_timer()
        else:
            break

if __name__ == "__main__":
    print("\nWelcome to the Alarm Program!\n")

    timer = set_timer()
    run_alarm(timer)
