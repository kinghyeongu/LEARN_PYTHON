# 피보나치수는 첫째 및 둘째 항이 1이며, 그 뒤의 모든 항은 바로 앞 두 항의 합인 수열을 말한다.
# 처음 10개의 항은 다음과 같다.
# 1,1,2,3,5,8,13,21,34,55...

def solution(n):
    a, b = 1, 0
    for _ in range(n):
        a, b = b, a + b
    return b

print(solution(10))