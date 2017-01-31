shopping_list = ["bananas"]


def add_item(item_name):
    if str.lower(item_name) in shopping_list:
        print "Item already in list!"
        return shopping_list
    else:
        shopping_list.append(item_name)
        return alpha_list(shopping_list)


def alpha_list(shopping_list):
    list.sort(shopping_list)
    return str.lower(shopping_list)


print add_item("APPLE")

print shopping_list