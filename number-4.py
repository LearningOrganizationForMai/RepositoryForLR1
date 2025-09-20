t=(1,2,3)
try:
    t[1]=100
except:
    print('кортеж нельзя изменять')

t1 = (4,5)
t2 = t+t1
print(t2)
print(t2.count(3))
print(t2.index(4))
print(t)