# mylist=["siyamak","diyama","saeed","ali","alireza"]
# for i in mylist:
#     if len(i) < 4:
#         print (i.upper())



    
        

        
x = int(input("enter ur number:\n"))
s = True
for ele in range(2,x):
    if x % ele == 0:
        s = False
        print("false")
        break
    else:
        print ("true")
