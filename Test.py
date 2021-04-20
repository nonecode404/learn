#input('\n\n按下ente开始')
a, b, c, d = 1, 1.0, 'c', 3+2j
print(type(a), type(b), type(c), type(d))

print(isinstance(a, int))

str = 'testxuhan'
print(str[0:-1])
print(str[1:2])
print(str * 2)
print(str + ' a a')

print('xu\nhan')
print(r'xu\nhan')

list1 = ['a', 'b', 1, 2.1]
list2 = ['ccccc']
print(list1)
print(list1[2:])
print(list2*2)
print(list1 + list2)

letters = ['1', '2', '3', '4', '5', '6', '7', '8']
print(letters[1:6:2])

def reverseWords(input):

    inputWords = input.split(" ")
    print(inputWords)
    inputWords = inputWords[-1::-1]
    print(inputWords)
    output = ' '.join(inputWords)
    return output
if __name__ == "__main__":
    input = 'A large puma!'
    rw = reverseWords(input)
    print(rw)


tuple = ('a', 'b', 12.3, 14)
print(tuple[2:])


sites = {'xuhan', 'error', 'crash', 'communication', 'ask'}
print(sites)
if 'xuhan' in sites:
    print('He exits')
else :
    print('not exits')

a = set('abcdefgf')
b = set('ac')
print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

#######字典

dict = {}
dict['one'] = 1
dict[2] = 2
tinydict = {'name':'xuhan', 'years-old':'21', 'sex':'man'}
print(dict['one'])
print(dict[2])
print(tinydict.keys())
print(tinydict.values())


print('--------数字---------')
a = 1.0
print(int(a))
b = 5

print('---------字符串-------')

a = 'hello'
if 'h' in a :
    print('h 在变量a中')
else :
    print('不在')

if 'm' not in a :
    print('m 不在变量a中')
else :
    print('m 在变量a中')
print(r'\n')
print('\n')

#字符串格式化

print('我叫%s，今年%d岁。'%('徐晗', 21))
print('\n')

#三引号
paraStr = """这是
一个
可以
换行的
操作"""
print(paraStr)
print('\n')

#f-string
print(f'{1 + 1}')
w = {'name':'xuhan', 'yearold':'21'}
print(f'{w["name"]}----{w["yearold"]}')
print('\n')


print('-------列表---------')
#更新
list = ['0', '0', '0']
print("第2个元素是", list[1])
list[1] = 211
print("改变后的第二个元素为", list[1])
print('\n')

#删除
del list[0]
print(list[0])
print('\n')

print('------元组----------')
#访问
typ1 = (1, 2, 3, 'aa', 4)
print(typ1[0])
print(typ1[3])
#元组的值不允许修改
print(typ1)
del typ1
print('\n')

print('---------字典-------')
dict1 = {'name':'xuxu', 'age':'21', 'colleage':'conputer'}
print(dict1['name'])
dict1['name'] = "liulii"
print(dict1)
print('\n')

#删除
del dict1['name']
print(dict1)
dict1.clear()
print(dict1)
del dict1
print('\n')

print('-------')

print('---------集合---------')
basket = {1 ,2 ,3 , 4, 5}
print(1 in basket)
basket.add('xuxu')
print('xuxu' in basket)
basket.remove('xuxu')
print('xuxu' in basket)
print('\n')

print('------斐波那契数列-------')
a, b = 0, 1
while b < 10:
    print(b, end = ',')
    a, b = b, a+b

print('\n')
#右边的表达式是会先执行的

i = 256*256
print()

print('------For循环-------')
listFor = ["xu", "han", "ni", "hao", "ma"]
for x in listFor :
    if 'x' in x :
        print(x)
    else :
        print(x, end=',')
print('\n')

print('--------range函数-------')
for i in range(0, 20, 2) :
    print(i, end=',')
print('\n')

for i in range(len(listFor)) :
    print(i, listFor[i])
print('\n')


print('---------迭代器-----------')
listIt = [1, 2, 3, 4]
it = iter(listIt)
print(next(it))
print(next(it))
for x in it:
    print(x, end=' ')
print('\n')

import sys

listIt1 = [1, 2, 3, 4]
it1 = iter(listIt1)

