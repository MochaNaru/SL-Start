'''
2023-04-21
정성욱
인치를 입력받아 센티미터로 변환하는 프로그램 작성
#문제분석
    변수 - 인치(inch)
    수식 - inch * 2.54
#알고리즘
    1.변수 지정 (실수로 지정)
    2.inch * 2.54 실행후 결과 출력
'''

inch=float(input("인치를 입력하세요: "))

print("인치가 {} 일때 센티미터는 {}cm 입니다".format(inch,inch*2.54))