def solution(sides):
    sides.sort(reverse=True)#내림차순 정렬
    
    if sides[0] >= sides[1] + sides[2]:
        return 2
    else:
        return 1