# while True :
#     try :
#         print(next(it1))
#     except StopIteration:
#         sys.exit()

#创建一个迭代器类，学到构造函数之后再来学习

print('-----------生成器---------')

# def fibonacci(n) :
#     a, b, counter = 0, 1, 0
#     while True :
#         if(counter > n ) :
#             return
#         yield a
#         a, b = b, a+b
#         counter += 1
#
# f = fibonacci(10)
#
# while True :
#     try :
#         print(next(f), end=' ')
#     except StopIteration :
#         sys.exit()

print('''Python 
    strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
    不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
    可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
''')

print('------python传不可变对象实例----------')

def ChageInt(a) :
    print(a)
    a = 10
    print(a)

b = 2
ChageInt(b)
print(b)

print('\n------python传可变对象实例----------')
def changeList(myList) :
    myList.append([1, 2, 3])
    print('函数内：', myList)
    return

myList = [10, 20, 30]
changeList(myList)
print('函数外：',myList)

print('\n---------不定长参数-----------')
def printInfo1( arg, *vartuple ) :
    print("输出:")
    print(arg)
    print(vartuple)

printInfo1(1, 3, 4)

def printInfo2( arg, **vardict ) :
    print(arg)
    print(vardict)

printInfo2(1, a = 2, b = 3 )

print("\n----------lanmda表达式---------")
sum = lambda arg1, arg2 : arg1 + arg2
print(sum(10, 20))

print("\n-------数据结构----------")
stack = [1, 2, 3, 4, 5]
stack.append(7)
print(stack)
stack.pop()
print(stack)

from collections import deque
queue = deque(["xu", "han", "age", "sex"])
queue.append(18)
print(queue)
queue.popleft()
print(queue)
queue.pop()
print(queue)

print('---------列表推导式------')
print("----数据结构下周一解决-------")


print("-------输入和输出---------")
s = "Hello, World!"
del str
print(str(s))
print(repr(s))

for x in range(1, 11) :
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=" ")
    print(repr(x*x*x).rjust(4))

for x in range(1, 11) :
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print('-----format--------')
print('{}今年{}'.format("徐晗", 21))

print('------读取键盘----')
# str = input("请输入：");
# print ("你输入的内容是: ", str)

print('------读写文件------')
print('------pickle模块----')
print('''
实现了对一个 Python 对象结构的二进制序列化和反序列化。
 "pickling" 是将 Python 对象及其所拥有的层次结构转化为一个字节流的过程，
 而 "unpickling" 是相反的操作，
 会将（来自一个 binary file 或者 bytes-like object 的）字节流转化回一个对象层次结构。
''')

print("-----OS文件/目录方法------")
print("os 模块提供了非常丰富的方法用来处理文件和目录。")

print("-------错误和异常---------")

print("-----异常处理--------")
# while True :
#     try :
#         x = int(input("请输入一个数字："))
#         break
#     except ValueError :
#         print("您输入的不是数字，请再次尝试输入")

try :
    f = open('test.txt')
    s = f.readline()
    i = int(s.strip())

except OSError as err:
    print("OS error: {0}".format(err))
except ValueError :
    print("不能转换成一个整形")
except :
    print("未知错误：", sys.exc_info()[0])
    raise

for arg in sys.argv[1:] :
    try :
        f  = open(arg, 'r')

    except IOError :
        print('cannot open！')

    else :
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

try:
    print("\n")
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('这句话，无论异常是否发生都会执行。')

print("-------抛出异常-------")

# x = 10
# if x > 5 :
#     raise Exception('x 不能大于 5。x 的值为: {}'.format(x))

# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise

print('\n\n----------------------')
print('先不学，学完类再来')
print("断言")
print('----------------------\n\n')

print("------面向对象------")
print('''
类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
方法：类中定义的函数。
类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
局部变量：定义在方法中的变量，只作用于当前实例的类。
实例变量：在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
实例化：创建一个类的实例，类的具体对象。
对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。''')

class myClass :
    i = 12345
    def f(self):
        return 'hello world'

del x
x = myClass()

print('类的属性i为', x.i)
print('类的方法f为：', x.f())


