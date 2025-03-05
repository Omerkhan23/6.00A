import os
# print(os.getcwd())
# file = open('test.txt','w')
# file.write('hello from first Example')
# file.close()



with open('data.txt','r') as school_data:
    record = school_data.read()
print(record)    