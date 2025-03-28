def calculate_discount(price, discount_percent):

        #check if the percentage is higher or equal to 20%
        
    if discount_percent < 20:
        return price

    discount = (discount_percent / 100) * price
    final_price = price - discount

    return (final_price)
        
#prompt user to enter price and discount percent

price = int (input("Enter the price:"))
discount_percent = int(input("Enter the discount percent:"))

final_price = calculate_discount (price, discount_percent)
print (final_price)

 
