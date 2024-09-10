data = [17,8,22,4,12,19,30,5,14,25]
left = [1,3,5,-1,-1,-1,9,-1,-1,-1]
right = [2,4,6,7,8,-1,-1,-1,-1,-1]

def BTS(to_seek,node,data,left,right):
    if node == -1:
        return False
    else:
        if to_seek == data[node]:
            return (True,node)
        else:
            if to_seek < data[node]:
                if left[node] != -1:
                    return BTS(to_seek,left[node],data,left,right)
                else:
                    return False
            if to_seek > data[node]:
                if right[node] != -1:
                    return BTS(to_seek,right[node],data,left,right)
                else:
                    return False




print(BTS(int(input("What would you like to search for")),0,data,left,right))

