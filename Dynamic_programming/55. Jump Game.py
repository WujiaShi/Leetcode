class Solution:
    def canJump(self, nums):
        if not nums:
            return False
        #开始时机器人没有燃料，必须要到达第一个格子才可以拿到燃料
        fuel = 0
        for i in range(len(nums)):
            
            #说明燃料已经耗尽且没有到达终点
            if fuel < 0:
                return False
            
            #选择多的燃料可以走的更远
            if fuel <= nums[i]:
                fuel = nums[i]   
            
            #每走一个格子消耗一个燃料
            fuel -= 1
            
        return True