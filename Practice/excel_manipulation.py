import openpyxl

book = openpyxl.load_workbook('F:/viranisystem/python_excel.xlsx')
sheet = book.active

for row in sheet.iter_rows(min_row=1, min_col=1, max_row=20):
    sku=row[0].value
    price = float(row[1].value)
    compare_at_price = row[2].value
    if(row[3].value is not None):
        stone_list = row[3].value.split(',')
        stone=stone_list[0]
    else:
        stone=""
    new_price=0
    if(sku[1]=='G' and price<2500):#if product is gold and price is less than $2500
        compare_at_price=price+price*0.10
        new_price=compare_at_price-compare_at_price*0.15
    elif(sku[1]=='D' and price<2500 and stone=='Diamond'):
        compare_at_price = price + price * 0.30
        new_price = compare_at_price - compare_at_price * 0.40

    print(sku,price,compare_at_price,new_price,stone)