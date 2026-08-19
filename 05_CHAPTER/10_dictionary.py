# WHAT IS DICTIONARY ?
# 🔹 Definition:
# A dictionary is unordered, mutable, and indexed by keys.

#    1.Keys must be unique and immutable (like strings, numbers, tuples).
#    2.Values can be any type (list, string, number, etc.).
#    3.Written with curly braces {} in the form key:value pairs

marks = {"harry": 34, "jack": 45, "lily": 94 }

print(marks, type(marks))
print(marks["lily"])
marks["harry"] = 3
print(marks)