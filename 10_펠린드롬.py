# 알파벳 소문자로만 이루어진 단어가 주어진다. 
# 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.
# 팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다. 
# aaa, abcba는 팰린드롬이고, banaba, sex는 팰린드롬이 아니다.

def solution(word):
    list_word = list(word)
    for i in range(0, len(list_word) // 2):
    
        if list_word[i] == list_word[len(list_word) - 1 - i]:
            continue
        else:
            return "false"
    return "true"

print(solution('helleh'))