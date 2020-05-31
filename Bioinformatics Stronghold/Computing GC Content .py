with open("C:\\Users\Diya Baban\Downloads\\Test.txt") as f:
    file = f.read()
file_2 = file.rstrip()
file_1= file_2.split('>')
fn_res = open("C:\\Users\Diya Baban\Downloads\\output_result.txt",'w')
fn_res.write(str(file_1))

print(file_1)