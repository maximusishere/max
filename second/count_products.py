class Product:
    def __init__(self, name, retail_price, purchase_price):
        self.name = name
        self.retail_price = retail_price
        self.purchase_price = purchase_price

    @property
    def profit(self):
        return self.retail_price - self.purchase_price
        
        # Опишите свойство profit
        
    @staticmethod
    def average_price(retail_price):
        oo = 0
        for i in retail_price:
            oo +=i
        return 0 if len(retail_price) == 0 else oo / len(retail_price)

       # Опишите статический метод average_price()
    
    @property
    def information(self):
        return f'Товар: {self.name}, розничная цена: {self.retail_price}, закупочная_цена: {self.purchase_price}'
    
        # Опишите свойство information


# Данные для проверки, не изменяйте их.
product_1 = Product('Картошка', 100, 90)
product_2 = Product('Перчатки', 150, 120)
product_3 = Product('Велосипед', 170, 150)

assortment_prices = [
    product_1.purchase_price, 
    product_2.purchase_price, 
    product_3.purchase_price
]

print(f'Средняя стоимость: {Product.average_price(assortment_prices)}')
print(f'Прибыль магазина с товара {product_1.name}: {product_1.profit}')
print(f'Информация о товаре {product_1.name}: {product_1.information}')