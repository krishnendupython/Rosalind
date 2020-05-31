f = open("C:\\Users\Diya Baban\Downloads\\rosalind_dna.txt",'r')
def nt_counter(x):
    file = x.read()
    file_lo = (file.lower()).rstrip()
    dic_of_nt = {}
    for i in file_lo:
        dic_of_nt[i] = file_lo.count(i)

    #ordering dictionary alphabetically
    from collections import OrderedDict
    dic_of_nt_ordered = OrderedDict(sorted(dic_of_nt.items()))

    #check the output befor writing in file 
    print(dic_of_nt_ordered)
    print(list(dic_of_nt_ordered.values()))

    #storing result in file
    fn_res = open("C:\\Users\Diya Baban\Downloads\\output_result.txt",'w')
    fn_res.write(str(list(dic_of_nt_ordered.values())))
    fn_res.close()
    return fn_res

print(nt_counter(f))
