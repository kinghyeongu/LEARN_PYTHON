# 1920 1080의 해상도는 16:9이다.
# 1920 1080을 입력하면 "16:9"를 리턴하시오

def solution(a, b):
    markA=a
    markB=b
    if(b>a) : a,b = b,a

    while(b!=0):
        a=a%b
        a,b=b,a
    return str(markA//a) + ":" + str(markB//a)

print(solution(1920,1080))