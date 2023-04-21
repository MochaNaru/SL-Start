'''
2023-04-21
정성욱
놀이공원 입장료 계산 프로그램작성
#문제분석
    1.변수 - num1, num2, num3, total
    2.수식 - num1*5000, num2*10000, num3*7000, total*0.2
#알고리즘
    1.변수선언
        num1(어린이 요금),num2(보통 요금),num3(경로우대) 정수로 입력, tatal(총가격)
    2.논리(선택-if~else)
        if (num1+num2+num3) =< 10 :
            print total(총가격) * 0.2
        else :
            print num1+num2+num3=total
'''

num1=int(input("어린이 요금 인원수를 적어주세요.")) #변수1 지정
num2=int(input("보통 요금 인원수를 적어주세요.")) #변수2 지정
num3=int(input("노인우대 요금 인원수를 적어주세요.")) #변수3 지정

total=(num1*5000)+(num2*10000)+(num3*7000) #총 가격 계산식

if (num1+num2+num3) >= 10 : #할인이 되는 인원수인가?
    print("할인이 되는 가격이므로",total*0.8,"원 입니다.") #할인이 되는 인원수일때 출력
else :
    print("어린이인원이{} 이고 보통인원이{} 이며 경로우대가 {} 일때 가격은 {} 원이다".format(num1,num2,num3,total))
#할인이 되지않을때 출력 문    