# x,y 좌표상에 3개의 점이 주어졌을때, 다른 한개의 점을 리턴

def solution(a,b,c):
    if a[0]==b[0]:
        x=c[0]
    elif a[0]==c[0]:
        x=b[0]
    else:
        x=a[0]
    if a[1]==b[1]:
        y=c[0]
    elif a[1]==c[1]:
        y=b[1]
    else:
        y=a[1]
    return x,y

print(solution((1,3),(1,7),(4,7)))
print(solution((3,2),(1,1),(1,2)))
print(solution((4,4),(1,1),(1,4)))