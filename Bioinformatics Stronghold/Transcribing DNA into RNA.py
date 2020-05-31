with open('C:\\Users\Diya Baban\Documents\VS CODE\Rosalind\X Working texts\\test.txt') as f:
    file = f.read()
dna_seq = file.lower()
def dna_to_rna (dna_seq):
    rna_seq = []
    for nt in dna_seq:
        if nt == 't':
            rna_seq.append('u')
        else:
            rna_seq.append(nt)
    return((''.join(map(str,rna_seq))).upper())

rna_seq_f = dna_to_rna (dna_seq)
nf = open('C:\\Users\Diya Baban\Documents\VS CODE\Rosalind\X Working texts\\test_output.txt', 'w')
new_file = nf.write(str(rna_seq_f))
nf.close()