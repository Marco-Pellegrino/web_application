import os



val = os.getcwd()

print(val)


os.chdir("assets/Example_Files/Parallel Beams")
val = os.getcwd() 

print(val)

with open("README.md",'r') as f:
    lines = f.readlines()

print(lines)

# print(val)




# print(val)




# print(val)




# print(val)