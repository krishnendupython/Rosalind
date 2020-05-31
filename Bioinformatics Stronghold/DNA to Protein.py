with open('C:\\Users\Diya Baban\Documents\VS CODE\Rosalind\X Working texts\\test.txt') as f:
    file = f.read()
dna_seq = file.upper()

def dna_to_protein(dna_seq):
    def dna_to_rna (dna_seq):
        rna_seq = []
        for nt in dna_seq:
            if nt == 'T':
                rna_seq.append('U')
            else:
                rna_seq.append(nt)
        return((''.join(map(str,rna_seq))).upper())

    def translation(ds):
        pro_seq = []
        for i in range(0,len(ds),3):
            if ds [i:i+3] == 'UUU' or ds [i:i+3] == 'UUC':
                pro_seq.append('F')
            elif ds [i:i+3] == 'UUA' or ds [i:i+3] == 'UUG':
                pro_seq.append('L')
            elif ds [i:i+3] == 'UCU' or ds [i:i+3] == 'UCC' or ds [i:i+3] == 'UCA' or ds [i:i+3] == 'UCG'or ds [i:i+3] == 'AGU' or ds [i:i+3] == 'AGC':
                pro_seq.append('S')
            elif ds [i:i+3] == 'UAU' or ds [i:i+3] == 'UAC':
                pro_seq.append('Y')
            elif ds [i:i+3] == 'UGU' or ds [i:i+3] == 'UGC':
                pro_seq.append('C')
            elif ds [i:i+3] == 'UGG':
                pro_seq.append('W')
            elif ds [i:i+3] == 'CUU' or ds [i:i+3] == 'CUC' or ds [i:i+3] == 'CUA' or ds [i:i+3] == 'CUG':
                pro_seq.append('L')
            elif ds [i:i+3] == 'CCU' or ds [i:i+3] == 'CCC' or ds [i:i+3] == 'CCA' or ds [i:i+3] == 'CCG':
                pro_seq.append('P')
            elif ds [i:i+3] == 'CAU' or ds [i:i+3] == 'CAC':
                pro_seq.append('H')
            elif ds [i:i+3] == 'CAA' or ds [i:i+3] == 'CAG':
                pro_seq.append('Q')
            elif ds [i:i+3] == 'CGU' or ds [i:i+3] == 'CGC' or ds [i:i+3] == 'CGA'or ds [i:i+3] == 'CGG' or ds [i:i+3] == 'AGA' or ds [i:i+3] == 'AGG':
                pro_seq.append('R')
            elif ds [i:i+3] == 'AUU' or ds [i:i+3] == 'AUC' or ds [i:i+3] == 'AUA':
                pro_seq.append('I')
            elif ds [i:i+3] == 'AUG':
                pro_seq.append('M')
            elif ds [i:i+3] == 'ACU' or ds [i:i+3] == 'ACC' or ds [i:i+3] == 'ACA' or ds [i:i+3] == 'ACG':
                pro_seq.append('T')
            elif ds [i:i+3] == 'AAU' or ds [i:i+3] == 'AAC':
                pro_seq.append('N')
            elif ds [i:i+3] == 'AAA' or ds [i:i+3] == 'AAG':
                pro_seq.append('K')
            elif ds [i:i+3] == 'GUU' or ds [i:i+3] == 'GUC' or ds [i:i+3] == 'GUA' or ds [i:i+3] == 'GUG':
                pro_seq.append('V')
            elif ds [i:i+3] == 'GCU' or ds [i:i+3] == 'GCC' or ds [i:i+3] == 'GCA' or ds [i:i+3] == 'GCG':
                pro_seq.append('A')
            elif ds [i:i+3] == 'GAU' or ds [i:i+3] == 'GAC':
                pro_seq.append('D')
            elif ds [i:i+3] == 'GAA' or ds [i:i+3] == 'GAG':
                pro_seq.append('E')
            elif ds [i:i+3] == 'GGU' or ds [i:i+3] == 'GGC' or ds [i:i+3] == 'GGA' or ds [i:i+3] == 'GGG':
                pro_seq.append('G')
            else:
                break
        return (''.join(map(str, pro_seq)))
    rna_seq_f = dna_to_rna (dna_seq)
    return (translation(rna_seq_f))
  
protein_seq = dna_to_protein(dna_seq) 
nf = open('C:\\Users\Diya Baban\Documents\VS CODE\Rosalind\X Working texts\\test_output.txt', 'w')
nf.write(protein_seq)
nf.close()