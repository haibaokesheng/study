'''
@Author: your name
@Date: 2020-03-25 15:12:33
@LastEditTime: 2020-04-03 17:41:07
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\python学习\正则.py
'''
import re
msg = '大小我肚子龙泉撑不住擦我司麻烦'
pattern = re.compile('肚子')
result = pattern.match(msg) #没有匹配
print(result)
# 使用正则re模块的方法 match
re.match('肚子',msg) #只要从开头进行匹配，若不匹配则返回None

result = pattern.search(msg) #没有匹配
print(result.span())#返回位置
print(result.group())#使用group提取到匹配的内容

msg = 'daw1dawd15fe1ad15fa1fa'
result = re.search('[a-z][0-9][a-z]',msg) # search 只要有匹配的后面就不会检索
print(result.group())

result = re.findall('[a-z][0-9][a-z]',msg) #find all 匹配整个字符串
print(result)

# a7a a88a a4545a
msg = 'a7agsefa88adaa4545a'
result = re.findall('[a-z][0-9]+[a-z]',msg)
print(result)

#  qq号码 5~11位 开头不能是0
qq = '15154852'
re.match('^[1-9][0-9]{4}$',qq)#^行首 $行尾
