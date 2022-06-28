'''
正则表达式
    使用re模块实现正则表达式操作

    定义
        正则表达式就是记录文本规则的代码
        可以查找操作符合某些复杂规则的字符串

    使用场景
        处理字符串
        处理日志

'''

'''
    python中使用正则表达式
        把正则表达式作为模式字符串
        正则表达式可以使用原生字符串来表示
        原生字符串需要在字符串前方加上 r’string‘
    
    #匹配字符串是否以Hogwarts_开头
    r'hgwart_\w+’
'''

'''
正则表达式对象转换
    compile（）：将字符串转换为正则表达式对象
    需要多次使用这个正则表达式的场景
    
    prog：正则表达式对象，可以直接调用匹配、替换、分割的方法，不需要再传入正则表达式
    pattern：正则表达式
    prog =re.compile(pattern)
'''
import  re
#匹配包装host的字符串
# pattern=r"host"
# prog =re.compile(pattern)

'''
匹配字符串
    match（）：从字符串的开始处理匹配
    search（）：在整个字符串中搜索第一个匹配的值
    findall（）在整个字符串中搜索所有符合正则表达式的字符串，返回列表
    
pattern:正则表达式
string：要匹配的字符串
flags:可选，控制匹配方式
    -A：只进行ASCII匹配
    -T：不区分大小写
    -H：将-和S用于包括整个字符串的开始和结尾的每一行
    -S：使用（.）字符匹配所有字符（包括换行符）
    -X：胡烈模式字符串中未转移的空格和注释
    
    re.match(pattern,string,[flags])
    re.search(pattern,string,[flags])
    re.findall(pattern,string,[flags])
'''
#匹配以hog开头的字符串
# pattern = r"hog\w+"
#
# s1 ="Hogwaer is a magic sch "
# match1=re.match(pattern,s1,re.I)
# print(match1)
# print(f"匹配值的起始位置为:{match1.start()}")
# print(f"匹配值的结束位置为:{match1.end()}")
# print(f"匹配位置的元组位置为:{match1.span()}")
# print(f"匹配位置的字符串位置为:{match1.span()}")
# print(f"匹配位置的数据为:{match1.group()}")
# match_list1=re.findall(pattern,s1,re.I)
# print(match_list1)
# s2="I like hogwa hogst"
# match2=re.match(pattern,s2,re.I)
# print(match2)
# match_list2=re.findall(pattern,s2,re.I)
# print(match_list2)

'''
替换字符串
    sub（）：实现字符串
    
    re.match(pattern,repl,string，[count],[flags])
    
    pattern:正则表达式
    repl：要替换的字符串
    string：要被查找替换的原始字符串
    count：可选，表示替换的最大次数，默认值为0，表示替换所有匹配
    flags：可选，控制匹配方式
'''
# pattern=r"1[34578]\d{9}"
# s1="中奖号码 123456，联系电话 15611111111"
# ree=re.sub(pattern,'11111111111',s1)
# print(ree)

'''
分割字符串
split（）：根据正则表达式分割字符串，返回列表
re.split(pattern,string，[maxsplit],[flags])
    pattern：正则表达式
    string：要匹配的字符串
    maxsplit：可选，表示最大拆分次数
    flags：可选，控制匹配方式
'''
p=r"[/|&]"
url="https://test-appranking.cd.xiaoxigroup.net/app/aso-keywords/1526845210/CN/as"

r=re.split(p,url)
print(r)