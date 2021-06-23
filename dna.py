import csv
import sys

# Prompt user for command line arguments
if len(sys.argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)

# Copy personal data to memory in form of a persons matrix
file = open(sys.argv[1], 'r')
read_data = csv.reader(file)
data = list(read_data)

# Copy dna sequence to memory
read_seq = open(sys.argv[2], 'r')
seq = read_seq.read()
read_seq.close()

# Check first STR sequence
STR_count = len(data[0])-1
counter = [0, 0, 0, 0, 0, 0, 0, 0]
STR_lenght = 0
STR_max_lenght = 0
skips = 0

# Evaluate lenght of the STR sequences
for h in range(0, STR_count):
    STR = data[0][h+1]
    for i in range(len(seq)):
        if skips != 0:
            skips -= 1
            continue
        if seq[i] == STR[0]:
            if seq[i:i+len(STR)] == STR:
                j = len(STR)
                STR_lenght += 1
                while seq[i+j: i+j + len(STR)] == STR:
                    STR_lenght += 1
                    j += len(STR)
                skips = j - 1
                if STR_lenght > STR_max_lenght:
                    STR_max_lenght = STR_lenght
                STR_lenght = 0

    # Make list out of longest STR sequences
    counter[h] = STR_max_lenght
    STR_max_lenght = 0

# Compare the DNA STR list with the persons matrix
for i in range(1, (len(data))):
    for j in range(1, (len(data[0]))):
        if int(data[i][j]) == counter[j-1]:
            if j == (len(data[0])-1):
                print(data[i][0])
                exit()
        else:
            break
print("No match")
exit()
