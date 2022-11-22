def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i*n #string은 더할 수 있다는 특성을 활용
    return answer
