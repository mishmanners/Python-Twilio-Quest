import sys

order_of_succession = sys.argv
order_of_succession.pop(0)

print("This is the order of succession:")
for index,item in enumerate(sys.argv, start=1):
    ordered_list = f"{index}. {item}"
    print(ordered_list)
