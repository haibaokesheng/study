'''
@Author: your name
@Date: 2020-04-08 12:45:49
@LastEditTime: 2020-04-08 13:49:11
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\剑指offer\13_机器人的运动范围.py
'''
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def sumofDigit(x,y):
            result = 0
            while x>0:
                result += x % 10
                x = x // 10
            while y>0:
                result += y % 10
                y = y//10
        return result

        def dfs(i,j):
            if i == m or j==n or sumofDigit(i,j)>k or (i,j) in visited:
                return
            visited.add((i,j))
            dfs(i+1,j)
            dfs(i,j+1)
        
        visited = set()     
        dfs(0,0)
        return len(visited)

        # BFS
        def check(a,b):
            def mysum(a):
                return sum(int(i) for i in str(a))
            if 0<=a<m and 0<=b<n and mysum(a)+mysum(b)<=k and (a,b) not in visited:
                cur.append((a,b))
            visited.add((a,b))
        ans = 0
        cur = [(0,0)]
        visited={(0,0)}
        while cur:
            x,y = cur.pop()
            ans +=1
            check(x+1,y)
            check(x-1,y)
            check(x,y+1)
            check(x,y-1)
        return ans