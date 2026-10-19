num = 1234

to_check_var = 0
num_check = num

while num_check > 0:
    ld = num_check % 10
    to_check_var = (to_check_var * 10) + ld
    num_check = num_check // 10

print(num, to_check_var)
print(num == to_check_var)