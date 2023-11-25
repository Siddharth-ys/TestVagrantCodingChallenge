class Product:
    def __init__(self, name, unit_price, is_gst_eligible):
        self.name = name
        self.unit_price = unit_price
        self.is_gst_eligible = is_gst_eligible

def calculate_discounted_price(unit_price):
    discount_percentage = 5
    if unit_price >= 500:
        discount = (discount_percentage / 100) * unit_price
        return unit_price - discount
    else:
        return unit_price

def calculate_total_amount(basket):
    total_amount = 0
    max_gst = 0

    for product in basket:
        discounted_price = calculate_discounted_price(product.unit_price)
        total_amount += discounted_price

        if product.is_gst_eligible and discounted_price > max_gst:
            max_gst = discounted_price

    return total_amount, max_gst

# add price multiplied by quantity(predefined) eg for 3 enter 1000*3
product1 = Product("Item1", 1100*1, True)
product2 = Product("Item2", 900*4, True)
product3 = Product("Item3", 200*3, True)
product4 = Product("Item2", 100*2, False)

basket = [product1, product2, product3]

total_amount, max_gst = calculate_total_amount(basket)

print(f"Total Amount to be paid: Rs. {total_amount}")
print(f"Maximum GST eligible product: Rs. {max_gst}")
