class Solution:
    def combinationSum(self, candidates, target: int):
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
            residual = target - candidates[idx]
            if residual < 0:
                break
            path.append(candidates[idx])
            self.dfs(candidates, idx, path, res, residual)
            path.pop()