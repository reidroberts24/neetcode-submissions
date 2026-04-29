class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #two pointers
        #stack
        #deque

        q = deque()
        res = [0] * len(temperatures)

        for day in range(len(temperatures)):
            temp_today = temperatures[day]
            
            while q and (temp_today > q[0][0] or temp_today > q[-1][0]):
                if temp_today > q[0][0]:
                    prev_temp, prev_day = q.popleft()
                elif temp_today > q[-1][0]:
                    prev_temp, prev_day = q.pop()
                
                res[prev_day] = day - prev_day
            
            q.append((temp_today, day))
            
        

        return res