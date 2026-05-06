def solution(price, money, count):
    answer = 0
    sum = 0
    for i in range(1,count+1):
        sum += price*i
    if sum > money :
        answer = sum - money
        return answer
    else:
        return 0