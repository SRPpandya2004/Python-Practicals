# Given  names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for  is not found, print Not found instead.

# Note: Your phone book should be a Dictionary/Map/HashMap data structure.

# Input Format

# The first line contains an integer, , denoting the number of entries in the phone book.
# Each of the  subsequent lines describes an entry in the form of  space-separated values on a single line. The first value is a friend's name, and the second value is an -digit phone number.

# After the  lines of phone book entries, there are an unknown number of lines of queries. Each line (query) contains a  to look up, and you must continue reading lines until there is no more input.

# Note: Names consist of lowercase English alphabetic letters and are first names only.


# Read input from STDIN. Print output to STDOUT

import sys
# Read the number of entries
n = int(input())

# Initialize dictionary to store phonebook data
phone_book = {}

# Populate the phonebook
for _ in range(n):
    name, num = input().split()
    phone_book[name] = num  # Store name as key and phone number as value

# Process queries until EOF
for line in sys.stdin:
    query = line.strip()
    if query in phone_book:
        print(f"{query}={phone_book[query]}")
    else:
        print("Not found")
