'''
2023-04-21
정성욱
아이디와 패스워드를 입력 받아 로그인 인증 결과를 출력하는 프로그램을 작성
#문제분석
    변수-아이디(id), 패스워드(password)

#알고리즘
    1.변수지정
    2.논리-(if~else)
'''

id = input("아이디를 입력하세요: ")
password = input("패스워드를 입력하세요: ")

if id == "admin" and password == "pw1234" :
    print("로그인 성공")

elif id != "admin" and password != "pw1234" :
    print("아이디와 패스워드가 모두 틀렸습니다.")

elif id != "admin" :
    print("아이디가 틀렸습니다.")

else:
    print("패스워드가 틀렸습니다.")