print("-----构造方法-------")
class complex :
    def __init__(self, realPart, imagPart) :
        self.r = realPart
        self.i = imagPart

x = complex(3, 5)

print('\nself代表类的实例，而非类')
print(x.r, x.i)
class test :
    def ptr(self):
        print(self)
        print(self.__class__)

t = test()
t.ptr()

class people :
    name = ''
    age = 0
    __weight = 0

    def __init__(self,n , a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说我 %d 岁"%(self.name,self.age))
        print("{} 说我 {} 岁".format(self.name, self.age))

pp = people('xuhan', 21, 180)
pp.speak()


class student(people) :
    grade = ''

    def __init__(self,n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g

    def speak(self):
        print("%s 说我 %d 岁, 在读%s年级"%(self.name,self.age, self.grade))

st = student('xu', 21, 100, '大五')
st.speak()

print('------多继承--------')

class speaker() :
    topic = ''
    name = ''
    def __init__(self, t, n):
        self.topic = t
        self.name = n

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

class sample(student, speaker):
    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, t, n)

testSam = sample('xx', 21, 30, '4', '学习')
testSam.speak()  #方法名同，默认调用的是在括号中排前地父类的方法

print('\n-----方法重写-------')

class parent :
    def method(self):
        print('调用父方法')

class child(parent):
    def method(self):
        print('调用子方法')

c = child()
c.method()
super(child, c).method()

print('\n--------私有方法私有类---------')
class justCounter :
    __secretCount = 0
    publicCount = 0

    def count(self):
        self.__secretCount +=1
        self.publicCount += 1
        print(self.__secretCount)

jc = justCounter()
jc.count()
jc.count()
print(jc.publicCount)

#私有方法
class site :
    def __init__(self, name, url):
        self.name = name
        self.__url = url

    def who(self):
        print('name: ',self.name)
        print('url: ', self.__url)

    def __foo(self):
        print("私有方法")

    def foo(self):
        print("公共方法")

si = site('当虹','arcvedio.com')
si.who()
si.foo()

print("\n-------运算符重载------")
class vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'vector (%d, %d)'% (self.a, self.b)

    def __add__(self, other):
        return vector(self.a + other.a, self.b + other.b)

v1 = vector(1, 2)
v2 = vector(2, 3)
print(v1 + v2)


print('\n--------命名空间和作用域--------')
print('''
A namespace is a mapping from names to objects.Most namespaces are currently implemented as Python dictionaries。
命名空间(Namespace)是从名称到对象的映射，大部分的命名空间都是通过 Python 字典来实现的。
''')

print('''
内置名称（built-in names）， Python 语言内置的名称，比如函数名 abs、char 和异常名称 BaseException、Exception 等等。
全局名称（global names），模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
局部名称（local names），函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）
''')

print('\n-------作用域-------')

print('''
A scope is a textual region of a Python program where a namespace is directly accessible. 
"Directly accessible" here means that an unqualified reference to a name attempts to find the name in the namespace.
作用域就是一个 Python 程序可以直接访问命名空间的正文区域。
''')

print('''\n-----四种作用域------
L（Local）：最内层，包含局部变量，比如一个函数/方法内部。
E（Enclosing）：包含了非局部(non-local)也非全局(non-global)的变量。
                比如两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，那么对于 B 中的名称来说 A 中的作用域就为 nonlocal。
G（Global）：当前脚本的最外层，比如当前模块的全局变量。
B（Built-in）： 包含了内建的变量/关键字等。，最后被搜索
''')

print('\n--------全局变量和局部变量---------')
total = 0
def sum(arg1, arg2) :
    total = arg1 + arg2
    print("函数内是局部变量：", total)
    return total

sum( 10, 20)
print("全局变量total：{}".format(total))


print('----global和nonlocal关键字-------')
num = 1

def fun1() :
    global num
    print(num)
    num = 123
    print(num)

fun1()
print('')
num1 = 10
def outer() :
    num1 = 10
    def inner() :
        nonlocal num1
        print(num1)
        num1 = 1000
        print(num1)

    inner()
    print(num1)

outer()

print('-------正则表达式---------')

print('''
re.RegexObject 
re.compile() 返回 RegexObject 对象。
re.MatchObject 
group() 返回被 RE 匹配的字符串。
start() 返回匹配开始的位置 
end() 返回匹配结束的位置 
span() 返回一个元组包含匹配 (开始,结束) 的位置 
''')
import re
print(re.match('xh', 'xhxuhan').span())
print(re.match('com', 'xuhan.com'))
print('\n')

line = 'Cats are smarter than dogs!'
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

print('matchObj.group()：', matchObj.group())
print('matchObj.group(1)：', matchObj.group(1))
print('matchObj.group(2)：', matchObj.group(2))
print('matchObj.group(1, 2)：', matchObj.group(1, 2))

#search
print('--search--')
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)

