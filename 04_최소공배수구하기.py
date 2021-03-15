#최소공배수 구하기

def solution(a, b):
    c, d = a, b
    if(b>a) : a,b = b,a
    
    while(b!=0):
        a=a%b
        a,b=b,a
    return int((c*d)/a)

print(solution(12,18))