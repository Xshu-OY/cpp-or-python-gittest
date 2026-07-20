def find(nums:list[int],target:int)->int:
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    return -1

def traverse(nums:list[int]):
    for i,j in enumerate(nums):
        print(i,j)
    

if __name__=="__main__":
    nums=[2,7,4,1,5,3,6]
    print(find(nums,5))
    traverse(nums)





