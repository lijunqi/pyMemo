# coding: utf-8

'''
python��, ����Զ���. python�в�������ν�Ĵ�ֵ����, һ�д��ݵĶ��Ƕ��������, Ҳ������Ϊ�Ǵ�ַ
python��, �����Ϊ�ɱ�(mutable)�Ͳ��ɱ�(immutable)��������
Ԫ��(tuple), ��ֵ��(number), �ַ���(string)��Ϊ���ɱ����, ���ֵ���(dictionary)���б���(list)�Ķ����ǿɱ����
'''
a = 1 # a point to object '1'
a = 2 # ��a���ڴ���ֵΪ2���ڴ����һ��, �������޸�ԭ��a�󶨵��ڴ��е�ֵ, ��ʱ, �ڴ���ֵΪ1���ڴ��ַ���ü���-1, �����ü���Ϊ0ʱ, �ڴ��ַ������
b = a # b point to a
b = 3 # b point to a new object '3', a is still 2

a = [1,2,3]
b = a # b is [1,2,3]
b.remove(1) # a and b both are [2,3]
b = [4,5,6] # b point to new object [4,5,6], a is [2,3]

b = 256
id(b) == id(256) # True
c = 257
id(c) == id(257) # False


'''
1. ��Ƭ�����͹�������list��������ǳ������ֻ�ǿ���������Χ�Ķ������ڲ���Ԫ�ض�ֻ�ǿ�����һ�����ö��ѡ�
2. ����copy�е�deepcopy�������������Χ���ڲ�Ԫ�ض������˿������������������á�
3. �������֣��ַ���������ԭ�����Ͷ���ȣ�û�б�������˵������������������鿴id�Ļ�Ҳ��һ���ģ�����������¸�ֵ��Ҳֻ���´���һ�������滻���ɵĶ��ѡ�
'''
Tom = ['Tom', ['age', 10]]
Jack = Tom[:]
June = list(Tom)

'''
!!! copy !!!
>>> for x in Tom:
... print id(x)
... 
140704715293600 --> 'Tom'
140704715147816 --> ['age', 20]
>>> for x in Jack: 
... print id(x)
... 
140704715286256 --> 'Jack'
140704715147816 --> ['age', 20]
>>> for x in June:
... print id(x)
... 
140704715286352 -->'June'
140704715147816 -->['age', 20]


!!! Deep copy !!!
>>> import copy
>>> Tom = ['Tom', ['age', 10]]
>>> Jack = copy.deepcopy(Tom)
>>> June = copy.deepcopy(Tom)
'''

Jack[1][1] = 20
print Tom, Jack, June
