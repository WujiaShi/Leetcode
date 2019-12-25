class Solution:
    def combinationSum2(self, candidates, target: int):
        if not candidates:
            return []
        res = []
        candidates.sort()
        self.dfs(candidates, 0, [], res, target)
        return res
        
    def dfs(self, candidates, start, path, res, target):
        if target == 0:
            res.append(path.copy())
            return 
            
        for idx in range(start, len(candidates)):
            if candidates[idx] > target:
                break
            if idx > start and candidates[idx] == candidates[idx - 1]:
                continue
            path.append(candidates[idx])
            self.dfs(candidates, idx + 1, path, res, target - candidates[idx])
            path.pop()