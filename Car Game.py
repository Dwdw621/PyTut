storage = ""

while True:
    UserInput = input(">").lower()
    if UserInput == "help":
        print(f"start - to start the cart \nstop - to stop the car \nquit - to exit")
    if UserInput != storage:
        if UserInput == "start":
            print("Car started... Ready to go!!!!!!!!")
        elif UserInput == "stop":
            print("Car stopped.")
        elif UserInput == "quit":
            break
        else:
            print("tf u just say?")
    else:
        print(f"You already {storage}!")
    storage = UserInput
