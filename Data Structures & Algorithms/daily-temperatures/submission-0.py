class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        q = []
        res = [0] * len(temperatures)
        
        i = 0
        while i < len(temperatures):
            cur_temp = temperatures[i]
            while q and cur_temp > q[-1][0]:
                last_temp, day = q.pop()
                res[day] = i - day
            q.append([cur_temp, i])
            i += 1
        return res