#최대공약수 구하기

def solution(a, b):
    if(b>a) : a,b = b,a

    while(b!=0):
        a=a%b
        a,b=b,a
    return a

print(solution(12,18))