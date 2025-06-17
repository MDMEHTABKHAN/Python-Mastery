a = 20
print(a)
print(type(a))
print(id(a))

a = 21
print(a)
print(type(a))
print(id(a))


b = 10
print(id(b))
c = 10
print(id(c))

# only for immutable 
text = 'Hello'
print(id(text))
txt = 'Hello'
print(id(txt))


t = (1,2,3)
print(id(t))

s = (1,2,3)
print(id(s))

list = [1,2,3,4]
print(id(list))
list_1 = [1,2,3,4]
print(id(list_1))