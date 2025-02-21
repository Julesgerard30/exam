#question 1
a = 16
a = a // 2
print(a**2)
a = a + 11
print(a+1)
a = a - 3
print(a)

#question 2
print((3+10**2/2) or 70.0)

#question 3
import datetime

a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "xyz" * (c // 3)
print(d)

#question 4
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
#call the function to find the number that is not a palindrome
print("A:", palindrome("6892149109325320763773670235239019412986"))
print("B:", palindrome("6800923757255865070000705685527573290086"))
print("C:", palindrome("9847255590886266818998186626880955527489"))
print("D:", palindrome("1414884937242655719669145562427394884141"))

# question 5
def count_pattern_occurrences(text):
    count = 0
    start = 0

    while True:
        start = text.find("C", start)
        if start == -1:
            break  # Stop if no more "C"
        if start > 0 and text[start - 1].isalpha():
            start += 1
            continue  # Skip if "C" is inside a word
        end = text.find("jeb", start)
        if end != -1:
            count += 1
        start = end + 3 if end != -1 else start + 1  # Continue searching

    return count

# Test
text = "Cwordjeb Ctextjeb Csomethingjeb notCjeb Canotherjeb"
print(count_pattern_occurrences(text))  # Output: 4 (correct)

#question 6
# Lists are mutable
my_list = [1, 2, 3]
my_list[0] = 10  # Works, We change the first element
print(my_list)   # Output: [10, 2, 3]

# Strings are immutable
my_string = "hello"
# my_string[0] = "H"  # ERROR Strings cannot be changed

# The only way to "change" a string is to create a new one
new_string = "H" + my_string[1:]
print(new_string)  # Output: Hello

#question 7
import random

# Step 1: Generate a list of 10 random numbers between 1 and 100
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Step 2: Process the list
for i in range(len(random_numbers)):
    if random_numbers[i] > 50:
        # Replace numbers greater than 50 with a new random number between 20 and 30
        random_numbers[i] = random.randint(20, 30)
    else:
        # Replace numbers lower than or equal to 50 with "XX"
        random_numbers[i] = "XX"

# Step 3: Print the final list
print(random_numbers)

#question 8
def is_valid_url(url):
    if not (url.startswith("http://") or url.startswith("https://")):
        return False
    if "." not in url[8:]:
        return False
    if url.endswith(".com") or url.endswith(".org") or url.endswith(".net"):
        return True
    return False

# Example tests
print(is_valid_url("http://example.com"))  # True
print(is_valid_url("https://my-site.org"))  # True
print(is_valid_url("ftp://notavalidurl.com"))  # False
print(is_valid_url("http://invalidurl"))  # False
print(is_valid_url("https://site.unknown"))  # False

#question 9
def days_since_birth(birthday):
    """
    This function calculates the number of days that have passed since birth,
    counting only whole years (excluding the birth year and the current year).
    """

    # Extracting the birth year from the given date in "DD-MM-YYYY" format
    birth_year = int(birthday[-4:])

    # Current year
    current_year = 2025

    # Computing the number of full years that have passed
    whole_years = current_year - birth_year - 1

    # Total days without considering leap years
    total_days = whole_years * 365

    # Counting leap years between birth_year+1 and current_year-1
    leap_years = 0
    for year in range(birth_year + 1, current_year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years += 1

    # Adding extra leap days
    total_days += leap_years

    return total_days
# Example usage
print(days_since_birth("12-06-2000"))  # Replace with your actual birthday