# Function Arguments & Return Values

# 1.Write a function full_name(first, last) that takes first name and last name
# as parameters and returns a single string in the format "First Last" .

# 2.Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:
# Both length and width
# Only length (use default width)

# 1.
def full_name(first, last):
    return first+last

print(f"{full_name("Dhruba", " Pramanik")}")

# 2.
def calculate_area(length, width=10):
    area = length*width
    return area

area_rec = calculate_area(5)
print(f"AREA : {area_rec}")

