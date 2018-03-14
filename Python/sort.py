import os

def Bubble(list):
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                list[i],list[j] = list[j],list[i]
    return list

nums = [1,2,6,4,8,0,3,4]
print Bubble(nums)

