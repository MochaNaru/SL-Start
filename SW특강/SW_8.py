'''
2023-04-21
정성욱
태어난 년도를 입력받아 띠를 출력하는 프로그램 작성
다만 띠 순서는 원숭이, 닭, 개, 돼지, 쥐, 소, 범, 토끼, 용, 뱀, 말, 양띠 이다

#문제분석
    변수 - year(태어난년도), zodiac(년도를 %12 한 수)
    수식 - year%12, zodiac == 0 ~ 10
#알고리즘
    1.변수지정
    2.조건(if~else)
'''

year = int(input("태어난 년도를 입력하세요: "))
zodiac = year % 12

if zodiac == 0:
    print("원숭이띠입니다.")

elif zodiac == 1:
    print("닭띠입니다.")

elif zodiac == 2:
    print("개띠입니다.")

elif zodiac == 3:
    print("돼지띠입니다.")

elif zodiac == 4:
    print("쥐띠입니다.")

elif zodiac == 5:
    print("소띠입니다.")

elif zodiac == 6:
    print("범띠입니다.")

elif zodiac == 7:
    print("토끼띠입니다.") 

elif zodiac == 8:
    print("용띠입니다.")

elif zodiac == 9:
    print("뱀띠입니다.")

elif zodiac == 10:
    print("말띠입니다.")

else:
    print("양띠입니다.")