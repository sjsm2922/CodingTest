def solution(x):
    answer = True
    hap = 0
    y = x
    while x > 0 : 
        hap += x%10
        x = x // 10
    if y % hap == 0 :
        return answer
    else:
        answer = False
        return answer
