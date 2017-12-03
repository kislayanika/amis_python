mylist = input("Enter list: ").split()
empty_list = []
def group(list, iterator):
    if iterator == len(list):
        return max(empty_list)
    secondlist = "".join(list)
    count_el = list.count(list[iterator])
    if (count_el - iterator)*str(list[iterator]) in secondlist:
        empty_list.append(count_el - iterator)
    return group(list, iterator + 1)
print(group(mylist, 0))
input()
