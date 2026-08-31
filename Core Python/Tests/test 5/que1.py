D=[2000,500,200,100,50,20,10,5]
amount=int(input("enter the ammount :"))
count=0
for note in D:
    count=count+amount//note
    amount=amount % note
print(f"minimum number of notes is {count}")
