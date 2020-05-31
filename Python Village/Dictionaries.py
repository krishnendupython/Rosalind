f = open('C:\\Users\Diya Baban\Downloads\\rosalind_ini6.txt','r')
fh = f.read()
lst = fh.split()
dic = {}
for i in lst:
    dic[i] = lst.count(i)

#print(dic) to check the dict structure
import pandas 

#from pandas import DataFrame or as below
df = pandas.DataFrame(list(dic.items()))

#creating dataframe without index and header
df_woindhd = df.to_string(index = False, header = False)

#creating new file to store the data 
fn = open('C:\\Users\Diya Baban\Downloads\\fresult.txt','w')
fn.write(str(df_woindhd))
fn.close()

#checking the created file
fo = open('C:\\Users\Diya Baban\Downloads\\fresult.txt','r')
new_file = fo.read()
print(new_file)