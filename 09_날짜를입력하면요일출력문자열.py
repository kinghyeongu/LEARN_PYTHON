# ?‚ ì§œë?? ?…? ¥?•˜ë©? ?š”?¼?„ ì¶œë ¥?•˜?Š” ?”„ë¡œê·¸?¨?„ ?™„?„±?•˜?‹œ?˜¤.
# ?˜ˆë¥¼ë“¤?–´ "20190830"?„ ?…? ¥?•˜ë©? "fri"ë¥? ì¶œë ¥
# ?‚ ì§œí˜•?‹??? YYYYMMDD 8?ë¦¬ì˜ ë¬¸ì?—´?´ê³?, 
# ?š”?¼??? mon, tue, wed, thu, fri, sat, sun 3?ë¦¬ì˜ ë¬¸ì?—´?´?‹¤.

import datetime

def solution(inputday):
    days = ['mon','tue','wed','thu','fri','sat','sun']
    year = int(inputday[0:4])
    month = 0
    day = 0
    if inputday[4]=='0':
        month=int(inputday[5])
    else:
        month=int(inputday[4:6])
    
    if inputday[6]=='0':
        day=int(inputday[7])
    else:
        day=int(inputday[6:])

    return str(days[datetime.date(year,month,day).weekday()])

print(solution('20190901'))