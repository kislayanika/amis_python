elements = []
k = int(input("Enter number of elements: ")) 
for i in range(k):
    element = input("Enter element: ")
    elements.append(element)
universal_element = []
for element in elements:
    if elements.count(element) == 1:
        universal_element.append(element)
print(" ".join(universal_element))
input()
