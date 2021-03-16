#양의 정수가 들어 있는 arr 리스트에 9의 배수의 개수를 리턴하는 프로그램을 작성하시오.

def solution(arr):
    count=0
    for i in arr:
        if i%9==0:
            count+=1
    return count

print(solution([3,2,9,27,16,81]))