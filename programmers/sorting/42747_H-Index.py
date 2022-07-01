def quick_sort(citations):
    if len(citations)<=1:
        return citations
    pivot=citations[len(citations)//2]
    lesser,equal,greater=[],[],[]
    for citation in citations:
        if citation<pivot:
            lesser.append(citation)
        elif citation>pivot:
            greater.append(citation)
        else:
            equal.append(citation)
    return quick_sort(lesser)+equal+quick_sort(greater)
    
def solution(citations):
    sorted_array=quick_sort(citations)[::-1]
    for i in range(len(sorted_array)):
        if i>=sorted_array[i]:
            return i
    return len(sorted_array)