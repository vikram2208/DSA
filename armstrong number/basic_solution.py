my_num = "1634"

power_elem=len(str(my_num))
result = 0

for i in range(0, power_elem):
    result = result + (int(my_num[i]) ** power_elem)

print(result)


# Without chaning into string
my_num = 1634
copy_elem = my_num
result = 0
power_elem=len(str(my_num))

while copy_elem > 0:
    ld = copy_elem % 10
    result = result + (ld ** power_elem)
    copy_elem = copy_elem // 10

print(result == my_num)