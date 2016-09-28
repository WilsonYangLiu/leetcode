class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dicts = dict()
        for i in range(len(nums)):
            if dicts.has_key(nums[i]):
                if type(dicts[nums[i]]) == list:
                    lst = dicts[nums[i]]
                    lst.append(i)
                    dicts[nums[i]] = lst
                else:
                    lst = [dicts[nums[i]]]
                    lst.append(i)
                    dicts[nums[i]] = lst
            else:
                dicts[nums[i]] = i
        
        nums.sort()
        
        for ele in nums:
	        if ele > target/2:
		        break
	        tmp = target - ele
	        if tmp == ele:
	            if type(dicts[tmp]) == list:
	                return (dicts[tmp][0], dicts[tmp][1])
	            else:
	                break
	        if (dicts.has_key(tmp)):
	            if type(dicts[tmp]) == list:
	                if type(dicts[ele]) == list:
	                    return (dicts[ele][0], dicts[tmp][0])
	                else:
	                    return (dicts[ele], dicts[tmp][0])
	            else:
	                if type(dicts[ele]) == list:
	                    return (dicts[ele][0], dicts[tmp])
	                else:
	                    return (dicts[ele], dicts[tmp])