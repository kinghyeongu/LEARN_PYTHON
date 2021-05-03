# 수학시험에서 사쿠라는 73점, 히토미는 37점을 맞았다.
# 히토미는 "쿠라야 너의 점수를 거꾸로 하니까 내 점수가 되네"
# 옆에 지나가는 나코가... "너희 둘 점수는 공통점이 거의 없는 서로소(공약수가 1)인걸 보니까 악연이군"
# 10점부터 99점 사이에 수중에서 점수를 거꾸로 할 때, 서로소가 되는 수를 모두 출력하시오.

def solution():
    for score in range(10,100):
        mark = score
        re = (score%10)*10 + score//10
        if(re>score) : score,re = re,score

        while(re!=0):
            score=score%re
            score,re=re,score
        if score==1:
            print(mark,end=' ')
solution()