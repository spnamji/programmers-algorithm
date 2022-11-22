def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    length = len(completion)  # 끝까지 안돌고 끝난겨어 완주자는 무조건 1이 적게 나오니까~
    # participant에다가 -1도 가능

    for i in range(length):
        if (participant[i] != completion[i]):
            return participant[i]

    return participant[-1]

print(["marina", "josipa", "nikola", "vinko", "filipa"])
