from process import find_winter_summer

original_array = [1, -1, 3, 8, 6]
low_nums, high_nums = find_winter_summer(original_array)

print("Winter:", low_nums, "with length of:", len(low_nums))
print("Summer:", high_nums)
