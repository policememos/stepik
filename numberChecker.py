n = '+7)123)456-58-99'
n = list(n)
q = ['+','(',')','-','-']
w = [0,1,4,7,9]
ans = "ДА"
temp1 = []
if len(n) == 16 and n[1] == '7':
    for i in w:
        temp1 += n.pop(i)
    if not temp1 == q: 
        ans = "НЕТ"
        

    for i in n:
        try:
            a = int(i)
            
        except:
            ans = "НЕТ"
            break
else:
    ans = "НЕТ"        
print(ans)
