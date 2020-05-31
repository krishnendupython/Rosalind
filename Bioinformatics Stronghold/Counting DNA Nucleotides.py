with open("C:\\Users\Diya Baban\Downloads\\rosalind_ini.txt") as f:
    file = f.read()
def nt_counter(seq):
    file_lo = (seq.lower()).rstrip()
    dic_of_nt = {}
    for i in file_lo:
        dic_of_nt[i] = file_lo.count(i)

    #ordering dictionary alphabetically
    from collections import OrderedDict
    dic_of_nt_ordered = OrderedDict(sorted(dic_of_nt.items()))
    return(dic_of_nt_ordered)
    
rslt = nt_counter(file)    
#storing result in file
fn_res = open("C:\\Users\Diya Baban\Downloads\\output_result.txt",'w')
fn_res.write(str(rslt))
fn_res.close()
  