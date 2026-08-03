rows=5
for i in range(1,rows +1):
    print(" "* (2*(rows -i )),end='')
    row_nums=[]
    for j in range(i,2*i):
        row_nums.append(str(j))
    for j in range(2*i-2,i-1,-1):
        row_nums.append(str(j))
    print(" ".join(row_nums))