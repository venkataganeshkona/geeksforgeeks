def removeDuplicates(nums):
    original_len=len(nums)
    initial_count = 0
    for i in range(0,len(nums)-1):
        j=i+1

        if(nums[i]==nums[j]):
            j=j+1
        else:
            nums[initial_count+1]=nums[j]
            initial_count+=1



    print nums[0:initial_count+1]


nums=[1,1,1,2,2,3,4,4,5,5,5,6,6,6,6]
removeDuplicates(nums)
