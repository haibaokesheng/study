'''
@Author: your name
@Date: 2020-04-09 12:31:04
@LastEditTime: 2020-04-09 13:26:08
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python学习d:\project\python_code\刷题人生\leetcode\17_电话号码的字母组合.py
'''
class Solution:
    def letterCombinations(self, digits: str): #-> List[str]:
        letterMap = [' ','','abc','def','ghi',
        'jkl','mno','pqrs','tuv','wxyz']
        res = []
        if(len(digits))==0:
            return []
        def FindCombinations(digits,index,s):
            if index == len(digits):       
                return res.append(s)
            c = digits[index]
            letters = letterMap[int(c)]
            for i in letters:
                FindCombinations(digits,index+1,s+i)

        FindCombinations(digits,0,"")
        return res
a = Solution()
print(a.letterCombinations("23"))