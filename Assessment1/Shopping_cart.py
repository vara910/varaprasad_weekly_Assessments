items= input("Enter items: ").split()
prices= input("Enter the prices: ").split()

# Convert price strings to integers
price_list = [int(price) for price in prices]

def cart_items(items, prices):
    items_list = items  
    return items_list, price_list

def calculate_items_price(price_list):
    return sum(price_list)

def main():
    items_list, price_list = cart_items(items, prices)  
    total_cost = calculate_items_price(price_list)  # Calculate the total cost
    print("Total price of the items:", total_cost)
    print("Items list: ", items_list)
main()
