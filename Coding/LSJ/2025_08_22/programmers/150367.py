def solution(numbers):
    return [1 if can_make_tree(num) else 0 for num in numbers]

def can_make_tree(num):
    binary = bin(num)[2:]  # 0b 제거
    
    # 포화 이진트리 크기 찾기
    length = 1
    while length < len(binary):
        length = length * 2 + 1
    
    # 앞에 0 패딩
    tree = binary.zfill(length)
    
    def check(start, end):
        if start > end:
            return True
        
        mid = (start + end) // 2
        
        # 루트가 0이면 전체가 0이어야 함
        if tree[mid] == '0':
            return all(tree[i] == '0' for i in range(start, end + 1))
        
        # 루트가 1이면 좌우 서브트리 검사
        return check(start, mid - 1) and check(mid + 1, end)
    
    return check(0, length - 1)