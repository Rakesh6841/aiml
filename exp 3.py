import csv
with open('exp3.csv') as f:
    csv_file=csv.reader(f)
    data=list(csv_file)
    print(data)
    
    sp=data[0][:-1]
    ge=[['?' for i in range(len(sp))] for i in range(len(sp))]
    
    print(sp)
    print(ge)
    
    count=1
    for i in data:
        if i[-1]=='Yes':
            for j in range(len(sp)):
                if i[j]!=sp[j]:
                    sp[j]='?'
                    ge[j][j] = "?"
                    
        elif i[-1]=='No':
            for j in range(len(sp)):
                if i[j]!=sp[j]:
                    ge[j][j]=sp[j]
                else:
                    ge[j][j]="?"
                    
        print('Step ',count)
        count+=1
        print(sp)
        print(ge)
        
    gh=[]
    for i in ge:
        for j in i:
            if j!='?':
                gh.append(i)
          
    print('final specific hyp',sp)
    print('final general hypothesis',gh)
    
    
