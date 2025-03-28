def calculate_discount(price, discount_percent):

        #check if the percentage is higher or equal to 20%
        
    if discount_percent < 20:
        return price

    discount = (discount_percent / 100) * price
    final_price = price - discount

    return (final_price)
        
#assign values

price = 200
discount_percent = 20
final_price = calculate_discount (price, discount_percent)
print (final_price)
