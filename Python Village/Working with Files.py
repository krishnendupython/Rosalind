f = open('C:\\Users\Diya Baban\Downloads\\rosalind_ini5.txt','r')
file = f.read()
lines = file.splitlines()
lst = []
f1 = open('C:\\Users\Diya Baban\Downloads\\result_file.txt', 'w')
for i in range(0, len(lines)):
    if i%2 != 0:
        f1.write(lines[i]+'\n')
f1.close()

fn = open('C:\\Users\Diya Baban\Downloads\\result_file.txt', 'r')
new_text = fn.read()
print(new_text)