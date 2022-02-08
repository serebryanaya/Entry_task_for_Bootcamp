def Counter(list_cn, val, size):
 count = 0
 i = size - 1
 while list_cn[i] >= val and i >= 0:
     count += list_cn[i] // val
     i = i - 1
 return count

str = input()
N, M = map(int, str.split(" "))
list_cn = []

copy = N
while copy != 0:
 list_cn.append(input())
 copy = copy - 1

list_cn = list(map(int, list_cn))
list_cn.sort()
size = len(list_cn)

low = 0
high = list_cn[size - 1]

total = sum(list_cn)

if total < M:
  print('0')
  exit()

if N == 1:
  print(list_cn[0] // M)
  exit()

if M == 1:
 print(high)
 exit()

count = 0
if high != low and high != list_cn[0]:
    while high - low > 1:
        mid = (low + high) // 2
        count = Counter(list_cn, mid, size)
        if count < M:
            high = mid
        elif count == M:
            if mid == high:
                print(high)
                exit()
            elif mid == low:
                print(low)
                exit()
        if count >= M:
            low = mid

count = Counter(list_cn, high, size)
if (count >= M):
 print(high)
 exit()
elif low != 0:
 count = Counter(list_cn, low, size)
 if (count >= M):
     print(low)
     exit()
print('0')
exit()