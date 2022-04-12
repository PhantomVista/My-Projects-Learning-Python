command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started")
        else:
            started = True
            print("Car Started...")
    elif command == "stop":
        if not started:
            print("Car already Stopped")
        else:
            started = False
            print("Car Stopped...")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit""")
    elif command == "quit":
        print("Thanks for Playing, bye")
        break
    else:
        print("I don't understand")

"""
command = ""
started = False
while True:
    command = input("> ").lower
    if command == "start"
        if started:
            print("car already started")
            else:
            started = True
            print("Car Started)
    elif command == "stop"
        if not started"
            print("car already stopped")
            else:
            started = False
            print("Car Stopped")
    elif command == "help"
        print(""start - to start the car
                stop - to stop the car
                quit - to end game"")
    elif command == "quit"
        print("Thanks for playing")
        break
    else:
        print("I don't understand")
    
"""


