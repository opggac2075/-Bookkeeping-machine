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
    products.append([name, price])          #以上功能為輸入商品及價格，加入總清單
    sum += price                            #將所有的花費及項目做總結
print('這是你的商品總表:', products)         #以下功能為將帳務資訊顯示
print('你的商品總共有', count-1, '項')
print('你總共花費的金額:$', sum)


    

 