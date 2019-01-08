
LIMIT = 1_000_000
sequence_lengths = {'1' : 0}

def collatz(num):
    # print(sequence_lengths)
    count = 0
    temp = num
    while str(temp) not in sequence_lengths:
        if temp % 2 == 0:
            temp = int(temp / 2)
            count += 1
        else:
            temp = int((3 * temp + 1) / 2)
            count += 2
        
        if str(temp) in sequence_lengths:
            sequence_lengths[str(num)] = count + sequence_lengths[str(temp)]

for i in range(1,LIMIT):
    collatz(i)

print(max(sequence_lengths.keys(), key=(lambda key: sequence_lengths[key])))