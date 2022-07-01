def solution(operations):
    queue=[]
    for operation in operations:
        cmd,num = operation.split()
        if cmd=="I":
            queue.append(int(num))
        elif cmd=="D":
            if len(queue)>0:
                if num=="1":
                    queue.remove(max(queue))
                elif num=="-1":
                    queue.remove(min(queue))
    if len(queue)==0:
        return [0,0]
    else:
        return [max(queue),min(queue)]