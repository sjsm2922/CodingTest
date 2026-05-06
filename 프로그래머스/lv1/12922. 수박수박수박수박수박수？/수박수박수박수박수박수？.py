def solution(n):
    answer = ''
    if n % 2 == 0 :
        answer = "수박" * (n//2)
    elif n >1 and n%2 != 0 :
        answer = "수"
        answer += "박수" * (n//2)
    else:
        answer = "수"
    return answer