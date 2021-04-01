# "OOXXOXO"와 같은 OX퀴즈가 있다.
# 문제를 맞은 경우 그 문제의 점수는 연속된 O의 개수이다.
# "OOXXOXO"의 점수는 5(1+2+0+0+1+0+1)이 된다.
# 퀴즈 결과의 문자열이 주어졌을때, 점수를 구하는 프로그램을 작성하시오.

def solution(result):
    score=0
    count=0
    for i in result:
        if i=='O':
            count+=1
            score+=count
        elif i=='X':
            count=0
    return score

print(solution("OOOOOOOOOO"))