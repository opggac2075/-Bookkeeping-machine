import os
products = []  
if os.path.isfile('Account_table.csv'): #檢查帳表檔案有沒有在電腦裡
    print('已讀取到舊的帳表檔案，請輸入以下資訊更新帳表')
    with open('Account_table.csv', 'r') as f: #讀取舊帳表檔案
        for line in f:
            if 'Commodity,Price' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)
else:
    print('沒有帳表檔案，請輸入以下資訊建立新的帳表檔案')  

print('(若要結束記帳，請輸入over)')#以下功能為輸入商品及價格，加入總清單 
print('(在輸入資訊時，請確保帳表為非開啟狀態)')
count = 0
sum = 0
while True:                         
    name = input('請輸入購買的商品名稱:')
    count += 1
    if name == 'over':
        break
    price = input('請輸入購買的商品價格:')    
    price = int(price)
    products.append([name, price])
    sum += price#將所有的花費及項目做總結

print('這是你的商品總表:', products)#以下功能為將帳務資訊顯示
for p in products:
    print(p[0], '的價格是:$', p[1], )
print('你的商品總共有', count-1, '項')
print('你本次總共花費的金額:$', sum)

#以下功能為將輸入的商品項目及價格以表格的方式存入電腦中
with open('Account_table.csv', 'w') as f:   
    f.write('Commodity,Price\n')#在for loop之前就先寫入欄位        
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n' )  #因為int在write的時候不能夠被連接(TypeError: can only concatenate str (not "int") to str)，只要在前面加上str()將數值轉為字串就可以符合write的條件了


 