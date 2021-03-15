# 입력된 수가 3의배수이면 '3의배수', 
# 5의배수이면 '5의배수', 7의배수이면 '7의배수', 
# 3,5,7의 배수가 아니면 '배수없음'을 출력하는 프로그램을 작성하시오.

def solution(n):
    if n%3==0:
        return '3의배수'
    elif n%5==0:
        return '5의배수'
    elif n%7==0:
        return '7의배수'
    else:
        return '배수없음'

print(solution(13))