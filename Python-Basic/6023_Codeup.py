"""
시:분:초 형식으로 시간이 입력될 때 분만 출력해보자.

어떻게 분만 출력해야 할지 주의 깊게 생각해야한다.
"""
a,b,c = input().split(':')
print(b)



"""
해보고 싶어서 하는 것!
현재 시간을 받아서 분만 빼보기
"""
import time

from time import localtime, strftime
local = time.time()
# print(local)

tm = localtime(local)
print(strftime('%Y-%m-%d %I:%M:%S %p', tm))
print(tm[4])


