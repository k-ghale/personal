
#
# def look_for_key(box):
#     for item in box:
#         if item.is_a_box():
#             look_for_key(item)
#         elif item.is_a_key():
#             print(" key_found ");
#

# recursion function for a countdown
def countdown(i):
    if i == 0:
        return

    print(i)
    return countdown(i-1)

# func to calculate factorial
    # 5! = 5 * 4 * 3 * 2 * 1
def fact(x):
    if x == 1:
        return 1
    return x * fact(x-1)


# implementat

num = 10

countdown(num)
print(fact(5))
print(fact(2))
print(fact(3))
