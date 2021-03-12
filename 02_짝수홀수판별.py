#입력한 숫자가 짝수이면 '짝수' 출력, 홀수이면 '홀수' 출력

def solution(n):
    if n%2==0:
        return '짝수'
    else:
        return '홀수'

print(solution(8))