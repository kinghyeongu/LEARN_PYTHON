# 3개의 변의 길이를 입력하면, '예각삼각형', '직각삼각형', '둔각삼각형'을 출력
# 3개의 변으로 삼각형이 조건이 안되면, 직선 출력

def solution(a,b,c):
    tlist = [a,b,c]
    tlist.sort()

    if tlist[2]>=tlist[0]+tlist[1]:
        return '직선'
    elif pow(tlist[2],2) == pow(tlist[0],2) + pow(tlist[1],2):
        return '직각삼각형'
    elif pow(tlist[2],2) < pow(tlist[0],2) + pow(tlist[1],2):
        return '예각삼각형'
    elif pow(tlist[2],2) > pow(tlist[0],2) + pow(tlist[1],2):
        return '둔각삼각형'

print(solution(3,4,6))