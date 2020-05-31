with open('C:\\Users\Diya Baban\Documents\VS CODE\Rosalind\X Working texts\\test.txt') as f:
    file = f.read()

wrk_file = file.split()
#print (wrk_file)
seq_1 = wrk_file[0]
seq_2 = wrk_file[1]

def hamming_distant(seq_1,seq_2):
    hamn_dist = 0
    for i in range(len(seq_1)):
        if seq_1 [i] != seq_2[i]:
            hamn_dist += 1
        else:
            hamn_dist += 0
    return hamn_dist

#calculating hamming distance
d = hamming_distant(seq_1,seq_2)

#writing to a file
f = open("C:\\Users\Diya Baban\Documents\VS CODE\Rosalind\X Working texts\\hamn_dist.txt",'w')
f.write(str(d))
f.close()