print('searchObj.group()：', searchObj.group())
print('searchObj.group(1)：', searchObj.group(1))
print('searchObj.group(2)：',searchObj.group(2))
print('searchObj.group(1, 2)：', searchObj.group(1, 2))

print('''
re.match 只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，
函数返回 None，而 re.search 匹配整个字符串，直到找到一个匹配。
''')

# 检索和替换
print('\nre.sub(pattern, repl, string, count=0, flags=0)')

phone = '150-831-5786 # 这是羲和的电话号码'

numPhone = re.sub(r'#.*$', "", phone)
print('电话号码：', numPhone)

numPhone = re.sub(r'\D', "", phone)
print('电话号码：', numPhone)

#repl 参数是一个函数
def double(matched):
    value = int(matched.group('value'))
    return value*2

sValue = 'A3C9A5A2A3A4'

#print(re.sub('(?P<value>\d+)', double, sValue))

print('\n\n---compile 函数---')

pattern = re.compile(r'\d+')

m = pattern.match('one12twothree34four')
print(m)

m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
print( m )

print(m.group())
print(m.end())
print(m.start())
print(m.span())

print('\n\n---findall----')
result1 = re.findall(r'\d+', 'xu 123 han 555')
patternFind = re.compile(r'\d+')
result2 = patternFind.findall('xu 123 han 555')
result3 = patternFind.findall('xu 123 han 555', 0, 7)
print(result1)
print(result2)
print(result3)
print('\nre.finditer')
itre = re.finditer(r'\d+', 'xasda1as1da1s153')
for match in itre:
    print(match.group())

print('\n----split-------')
print(re.split('\W+', 'runoob, runoob, runoob.'))

print('\n----修饰符-----')
print('''
re.I 使匹配对大小写不敏感
re.L 做本地化识别（locale-aware）匹配
re.M 多行匹配，影响 ^ 和 $
re.S 使 . 匹配包括换行在内的所有字符
re.U 根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
''')

print('\n\n--------数据库----------')
# noinspection PyUnresolvedReferences
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root',
    database = 'xh'
)

# print(mydb)
#
# #创建数据库
mycusor = mydb.cursor()
mycusor.execute("SHOW DATABASES")

for mcr in mycusor:
    print(mcr)

#mycusor.execute("CREATE TABLE friends (name VARCHAR(255), url VARCHAR(255))")
print('\n---table----')
mycusor.execute("SHOW TABLES")

for mcr in mycusor:
    print(mcr)

print('\n---主键设置----')

#mycusor.execute("ALTER TABLE friends ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

print('\n---插入数据----')
sql = 'INSERT INTO friends (name, url) VALUES (%s, %s)'
valSql = ('xuhan', 'arcvedio.com')
mycusor.execute(sql, valSql)
mydb.commit()
print(mycusor.rowcount, "记录插入成功")
print('ID: ', mycusor.lastrowid)

print('\n----插入多条数据失败')
valSqlMul =  [('Google', 'https://www.google.com')]

#mycusor.execute(sql, valSqlMul)

# print('\n---查询数据----')
# mycusor.execute('select * from friends')
#
# myresult = mycusor.fetchall()
#
# for x in myresult:
#     print(x)
# mycusor.execute('select name from friends')
#
# myresult = mycusor.fetchall()
# for x in myresult:
#     print(x)
#
# mycusor.execute('select * from friends')
# print(mycusor.fetchone())

print('\n---where语句----')


# sqlWhere = "SELECT * FROM friends WHERE id = 1"
# mycusor.execute(sqlWhere)
#
# myresult = mycusor.fetchall()
#
# for x in myresult:
#     print(x)

