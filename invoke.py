# coding: utf-8

'''
新的默认列表只在函数被定义的那一刻创建一次

当extendList被没有指定特定参数list调用时，这组list的值随后将被使用
这是因为带有默认参数的表达式在函数被定义的时候被计算，不是在调用的时候被计算
因此list1和list3是在同一个默认列表上进行操作(计算)的
而list2是在一个分离的列表上进行操作(计算)的(通过传递一个自有的空列表作为列表参数的数值)

下面这段代码可能能够产生想要的结果
def extendList(val, list=None):
    if list is None:
    list = []
    list.append(val)
    return list
'''

def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3

'''
result:
list1 = [10, 'a']
list2 = [123]
list3 = [10, 'a']
'''
