def solution(n):
    a = int(n **(1/2))
    if a * a == n:
        answer = (a+1) ** 2 
    else :
        answer = -1
    return answer