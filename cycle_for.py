from random import randint
# Формат цикла for
# for <переменная> in <обьект>:
#     <тело цикла>
# В переменную i сохраняем копию элемента
m = [45,46,32,12]
for i in m:
    print(i)
for i in range(4):
    a = randint(1,100)
    print(a,end=" ")
print()
print(i)