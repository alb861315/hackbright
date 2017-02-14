# grocery_string = "item:apples,quantity:4,price:1.50\n"
# split_date = grocery_string.split(",")
# print split_date
# item_data = split_date[0]
# print item_data
# item_list = item_data.split(":")
# print item_list
# item_name = item_list[1]
# print item_name

# my_name = "Kyoko"
# print list(my_name)

# num = "1,2,3,4,5"
# num_list = num.split(",")
# print num_li
# string = "One fish two fish red fish blue fish"
# print string.split("fish")

grocery_string = "item:apples,quantity:4,price:1.50\n"


def grocery_bill(grocery_string):
    split_data = grocery_string.split(",")
    print "split_data = ", split_data

    quantity_data = split_data[1]
    print "quantity_data = ", quantity_data

    quantity_list = quantity_data.split(":")
    print "quantity list =", quantity_list

    quantity = int(quantity_list[1])
    print "quantity= ", quantity

    price_data = split_data[2].strip()
    print "price_date = ", price_data

    price_list = price_data.split(":")
    print "price_list = ", price_list

    price = float(price_list[1])
    print "price = ", price

    bill_total = quantity * price
    return bill_total

print "Bill total: ", grocery_bill(grocery_string)
