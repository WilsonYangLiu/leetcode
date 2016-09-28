#! /usr/bin/env python 2.7
# -*- coding: UTF-8 -*-

def twoSum(sums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == target - nums[i]:
                print (i, j)
            


nums = [2, 7,7,7, 11, 15]
target = 18

twoSum(nums, target)
