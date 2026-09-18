import time 
 
def passwordCracker(password): 
 
    startTime = time.time() 

    #This is my character dictionary 
    Dictionary = [ 
        "a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", 
        "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", "l", "L", 
        "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", 
        "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", 
        "y", "Y", "z", "Z", 
 
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 
 
        "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", 
        "(", ")", "-", "_", "=", "+", "[", "{", "]", "}", 
        "\\", "|", ";", ":", "'", "\"", ",", "<", ".", ">", "/", "?" 
    ] 

    #This is a list which keeps track of the correct characters 
    letter = [] 
 
    pWord = password 

    #Checks if character in alphabet matches password character 
    for x in range(0, len(pWord)): 
        for y in range(0, len(Dictionary)): 

            if pWord[x] == Dictionary[y]: 
                letter.append(Dictionary[y]) 
                print(letter) 

            else: 
                print(letter) 

        #This prints the whole password 
        print(letter) 

        #This ends the time that was running when this started 
        endTime = time.time() 

        # subtracts end and start values to find the elapsed time 
        elapsedTime = endTime - startTime 

        #Prints the elapsed time 
        print("That took ", elapsedTime, "seconds") 
        print("The password is: ", password)

        if elapsedTime < 0.01:
            print("Password Secuirty: Weak")

        elif elapsedTime < 0.02 and elapsedTime < 0.03:
            print("Password Secuirty: Moderate")


        elif elapsedTime > 0.03:
            print("Password Secuirty: Strong")
 

while True:

    #Asks the user for a password
    password = input("Enter a password (or type q to quit): ")

    if password.lower() == "q":
        break

    passwordCracker(password)