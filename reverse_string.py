# Problem: Reverse a String
# Difficulty: Easy
# Topic: Strings
# Mrithika — Biomedical Engineering Student

# ---- Problem Statement ----
# Given a string, return it in reverse order.
# Example: "hello" → "olleh"

# ---- Solution 1: Using Python slicing ----
def reverse_string(s):
    return s[::-1]

# ---- Solution 2: Using a loop ----
def reverse_string_loop(s):
    result = ""
    for char in s:
        result = char + result
    return result

# ---- Test Cases ----
print("=== Reverse String ===")
print(reverse_string("hello"))        # olleh
print(reverse_string("biomedical"))   # lacideomib
print(reverse_string("GitHub"))       # buhtiG

print("\n=== Using Loop ===")
print(reverse_string_loop("hello"))   # olleh
