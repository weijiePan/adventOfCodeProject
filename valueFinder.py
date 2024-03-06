

    

def find_first_last_digit(fileName):
    with open(fileName, "r") as f:
        lines = f.readlines();
    values = []
    for i in lines:
        val1 = 0;
        val2 = 0;
        
        ind = 0;
        while i[ind].isdigit() == False:
            ind+=1
        val1 = i[ind]
        ind = len(i) - 1
        while i[ind].isdigit() == False:
            ind-=1
        val2 = i[ind]
        values.append(str(val1) + " " + str(val2))
    return values
def combine_values_in_a_list(l):
    x = []
    for i in l:
        twoVal = i.split(" ")
        twoVal[0] = int(twoVal[0])
        twoVal[0] *= 10
        twoVal[0] += int(twoVal[1])
        x.append(twoVal[0])
    return x

firstAndLastVal = find_first_last_digit("inputs.txt")
combined = combine_values_in_a_list(firstAndLastVal)
sum = 0
for i in combined:
    sum += i
print(sum)
