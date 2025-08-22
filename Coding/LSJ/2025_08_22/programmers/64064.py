def solution(user_id, banned_id):
    # answer = 0
    # ul = []
    # # user_id , banned_id , 둘이 같은지
    # for i in range(len(user_id)):
    #     for j in range(len(banned_id)):
    #         for k in range(len(user_id[i])):
    #             if banned_id[j][k] == '*':
    #                 continue
    #             else:
    #                 if user_id[i][k] == banned_id[j][k]:
    #                     if k == len(user_id[i][k])-1:
    #                         cnt += 1
    #                     continue
    #                 else:
    #                     break
    # return answer
    
    match = []
    
    for i in range(len(user_id)):
        for j in range(len(banned_id)):
            if len(user_id[i]) != len(banned_id[j]):
                continue
            
            is_match = True
            for k in range(len(user_id[i])):
                if banned_id[j][k] != '*' and user_id[i][k] != banned_id[j][k]:
                    is_match = False
                    break
            
            if is_match:
                match.append((i, j))
                
    def backtrack(banned_idx, used_users, current):
        if banned_idx == len(banned_id):
            combinations.add(tuple(sorted([user_id[user_idx]for user_idx in current])))
            return
        for user_idx, banned_match_idx in match:
            if banned_match_idx == banned_idx and user_idx not in used_users:
                used_users.add(user_idx)
                current.append(user_idx)
                backtrack(banned_idx + 1, used_users, current)
                current.pop()
                used_users.remove(user_idx)
    
    combinations = set()
    backtrack(0, set(), [])
    return len(combinations)