with open('C:\\Users\Diya Baban\Documents\VS CODE\Rosalind\X Working texts\\rosalind_prtm (1).txt') as f:
    file = f.read()

pro = file.upper()

def protein_mass(pro):
    pro_mass = 0
    for aa in range(len(pro)):
        if pro [aa] == 'A':
            pro_mass += 71.03711
        elif pro [aa] == 'C':
            pro_mass += 103.00919
        elif pro [aa] == 'D':
            pro_mass += 115.02694    
        elif pro [aa] == 'E':
            pro_mass += 129.04259
        elif pro [aa] == 'F':
            pro_mass += 147.06841
        elif pro [aa] == 'G':
            pro_mass += 57.02146
        elif pro [aa] == 'H':
            pro_mass += 137.05891
        elif pro [aa] == 'I':
            pro_mass += 113.08406
        elif pro [aa] == 'K':
            pro_mass += 128.09496
        elif pro [aa] == 'L':
            pro_mass += 113.08406
        elif pro [aa] == 'M':
            pro_mass += 131.04049
        elif pro [aa] == 'N':
            pro_mass += 114.04293
        elif pro [aa] == 'P':
            pro_mass += 97.05276
        elif pro [aa] == 'Q':
            pro_mass += 128.05858
        elif pro [aa] == 'R':
            pro_mass += 156.10111
        elif pro [aa] == 'S':
            pro_mass += 87.03203
        elif pro [aa] == 'T':
            pro_mass += 101.04768
        elif pro [aa] == 'V':
            pro_mass += 99.06841
        elif pro [aa] == 'W':
            pro_mass += 186.07931
        elif pro [aa] == 'Y':
            pro_mass += 163.06333
        else:
            exit
    return pro_mass

pro_mass = protein_mass(pro)
pro_mass_round = round(pro_mass,3)

nf = open('C:\\Users\Diya Baban\Documents\VS CODE\Rosalind\X Working texts\\test_output.txt', 'w')
nf.write(str(pro_mass_round))
nf.close()