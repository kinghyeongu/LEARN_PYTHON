# 축구에서 승리하면 3점, 무승부는 1점, 패배는 0점의 승점을 얻는다.
# 승리는 Win의 W, 무승부는 Draw의 D, 패배는 Lose의 L로 표기한다고 할 때, 
# 만약 어느축구팀이 "WWWWW" 의 기록을 가지면 이 팀의 승점은 15점 이다.

def solution(result):
    sum=0
    for i in result:
        if(i=='W'):
            sum+=3
        elif(i=='D'):
            sum+=1
    return sum

n = input()
print(solution(n))