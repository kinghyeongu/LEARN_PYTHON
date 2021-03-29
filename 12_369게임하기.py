# 3,6,9 게임은 3 또는 6 또는 9 가 들어가는 숫자는 제외하는 게임이다. 
# 3,6,9 게임의 숫자는 다음과 같은 수열이다.
# 1 2 4 5 7 8 10 11 12 14 15 17 18 20 21 22 24 25 27 28 40 .....
# 10까지의 3,6,9 게임수의 합
# 1+2+4+5+7+8+10 = 37

def solution(howlong):
    sum=0
    for i in range(1,howlong+1):
        count=0
        for j in str(i):
            if j=='3' or j=='6' or j=='9':
                count+=1
                break
        if count!=1:
            sum+=i
    return sum
print(solution(10))