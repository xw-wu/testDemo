'''
IO操作(流的输入和输出)
    输入流 InputStream:从磁盘、网络流进内存的操作
    输出流 OutputStream从内存流出道磁盘、网络
'''
'''
文件操作步骤
    打开文件
    操作文件：读写内容
    关闭文件：读写完成要及时的关闭
'''

'''
open 方法
def open（file,mode=‘r’，buffering=None，encoding=None，errors=None，newlinr=None，closefd=True）:
    file 必填
    mode 必填 打开方式，打开权限
    encoding 必填 中文需要设置编码，解决乱码问题
    buffering 缓冲区
    errors 出现编码错误的时候是忽略还是抛出来
'''
'''
文件读写模式
    f,以只读模式打开文件，并将文件指针指向文件头；如果文件不存在会报错
    w，以只写模式打开文件，并将文件指针指向文件头；如果文件存在则将其内容清空，如果文件不存在则创建
    a,以只追加可写模式打开文件，并将文件指针指向文件尾部，如果文件不存在则创建
    r+，在r的基础上增加了可写功能
    w+，在w的基础上增加了可读功能
    a+，在a的基础上增加了可读功能
    b，读写二进制文件（默认是t，表示文本），需要与上面集中模式搭配使用，如ab，wb，ab，ab+（posix系统，包括Liunx都会忽略该字符）
'''
'''
读操作
    read（）：一次读取文件所有内容，返回一个str
    read（size）：每次最多读取指定长度的内容，返回一个str：在python2中size指定的是字节长度，在python3中指定的是字符长度
    readlines（）：一次读取文件所有内容，按行返回一个list
    readline（）：每次只读取一行内容
'''

'''
    实战1
'''
#第一步：以只读模式打开文件
f=open('data.txt','r',encoding='utf-8')
#第二部：读取文件内容
#换行会占一个字符
# print(f.read(15))
# #read（）光标显示在最后一位，那么对应的第二次读取的时候从光标位置读取，没有读取任何内容
# result1=f.read()
# print(type(result1))
# print(result1)
# #读完一次之后，再次读取文件，内容将是不完整的，需要重新设置游标位置
# #设置游标位置
# f.seek(0)
# result=f.readline()
# print(type(result))
# print(result)
# #第三部：关闭文件
# f.close()

'''
忘记关闭文件的危害
    打开文件达到一定数量，将会导致打开失败
    占用内存控件，非常浪费资源
    会导致系统自动回收资源，丢失数据
'''
'''
with 用法：执行完操作之后直接关闭文件，执行close操作
with open('data.txt','r',encoding='utf-8') as f:
    print(f.read())
print(f.closed)#查看关闭状态
'''
# with open('data.txt','r',encoding='utf-8') as f:
#     print(f.read())
# print(f.closed)#查看关闭状态

'''
写操作实战
    mode="w+",读写权限，会新建文件，清空内容再写入
    mode=“r+”,读写权限，替换原来的内容
    mode="a+",读写权限，追加内容
'''
with open('data.txt','a+',encoding='utf-8') as f:
    print(f.write('gpython de 1232 fer'))

'''
总结
    使用with方法，会自动完成关闭操作
    通过python封装的API，可以实现读写追加操作
    文件打开要使用utf-8的编码格式（以免出现中文乱码）
'''