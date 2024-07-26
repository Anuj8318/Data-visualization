import numpy as np

# 1. Calculate the total revenue generated by two product categories in a store
# Input:
# category 1 revenue np.array([500, 600, 700, 550])
# category2 revenue np.array([450, 700, 800, 600])
# Output: Total Revenue: [950 1300 1500 1150]

category_1= np.array([500, 600, 700, 550])
category_2 = np.array([450, 700, 800, 600])

category =  category_1+category_2
print("Total Revenue:" ,category)


# 2. Calculate the profit made by a company
# Input: revenue = np.array([10000, 12000, 11000, 105001) expenses np.array([4000, 5000, 4500, 4800])
# 2 to 10.
# Output:
# Profit: [6000 7000 6500 5700]


revenue = np.array([10000, 12000, 11000, 10500])
expenses = np.array([4000, 5000, 4500, 4800])

# Calculate the profit
profit = revenue - expenses

# Display the profit
print("Profit:", profit)





# 3. Determine which products in a store are out of stock (quantity is 0).
# Input: inventory= np.array([10, 0, 5, 0, 20, 01)
# Output: Out of Stock Products: [0.00]



# Inventory data
inventory = np.array([10, 0, 5, 0, 20, 0])

# Determine which products are out of stock (quantity is 0)
out_of_stock = inventory == 0

# Display the indices of out-of-stock products
print("Out of Stock Products:", np.where(out_of_stock)[0])





#  Calculate the total cost of items in a shopping cart, considering the quantity and price<hr/>

# Input: <br/>
# quantity = np.array([2, 3, 4, 1])<br/>
# price_per_items = np.array([10.0, 5.0, 8.0, 12.0])<br/>

# Output: <br/>
# Total cost of items : [20. 15. 32. 12.]

quantity = np.array([2, 3, 4, 1])
price_per_items = np.array([10.0, 5.0, 8.0, 12.0])

print("Total cost of items : ", quantity * price_per_items)
qantity = np.array([2,3,4,1])
price_per_item= np.array([10.0,])