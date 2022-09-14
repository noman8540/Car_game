import turtle
# car game 


print("This is the car game...")

command = {"What do you want to choice? start, stop, help, quit"}
started = False
while True:
    print(command)
    command_choice = input('>').lower()
    if command_choice == 'start':
        if started:
            print('car is already started!')
        else:
            started = True
            print('Car started.. Ready to go')
    elif command_choice == 'stop':
        if not started:
            print('car is already stopped!')
        else:
            started = False
            print('car stopped.')
    elif command_choice == 'help':
        print('''
            start - to start the car,
            stop - to stop the car,
            quit - to quit the game.
            ''')
    elif command_choice == 'quit':
        break
    else:
        print("sorry, I don't understand that!" )
