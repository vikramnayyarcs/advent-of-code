f = open("input.txt", "r")
output = f.readlines()
f.close()

temp = [line[:-1] for line in output]

temp = [x.split() for x in temp]

print(temp)
