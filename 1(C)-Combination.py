from import combinations
list=[1, -8, 3, 4, -7]
print("Positive Combinations")
for r in rang(len(list)+1):
  for combo in combinations(list, r):
    if all(num > 0 for num in combo):
      print(combo)
