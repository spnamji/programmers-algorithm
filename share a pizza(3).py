def solution(slice, n):
    if (n / slice).is_integer() :
        return n // slice
    else :
        return n // slice + 1
