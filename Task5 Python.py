numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Original list: ", numbers)

numbers.append(110)
print("\nAfter append: ", numbers)

numbers.insert(2, 25)
print("\nAfter insert at 3rd position: ", numbers)

numbers.remove(40)
print("\nAfter removing 40: ", numbers)

numbers.pop()
print("\nAfter popping last element: ", numbers)

index_value = numbers.index(50)
print("\nIndex of 50: ", index_value)

count_value = numbers.count(20)
print("\nCount of 20: ", count_value)

numbers.sort()
print("\nAfter sorting: ", numbers)

numbers.reverse()
print("\nAfter reversing: ", numbers)


new_numbers = [200, 220, 240, 260, 280]
numbers.extend(new_numbers)
print("\nAfter extending with new numbers: ", numbers)