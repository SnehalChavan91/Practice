def smallest_num(items):
    smallest=items[0]
    for i in items:
        if i<smallest:
            smallest=i
    return smallest
print(smallest_num([10,20,5,-5,40]))