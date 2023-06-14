'''
숫자 추측 게임 만들기

[문제 분석]
사용자가 입력한 값과 컴퓨터가 생성한 랜덤 값(1~30)을 비교한다.
몇번 만에 맞혔는지 알려준다.

사용자에게 힌트를 준다. 
사용자가 입력한 값이 랜덤 값 보다 크면 숫자는 작다. 라고한다
사용자가 입력한 값이 랜덤 값 보다 작으면 숫자는 크다. 라고한다

사용자가 값을 입력하여 힌트를 받을 때 마다 count 를 1씩 증가

게임은 한번만한다.
게임은 0을 입력하면 종료한다.
게임은 사용자가 y를 입력하면 시작한다
'''

# 알고리즘
# 1. 게임시작 여부를 묻는다.
#       1) start == y 아래 코드를 실행
# 2. randum함수로 숫자(num1)를 1~30사이로 하나를 지정한다
# 3. while True 로 무한반복을 건다
#       1) 정수를 입력받는다
#       2) 입력받은 정수(num2) == num1일때 "축하드립니다." 를 출력하며 프로그램 종료
#              a. 몇번 만에 맞췄는지 표시
#              a. 프로그램 종료
#       3) 입력받은 정수(num2)가 num1 보다 작을때 "숫자는 더 크다" 를 출력
#              a. count + 1
#       4) 입력받은 정수(num2)가 num1 보다 클때 "숫자는 더 작다" 를 출력
#              a. count + 1
# omNum : 지정해주는 숫자
# guessNum : 입력하는 숫자

import random

playAgain = 'y'

start = input("게임을 시작하시겠습니까? ")
while playAgain =='y' :
    comNum = random.randint(1,30)

    count = 1
    while True :
        guessNum = int(input("추측한 숫자를 입력 해주세요 : "))
        
        if comNum == guessNum :
            print("{}번 만에 맞췄습니다.".format(count))
            break
        
        elif comNum > guessNum :
            print("입력된 숫자보다 더 큰 숫자입니다.")
            
        elif comNum < guessNum :
            print("입력된 숫자보다 더 작은 숫자입니다.")
        count += 1
        
    playAgain = input("게임을 다시 하실거면 y 를 입력해주세요. ")