print('(若要結束記帳，請輸入over)')
products = []   
count = 0
sum = 0
while True:                         
    name = input('請輸入購買的商品名稱:')
    count += 1
    if name == 'over':
        break
    price = input('請輸入購買的商品價格:')
    price = int(price)
    d = str(price)                          #因為int在write的時候不能夠被連接(TypeError: can only concatenate str (not "int") to str)，用型別轉換轉成str之後再存成另一個變數加入清單，就可以符合write的條件了
    products.append([name, price, d])       #以上功能為輸入商品及價格，加入總清單
    sum += price                            #將所有的花費及項目做總結
print('這是你的商品總表:', products)         #以下功能為將帳務資訊顯示
for p in products:
    print(p[0], '的價格是:$', p[1], )
print('你的商品總共有', count-1, '項')
print('你總共花費的金額:$', sum)
                                                #以下功能為將輸入的商品項目及價格以表格的方式存入電腦中
with open('Accounttable.csv', 'w') as f:   
    for p in products:
        f.write(p[0] + ',' + p[2] + '\n' )

 