# f = open("FILE IO\demo.txt", "r")

# f = open('FILE IO\order_details.csv','r')

# f = open('File IO\sample.txt','r')

# data = f.read()
# data = f.read(100) # 5 words read


# print(data)
# print(type(data))
# f.close()





with open(r'FILE IO\order_details.csv', 'r') as f:
    # data = f.read()
    # print(data)

    line1 = f.readline()
    print(line1)
    line10 = f.readline()
    print(line10)