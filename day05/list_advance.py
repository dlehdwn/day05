# list_advance

# 리스트 연산자
# + (int, str, list)
x = ['아메리카노', '카페라떼', '바닐라라떼']
y = ['조각케익', '카스테라', '쿠키']
p = x + y
print(p)



# 리스트 기능
# 1.리스트의 길이 기능 : len()
x = ['아메리카노', '카페라떼', '바닐라라떼']
print(len(x))

# 2.리스트 추가 : append()
x = ['아메리카노', '카페라떼', '바닐라라떼']
x.append('카푸치노')
print(x)

# 3.리스트 추가 [몇번째] : insert(몇번째, 무엇을)

# 4.제거 : remove()
x = ['아메리카노', '카페라떼', '바닐라라떼']
x.remove('아메리카노')
print(x)

# 5.리스트 해당 아이템 위치 찾기 : index()
x = ['아메리카노', '카페라떼', '바닐라라떼']
print(x.index('아메리카노'))

# 6.리스트에 해당 아이템 몇개 : count()
x = ['아메리카노', '카페라떼', '바닐라라떼']
print(x.count('아메리카노'))

# 7.리스트를 추가 : extend(리스트) + [같은역할]
n = ['쿠키','케이크']
x.extend(n)
print(x)

# 8.리스트 정렬 : sort() / sort(reverse=True)
x.sort()
print(x)
x.sort(reverse=True)
print(x)
