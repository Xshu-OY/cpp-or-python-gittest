def bubbleSort(nums:list[int])->list[int]:
    for i in range(len(nums)):
        for j in range(len(nums)-1-i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums



if __name__=="__main__":
    nums=[2,7,4,1,5,3,6]
    bubbleSort(nums)
    print(nums)


