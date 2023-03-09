from random import randint


def alkoholtest():
    ans = False
    num1 = randint(0,100)
    num2 = randint(0,100)
    result = num1 + num2

    response = int(input(f"Was ergibt {num1} + {num2} = ?   "))
    if response == result:
        ans == True
        print("Richtig! Stark! :D")
    return ans

def drive_home_alone():
    print("Ok, du kannst nach Hause fahren!!!")

age = int(input("Wurstlänge?    "))
if age > 17:
    license = input("Hast du einen Führerschein? (y|n)  ")
    if license == 'y':
        alc = input("Hast du Alkohol getrunken? (y|n)   ")
        if alc == 'y':
            bestanden = True
            i = 0
            while bestanden == True and i<3:
                if alkoholtest() == False:
                    bestanden = False
                i += 1
            if bestanden == True:
                drive_home_alone()
            else:
                print("Bitte ruf deine Eltern an!   ")
        else:
            drive_home_alone()
    else:
        print("Bitte ruf deine Eltern an!   ")
else:
    print("Bitte ruf deine Eltern an!   ")
