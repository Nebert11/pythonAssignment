def calculate_discount(price, discount_percent):
        
    if discount_percent < 20:
        return price

    discount = (discount_percent / 100) * price
    final_price = price - discount

    return (final_price)

price = int (input("Enter the price:"))
discount_percent = int(input("Enter the discount percent:"))

final_price = calculate_discount (price, discount_percent)
print (final_price)

 
