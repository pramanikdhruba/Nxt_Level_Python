# Modules and Pip – Using External Libraries
# 1.Import the math module and use it to:
#       i.Find the square root of 144
#       ii.Calculate sin(90°) (hint: use math.radians() )
# 2.Install and import the requests module (if available) and use it to fetch data from "https://api.github.com" .

# -------------------------------
# 1. Using the math module
# -------------------------------
import math

# i. Find the square root of 144
sqrt_result = math.sqrt(144)
print("Square root of 144:", sqrt_result)

# ii. Calculate sin(90°)
sin_result = math.sin(math.radians(90))
print("sin(90°):", sin_result)

# -------------------------------
# 2. Using the requests module
# -------------------------------
# (Make sure requests is installed: run 'pip install requests' in terminal if needed)
import requests

# Fetch data from GitHub API
response = requests.get("https://api.github.com")

# Display the status code and part of the response data
print("\nStatus Code:", response.status_code)
print("Response JSON Preview:", response.json())