# 입/출력
# integer와 string을 공백을 두고 입력받게해보자.
# a, b = input().split()
# print(a)
# print(b)
# print("a is %d , b is %s" % (a,b))
# print(1, 2, 3, sep='\n') => 아래와같이 출력
# 1
# 2
# 3
# print(1, end='')    
# print(2, end='')
# print(3) => 아래와 같이 출력
# 123
# i=1
# v=2
# print("index : {}, value: {}".format(i,v))
# print("key = {key}, value={value}".format(key=key,value=val))

# 연산자
# // : 나누고 나머자를 버리고 몫만 취함
# / : 나눔. 나머지없이 나누어떨어져도 결과값은 실수float형
# % : 나머지
# ** : 제곱
# @ : 행렬 곱셈


# 2진,8진,16진수 표현법
# 0b110 ==> 6
# 0o10 ==> 8
# 0xF ==> 15

# 변수 여러개 사용 및 값 바꾸기
# x, y = 10, 20
# x, y = y, x

# int로 변환 : int()
# str로 변환 : str()
# a = 10
# b = 20
# print(int(a))

# map : 배열 요소들 변환 (형변환에 주로 쓰이는 듯..)
# a = [1,2,3,4,5,6,7,8,9]
# b = map(int,a)
# for _b in b:
#     print(_b, type(_b))
# b = map(str,a)
# for _b in b:
#     print(_b, type(_b))

# boolean : True/False로 맨앞 대문자로
# 1 == 1.0 => True
# 1 is 1.0 => False
# 1 is not 1.0 => True
# 값이 있으면 무조건 True => bool(1),bool(1.5),bool('False')
# 없가나 빈 문자열이면 False => bool(0),bool(0.0),bool('')
# print(True and False) => False
# and, or를 쓴다. (&&,||)

# 객체 메모리주소 
# a = 1
# print(id(a))

# a=[]
# a={'':''}
# a={}
# a=()