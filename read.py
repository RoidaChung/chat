data = []
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count += 1 # count =count + 1
        if count % 1000 == 0:    # % 求餘數
            print(len(data))   

print('檔案讀取完了,總共有', len(data), '筆留言')
sum_len = 0
for d in data:
    sum_len += len(d)   # sum_len = sum_len + len(d)
#    print(sum_len,len(d))
print('平均留言長度', sum_len/len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('總共有',len(new), '筆資料小於100字元長度')
print(new[0])





    
