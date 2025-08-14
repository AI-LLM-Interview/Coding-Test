from itertools import permutations

def solution(numbers):
    all_nums = set()
    
    # 전체 순열 숫자 만들기
    for i in range(1, len(numbers) + 1):
        for perm in permutations(numbers, i):
            num = int(''.join(perm))
            all_nums.add(num)
    
    # 소수 개수
    count = 0
    for num in all_nums:
        if is_prime(num):
            count += 1
    
    return count

def is_prime(n):
    # 2보다 작으면 소수 아님
    if n < 2:
        return False
    
    # 2부터 n-1까지 나누어보기
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 or n < 2:
            return False
    
    return True