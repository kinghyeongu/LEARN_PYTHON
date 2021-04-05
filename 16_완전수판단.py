# 어떤 수가 자기 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다. 
# 예를 들어 6은 6=1+2+3 으로 완전수이다.
# n이 완전수인지 아닌지 판단해주는 프로그램을 작성하시오
# n이 완전수이면 "Perfect Number", 완전수가 아니면 "Not Perfect"를 리턴하시오.

def solution(n):
    sum=1
    for i in range(2,n//2+1):
        if n%i==0:
            sum+=i
    if n==sum:
        return 'Perfect Number'
    else:
        return 'Not Perfect'

print(solution(4964))