f = open(r'C:\Users\robin\Downloads\rosalind_tree.txt', 'r')
str1 = ' '
mat = []
while (str1 != ''):
    str1 = f.readline().strip()
    mat.append(str1)
mat.remove('')
n = int(mat[0])
edge = n - len(mat)
print(edge)