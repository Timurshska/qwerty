import random
def is_valid(num1):
    if num1.isdigit() == True and int(num1) > 0 and int(num1) < 100:
        return True
    else:
        return False
    pass


flag = 1
print('Добро пожаловать в числовую угадайку')
while flag == 1:
    print('Введите правую границу')
    ran = input()
    while not is_valid(str(ran)):
        print('некорректный ввод')
        ran = input()
    ran = int(ran)
    iters = 1
    num1 = random.randrange(1, ran)
    num = (input())
    while not is_valid(str(num)):
        print('некорректный ввод')
        num = input()
    num = int(num)
    while num != num1:
        iters += 1
        if num > num1:
            print('Слишком много, попробуйте еще раз')
        if num < num1:
            print('Слишком мало, попробуйте еще раз')
        num = (input())
        while is_valid(str(num)) != True:
            print('некорректный ввод')
            num = input()
        num = int(num)
    print('Вы угадали, поздравляем!')
    print (f'количество попыток {iters}')
    print('Еще одну? 0 - если нет')
    s = input()
    if s.isdigit():
        if int(s) == 0:
            flag = 0
