# How many times a element is repeated in a dictonary 

my_list = [1,3,5,3,21,23,4,5,6,3,21,1]

def calculate_frequency(my_elem: list):
    response = {

    }

    while my_elem != []:
        first_elem = my_elem[-1]
        for i in my_elem:
            if i == first_elem:
                if response.get(i):
                    response[i] = response[i] + 1
                    my_elem.remove(i)
                else:
                    response[i] = 1
        my_elem.pop()
    return response

print(calculate_frequency(my_list))


# As per video
response = {}
my_list = [1,3,5,3,21,23,4,5,6,3,21,1]

for i in range(0, len(my_list)):
    response[my_list[i]] = response.get(my_list[i], 0) + 1

print(response)