my_elem = "testing jio" # Element is a < i > z
my_elem_list = ["a", "b", "c", "t", "e", "o", "i", "j", "n"]

response = {}
# Here, I need to implement the ASCII concept. 
for i in my_elem:
    response[ord(i)] = response.get(ord(i), 0) + 1
print(response)
for j in my_elem_list:
    if response.get(ord(j)):
        print(chr(response.get(ord(j)))  , response.get(ord(j)))