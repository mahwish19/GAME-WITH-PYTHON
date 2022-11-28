col_1=['A','E','I','M','Q','U','Y']
col_2=['B','F','J','N','R','V','Z']
col_3=['C','G','K','O','S','W',' ']
col_4=['D','H','L','P','T','X',' ']
print('\n')
print('Think only any three letter word')
print('col_no1    col_no2    col_no3    col_no4')
for x in range(7):
    print(col_1[x],'        ',col_2[x],'        ',col_3[x],'        ',col_4[x])


print('What is the length of your word')
o=int(input())
print('Enter the column number of each letter. Press enter after each column number')
y=0
my_list=[]
print('col_no1         col_no2        col_no3        col_no4        col_no5        col_no6        col_no7')
while(y<o):
    print('\t')
    z=int(input())
    
    if z==1:
        for letter in range(7):
            print(' ',col_1[letter],end='            ')
    elif z==2:
        for letter in range(7):
            print(' ',col_2[letter],end='            ')
    elif z==3:
        for letter in range(7):
            print(' ',col_3[letter],end='            ')
    else:
        for letter in range(7):
            print(' ',col_4[letter],end='            ')
          
    a=z
    my_list.append(a)
    y+=1
    
   
print('')    
m=1
your_word=''
for d in range(o):
        print('from the above columns,enter column number for letter',m,':')
        n=int(input())
        if my_list[d]==1:
            i=col_1[n-1]
        elif my_list[d]==2:
            i=col_2[n-1]
        elif my_list[d]==3:
            i=col_3[n-1]
        elif my_list[d]==4:
            i=col_4[n-1]
        your_word+=i
        m+=1
print('Your word is ' ,your_word)
