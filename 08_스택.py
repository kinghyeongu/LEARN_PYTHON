# 1. "PUSH+X"
# - 스택에 정수 X값을 넣습니다.
# 2. "POP"
# - 스택에서 가장 위에 있는 데이터를 꺼냅니다.
# - 만약 스택에 아무것도 있지 않다면, 명령을 무시합니다.
# 위의 명령들 모두 수행한 후에 큐스택 남아 있는 값들을 리턴하세요.
# cmds = ["PUSH+1","PUSH+2","PUSH+3","POP","POP","PUSH+4","POP","PUSH+5"]
# 리턴(정답): [1,5]

def solution(cmds):
    result = []
    for s in cmds:
        if s.split('+')[0] == "PUSH":
            result.append(int(s.split('+')[1]))
        if s=="POP":
            if len(result)!=0:
                del result[len(result)-1]
    return result

print(solution(["PUSH+1","PUSH+2","PUSH+3","POP","POP","PUSH+4","POP","PUSH+5"]))