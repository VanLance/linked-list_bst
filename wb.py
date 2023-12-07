def sum_singles(alist):
  hash_map = {}
  for num in alist:
    hash_map[num] = hash_map.get(num, 0) + 1
  return sum(k for k, v in hash_map.items() if v == 1)

print(sum_singles([4,5,7,5,4,8]), 15)
print(sum_singles([9, 10, 19, 13, 19, 13]), 19)
print(sum_singles([16, 0, 11, 4, 8, 16, 0, 11]), 12)