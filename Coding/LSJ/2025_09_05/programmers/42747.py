
def solution(citations):
    citations.sort(reverse=True)
    h_index = 0
    
    for i in range(len(citations)):
        current_citation = citations[i]
        papers_count = i + 1
        
        if current_citation >= papers_count:
            h_index = papers_count
        else:
            break
    
    return h_index