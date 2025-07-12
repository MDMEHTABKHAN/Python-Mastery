lst = [10,20,30,40,50]
for i in lst:
    print(i)

for i in [1,2,3,4,5]:
    print(i) 

lst = [1,2,3,4,5, 'python', 'java', 'c', 'c++', 'HTML','CSS', 'JavaScript', 'SQL']

for i in lst:
    print(i)

t = (1,2,3, 3+4j, 'Python', 3.4)

for j in t:
    print(j)
for j in (1,2,3, 3+4j, 'Python', 3.4):
    print(j)    

set = {1,2,34,56}

for k in set:
    print(k)

dic = {
   'name': 'mehtab',
   'age': 23,
   'isStudent': False
}    

for d in dic:
    print(d)
for key, value in dic.items():
    print(f"{key}: {value}") 


for i in range(6):
    print('Python')
          


l = [10,20,30,40,50,60,70,80,90,100]

for i in l:
    if i == 30:
        # continue
        # break
        pass
    print(i)
