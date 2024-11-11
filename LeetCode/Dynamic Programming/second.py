class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def dfs(curr_opened, need_closing, curr):
            if curr_opened == n and need_closing == 0 and len(curr) == 2*n:
                res.append(curr)
            if curr_opened < n:
                dfs(curr_opened + 1, need_closing+1, curr + "(")
            if need_closing > 0:
                dfs(curr_opened, need_closing-1, curr + ")")
            
        res = []
        dfs(0, 0, "")
        return res
