from collections import deque
def solution(cap, n, deliveries, pickups):
    answer = 0
    while not deliveries and not pickups:
        if deliveries:
            return answer