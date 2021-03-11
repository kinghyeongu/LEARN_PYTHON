# 1부터 입력받은 수 n까지의 합을 출력하시오.

def solution(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum

print(solution(10))