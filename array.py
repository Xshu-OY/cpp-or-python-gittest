import random

def random_access(nums:list[int])->int:
    random_index=random.randint(0,len(nums)-1)
    return nums[random_index]

def insert(nums:list[int],num:int,index:int)->list[int]:
    for i in range(len(nums)-1,index,-1):
        nums[i]=nums[i-1]
    nums[index]=num
    return nums


if __name__=="__main__":
    nums=[2,7,4,1,5,3,6]
    print(random_access(nums))