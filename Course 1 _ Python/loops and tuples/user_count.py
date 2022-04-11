def count_users(group):
  count = 0
  for member in get_members(group):
    count += 1
    if is_group(member = 3 ):
      count += count_users(member)
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18
print(count_users("Dales")) # Should be 
print(count_users("")) # Should be 