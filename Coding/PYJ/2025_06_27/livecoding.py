from typing import List
from collections import deque

class Solution:
    def trap(self, height: List[int]) -> int:
        # 각 층마다 주변을 봤을 떄, 벽이 있으면 물을 담을 수 있다. 
        # 1. 1차원인 높이를 2차원 으로 변환
        # 2. 각 높이마다 0인 곳을 순회
        # 3. 양 옆에 벽으로 둘러싸인 공간을 만나면 물을 담을 수 있다고 확인하고 영역 확인 
        # 3 - 1. 벽으로 둘러싸인 공간이 아니라 물을 담을 수 없으면 0 으로 반환

        def move(direction, x):
            if direction == 'left':
                if x <= 0:
                    return 0
                return x - 1
            elif direction == 'right': 
                return x + 1
            return x

        def bfs(x: int) -> int:
            queue = deque(x)

            left = x - 1
            right = x + 1

            left_barrier = False
            right_barrier = False

            while queue:

                # 오른쪽 왼쪽 다르게 판단해야하는데 이것도 함수를 만드는게 더 편할 듯
                if right < len(barriers) and height[right] > 0:  # 오른쪽 벽이 있는지 확인
                    right_barrier = True

                if left >= 0 and height[left] > 0: # 왼쪽 벽이 있는지 확인
                    left_barrier = True

                left -= 1
                right += 1

                if left_barrier and right_barrier:  # 양 옆에 벽이 있는지 확인
                    return right - left - 1  # 물을 담을 수 있는 영역의 크기 반환
            return 0 # 없음 0

        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        barriers = height.copy()

        height.sort(reverse=True)
        max_height = height[0]

        water = 0

        # 1. 1차원인 높이를 2차원으로 변환하지말고 -1 하는 방식으로 하장
        for i in range(max_height):    # 최고 높이 만큼 반복
            # barriers = [h - 1 for h in barriers]  # 각 높이에서 1씩 낮추기
            # 2. 각 높이마다 0인 곳을 순회
            for j in range(len(barriers)):
                if barriers[j] <= 0:       # 비어있는 공간일 때,  # 3. 양 옆에 벽으로 둘러싸인 공간을 만나면 물을 담을 수 있다고 확인하고 영역 반환
                    water += bfs(j)

        return water 
    
# Example usage
if __name__ == "__main__":
    solution = Solution()
    result = solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print(result)  # Output: 6