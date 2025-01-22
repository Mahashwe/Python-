#interval : [1,3] [6,9] #this is given 
#new interval : [2,5] #to be added 
#op : [1,5][6,9]

def interval(user,new):
    final = []
    i = 0
    n = len(user)

    while i < n and user[i][1] < new[0]:
        final.append(user[i])
        i += 1
        # print("first:",final)

    while i < n and user[i][0] < new[1]:
        new[0] = min(new[0],user[i][0])
        new[1] = max(new[1],user[i][1])
        i+=1
        final.append(new)
    
    while i < n :
        final.append(user[i])
        i +=1

    # print(final)
    return final


a =  [[1,2],[3,5],[6,7],[8,10],[12,16]]
b = [4,8]
ans = interval(user=a,new=b)
print(ans)

