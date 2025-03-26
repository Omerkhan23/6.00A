import os
# print(os.getcwd())
# current_loc = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(current_loc,'test.txt') #location where we want it to be stored otherwise
# #it would be stored in the current working directory

# file = open(file_path,'w')
# file.write('hello from second Example')
# file.close()
# print(f"File written at: {file_path}")

#two ways to read a file,either provide an absolute or relative path
# with open(r'others\data.txt', 'r') as school_data:
#     record = school_data.read()
# print(record)    


#or 
# Change the working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('data.txt', 'r') as school_data:
    record = school_data.read()
print(record)