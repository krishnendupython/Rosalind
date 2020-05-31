from Bio import  SeqIO
from Bio.SeqUtils import GC

identifiers = sorted(GC(seq) for seq in SeqIO.parse ('C:\\Users\Diya Baban\Documents\VS CODE\Rosalind\X Working texts\\test.fasta','fasta'))

    
file = open('C:\\Users\Diya Baban\Documents\VS CODE\Rosalind\X Working texts\\sequence.txt','w')
file.write(str(identifiers))
file.close()