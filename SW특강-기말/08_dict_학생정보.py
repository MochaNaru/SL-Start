'''
학과 학번 이름 : 

학생 정보를 사전에 저장하고,
특정 학생의 정보(학번)를 입력하여 학생을 찾아주세요.

[알고리즘]
1. 학생 정보 저장 사전 만들기 - 빈 사전 만들기
2. 학생 정보 입력 - 사전에 저장 (z 키를 누르면 종료 - 무한반복)
3. 학번으로 검색하여 학생 찾기 (학번이 빈칸이면 검색 종료 - 무한반복)
'''

student = []

print('::학생 정보 입력::')
while True :
    idnum = input('학번 입력') 
    if idnum == 'z' :
        break
    
    naem = input('이름 입력 : ') #값
    student[idnum] = naem # 키 <= 값

print['입력 종료']
print(student)

print('학생 검색')
while True :
    idnum = input('찾고자 하는 학생의 학번을 입력 하세요 : ')
    if idnum == '' :
        break #검색 종료
    if idnum in student : #사전에 키가 있나요?
        print('<<검색결과>>')
        print('학번 : ', idnum, '이름 : ', student[idnum])
    else :
        print('찾고자 하는 학생이 없습니다.')
print('프로그램 종료')