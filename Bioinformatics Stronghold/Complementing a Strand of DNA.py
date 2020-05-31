with open('C:\\Users\Diya Baban\Downloads\\rosalind_revc.txt') as f:
    file = f.read()

def reverse_complement (Fwd_seq):
    work_seq = Fwd_seq.lower()
    lst = []
    for nt in range(len(work_seq)):
        if work_seq [nt] == 'a':
            lst.append('t')
        elif work_seq [nt] == 't':
            lst.append('a')
        elif work_seq [nt] == 'g':
            lst.append('c')
        elif work_seq [nt] == 'c':
            lst.append('g') 
    lst_1 =''.join(map(str,lst))
    rev_seq = lst_1[::-1]
    return (rev_seq.upper())
    
rslt = reverse_complement(file)

nf = open('C:\\Users\Diya Baban\Downloads\\output_result.txt','w')
nf.write(rslt)
nf.close()



