# 元类会自动将你通常传给‘type’的参数作为自己的参数传入
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''返回一个类对象，将属性都转为大写形式'''
    #  选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    for name, value in future_class_attr.items():
        print("name: %s,   value: %s" % (name, value))
    # 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
 
    # 通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)
 
 
class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        return super(UpperAttrMetaclass, cls).__new__(cls, name, bases, uppercase_attr)




class Foo(object):
    __metaclass__ = UpperAttrMetaclass  #  这会作用到这个模块中的所有类
    # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
    bar = 'bip'


print hasattr(Foo, 'bar')
# 输出: False
print hasattr(Foo, 'BAR')
# 输出:True
 
f = Foo()
print f.BAR
# 输出:'bip'