
import random
while True:
    user = input('가위바위보를입력하세요:')

    li = ['바위', '가위', '보']
    computer = random.choice(li)
    print(li)
    if (user == '가위' and computer == '바위') or (user == '바위' and computer == '보') or (user == '보' and computer == '가위'):
        print('컴퓨터가 이겼습니다')
    elif (user == '바위' and computer == '가위') or (user == '보' and computer == '바위') or (user == '가위' and computer == '보'):
        print('유저가 이겼습니다')
    elif (user == '바위' and computer == '바위') or (user == '가위' and computer == '가위') or (user == '보' and computer == '보'):
        print('비겼습니다')
