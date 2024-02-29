import random

random_number = random.randint(1, 100)

while True:
    a = int(input('숫자를 입력하세요:'))

    if a < random_number:
        print('up')
    elif a > random_number:
        print('down')
    else:
        print('정답')
        break
