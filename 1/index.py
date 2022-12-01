results = []
sums = []

f = open("input.txt", "r")
output = f.readlines()
f.close()

temp = [line[:-1] for line in output]

container = []

#Get each array.
for e in temp:
    if e == '':
        results.append(container)
        sums.append(sum(container))
        container = []
        continue
    else:
        container.append(int(e))

#print(max(sums)) #Get the highest sum of calories (part 1).

sums.sort(reverse=True)

# print(sum(sums[:3])) #Get the sum of the top 3 elfs's calories.
