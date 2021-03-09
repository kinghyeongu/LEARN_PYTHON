#?…? ¥?œ¼ë¡? ì£¼ì–´ì§? ?ˆ˜ nê¹Œì???˜ ?†Œ?ˆ˜(prime number)?˜ ?•©?„ ë¦¬í„´?•˜?‹œ?˜¤.

def prime(n):
    sum=0
    count=0
    for i in range(2,n+1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            sum+=i
    return sum

print(prime(10))
# 2+3+5+7