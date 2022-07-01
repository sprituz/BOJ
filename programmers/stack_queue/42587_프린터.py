def solution(priorities, location):
    locations=[i for i in range(len(priorities))]
    prints=[]
    answer = 0
    while len(priorities)>0:
        if priorities[0]<max(priorities):
            priorities.append(priorities[0])
            del priorities[0]
            locations.append(locations[0])
            del locations[0]
        else:
            prints.append(locations[0])
            del priorities[0]
            del locations[0]
    return prints.index(location)+1