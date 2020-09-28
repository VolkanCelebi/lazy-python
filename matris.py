matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
mat_trans = []
trans = []
trans1 = []
trans2 = []
trans3 = []
for row in matrix:
    for i in range(4):
        if i == 0:
            trans.append(row[i])
        if i == 1:
            trans1.append(row[i])
        if i == 2:
            trans2.append(row[i])
        if i == 3:
            trans3.append(row[i])
mat_trans.append(trans)
mat_trans.append(trans1)
mat_trans.append(trans2)
mat_trans.append(trans3)
trans = []
print(mat_trans)
# sonuç: [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

#yerine
print([*zip(*matris)])