# sql = "SELECT * FROM friends WHERE url LIKE '%oo%'"
#
# mycusor.execute(sql)
#
# myresult = mycusor.fetchall()
#
# for x in myresult:
#     print(x)

print('\n----防止sql注入----')

# sql = "SELECT * FROM friends WHERE name = %s"
# na = "xuhan"
# mycusor.execute(sql, na)
# myresult = mycusor.fetchall()
# for x in myresult:
#     print(x)

print('\n----排序-----')

# sql = "SELECT * FROM friends ORDER BY id DESC "
# mycusor.execute(sql)
#
# myresult = mycusor.fetchall()
# for x in myresult:
#     print(x)

print('\n----Limit\OFFSET---')

mycusor.execute('SELECT * FROM friends LIMIT 3 OFFSET 1') # 0 为 第一条，1 为第二条，以此类推

myresult = mycusor.fetchall()
for x in myresult:
    print(x)

print('\n----删除记录----')

# mycusor.execute('delete from friends where id = 1')
# mydb.commit()
# print(mycusor.rowcount,"条记录删除")
#防止注入参考上
# sql = "DELETE FROM friends WHERE id = %s"
# na = ("xu",)
#
# mycusor.execute(sql, na)
#
# mydb.commit()
#
# print(mycusor.rowcount, " 条记录删除")

print("\n-------更新表数据------")
# sql = "UPDATE friends SET name = %s WHERE id = 10"
# strSql = "hanhan"
# mycusor.execute(sql, strSql)
# mydb.commit()
# print(mycusor.rowcount, "记录修改")

print("\n-------删除表------")
mycusor.execute("drop table if exists sites")

print('\n\n-------------网络编程-------------------')
import socket

# severSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = socket.gethostname()
# port = 22222
# severSocket.bind((host, port))
# severSocket.listen(5)
# while True :
#     clientSocket,addr = severSocket.accept()
#     print("链接地址：%s"%str(addr))
#
#     msg = "welcom!" + '\r\n'
#     clientSocket.send(msg.encode("UTF-8"))
#     clientSocket.close()

print('\n--客户端---')
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # 获取本地主机名
# host = socket.gethostname()
#
# # 设置端口号
# port = 22222
#
# # 连接服务，指定主机和端口
# s.connect((host, port))
#
# # 接收小于 1024 字节的数据
# msg = s.recv(1024)
#
# s.close()
#
# print (msg.decode('utf-8'))

print('\n\n----------多线程----------')
print('----函数式启动线程----')
import _thread
import time

# def printTime(threadName, delay) :
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print("%s : %s" % (threadName, time.ctime(time.time())))
#
# try:
#     _thread.start_new_thread( printTime, ("Thread-1", 1,))
#     _thread.start_new_thread( printTime, ("Thread-2", 2,))
# except:
#     print('Error: 无法启动')


print('\n\n----用类来起线程----')
import threading
exitFlag = 0





class myThread(threading.Thread) :
    def __init__(self,threadId, threadNmae, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.threadName = threadNmae
        self.counter = counter
    def run(self):
        print("开始线程："+ self.threadName)
        printTime(self.threadName, self.counter, 5)
        print("退出线程："+ self.threadName)


def printTime(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()

        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1



thread1 = myThread(1, "Thread - 1", 1)
thread2 = myThread(2, "Thread - 2", 1)
thread1.start()
thread2.start()
thread1.join()
thread2.join()


print('''\n\n
start() 方法是启动一个子线程，线程名就是我们定义的name
run() 方法并不启动一个新线程，就是在主线程中调用了一个普通函数而已。''')

print('\n线程同步')
threadLock = threading.Lock()
threads = []

class myThread01(threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        threadLock.acquire()
        printTime(self.name, self.counter, 3)
        print("退出线程：" + self.name)
        threadLock.release()

thread3 = myThread01(3,"Thread-3", 1)
thread4 = myThread01(4,"Thread-4", 1)

thread3.start()
thread4.start()

threads.append(thread3)
threads.append(thread4)

for t in threads:
    t.join()


print('\n\n---线程优先级队列---')
