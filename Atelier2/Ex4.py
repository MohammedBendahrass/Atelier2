set1 = {23, 42, 65, 57, 78, 83, 29}
set2 = {57, 83, 29, 67, 73, 43, 48}

intersection = set1.intersection(set2)

set1.difference_update(intersection)

print(f"Intersection : {intersection}")
print(f"Set 1 Apres Supprission : {set1}")