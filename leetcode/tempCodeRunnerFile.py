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