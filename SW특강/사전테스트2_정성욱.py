'''
2023-04-21
정성욱
자판기 잔돈 계산 프로그램
투입한 돈에서 커피1잔(350)을 뺀 잔돈을 출력
#문제분석
    변수-money(투입한돈), chg(잔돈)
    수식-money-350, chg//1000, chg%1000, chg//500, chg%500, chg//100, chg%100, chg//50, chg%50 
#알고리즘 
    1.변수선언
        money(투입한돈) 정수로 입력
    2.알고리즘
        
'''

money=int(input("투입된 돈을 입력해주세요."))

coin=money-350
chg=money-350

w1000 = coin // 1000
coin = coin % 1000

w500 = coin // 500
coin = coin % 500

w100 = coin // 100
coin = coin % 100

w50 = coin // 50
coin = coin % 50

print("잔돈은 {} 원이며 1000원짜리는 {} 개 500원짜리는 {} 개 100원짜리는 {} 개 50원짜리는 {} 개 입니다.".format(chg,w1000,w500,w100,w50))