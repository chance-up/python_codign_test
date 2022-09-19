# 1. 값 할당은 아래와같이 다양한 자료형 저장가능
# person = ['james', 17, 175.3, True]
# a = []
# b = [1, 2, 3]
# c = ['Life', 'is', 'too', 'short']
# d = [1, 2, 'Life', 'is']
# e = [1, 2, ['Life', 'is']]

# 2. make empty list
# >>> a = []
# >>> a
# []
# >>> b = list()
# >>> b
# []

# 3. make list using range
# >>> c = list(range(-4, 10, 2))
# >>> c
# [-4, -2, 0, 2, 4, 6, 8]

# 4. 리스트접근
# list1 = [-4, -2, 0, 2, 4, 6, 8]
# list1[0]
# list1[-1] => 마지막요소

# 5. 자르기
# a = [1, 2, 3, 4, 5]
# a[0:2] => [1, 2]
# a[:2] => [1, 2]  #0번째 인덱스부터 2번째 인덱스까지 자름(자기자신포함 x)
# a[2:] => [3, 4, 5] #2번째 인덱스부터 끝까지 자름(자기자신포함 o)


# 6. 리스트 연산
# print([1, 2, 3] + [4, 5, 6])
# print([1, 2, 3] * 3)

# 7. 리스트 길이
# len(a)


## Method들
# list append
# a = [1, 2, 3]
# a.append(5)

# list insert
# a = [1, 2, 3]
# a.insert(1, 5)

# delete
# a = [1, 2, 3]
# del a[1]
# del a[2:]
# print(a)

# remove
# a = [1, 2, 3, 4, 5, 6, 7]
# a.remove(3)

# list sort/reverse
# a = [3, 2, 1] # ['a','b','c'] 도 정렬가능
# a.sort()
# a.sort(reverse=True)
# a.reverse()
# b = ['가', '가나', '가나다라', '가나다']
# b.sort(key=len)

# sorted (내장함수) 사용
# x = [1 ,11, 2, 3]
# y = sorted(x)
# y = sorted(x,reverse=True)
# y = sorted(x,reverse=True)

# countries = [
#   {'code': 'KR', 'name': 'Korea'},
#   {'code': 'CA', 'name': 'Canada'},
#   {'code': 'US', 'name': 'United States'},
#   {'code': 'GB', 'name': 'United Kingdom'},
#   {'code': 'CN', 'name': 'China'}
# ]
# sorted(countries, key=lambda country: country["code"])
# sorted(countries, key=lambda country: country["name"])

# import operator
# d = {'b': 400, 'f': 300, 'a': 200, 'd': 100, 'c': 500}
# g = sorted(d.items(), key=operator.itemgetter(1))
# h = sorted(d.items(), key=operator.itemgetter(1), reverse=True)

# index() 해당 요소가 포함되어있는지, 있다면 인덱스반환
# list1.index(-2)
# 요소가 없다면 is not in list 에러발생
# list1.index(-1)

# count() 매칭되는 요소가 몇개인지?
# a = [1, 5, 5, 3, 7, 0, 1, 2]
# a.count(5) => 2
# a.count(13) => 0

# 포함되어 있는지없는지?
# 35 in [1, 35,90,100] => True
# 11 in [1, 3, 5,10] => False
# 11 not in [1, 3, 5,10] =>True

