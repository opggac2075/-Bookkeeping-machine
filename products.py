print('(若要結束記帳，請輸入over)')
products = []
sum = 0
while True:
    name = input('請輸入購買的商品名稱:')
    if name == 'over':
        break
    price = input('請輸入購買的商品價格:')
    price = int(price)
    products.append([name, price])
    sum += price
print('這是你的商品總表:', products)
print('你總共花費的金額:$', sum)


    

 