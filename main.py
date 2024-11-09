def hallo():
    print("Привет дорогой дневник!")
def first_Func(a):
    print("Меня завут",a)
def classMy():
    return "Я учусь в 1 классе"
def myFavoriteGame():
    return "Моей любимой игрой является "

name = "Николай"

hallo()
first_Func(name)

myClass = classMy()
isCorrect = False
print(myClass)

if myClass == "Я учусь в 1 классе":
    isCorrect = True
    print("Все верно, вы в первом классе")
else:
    isCorrect = False
    print("Неправильно, вы учитесь в первом классе")

myGame = myFavoriteGame() + "Rome 2"
print(myGame)
print(len(myGame))

count = 0
while count < len(myGame):
    print(myGame[count])
    count = count + 1

