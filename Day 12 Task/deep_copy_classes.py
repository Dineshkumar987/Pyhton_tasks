import copy

classes = [["Math", [30, 35]], ["Science", [25, 28]]]

classes_copy = copy.deepcopy(classes)

classes[0][1][0] = 40

print("Original:", classes)
print("Copied:", classes_copy)