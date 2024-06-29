N=int(input())
Str=input().lower()
no_spaces = ''.join(Str.split())
 
 
 
from collections import Counter
 
def count_substring_in_string(given_string, substring):
    # Count characters in the given_string
    char_count = Counter(given_string)
    
    # Count characters in the substring
    sub_count = Counter(substring)
    
    # Calculate how many times the substring can be formed
    times = float('inf')
    for char in sub_count:
        times = min(times, char_count[char] // sub_count[char])
    
    return times
 
# Example usage:
given_string = Str
substring = "hackerearth"
 
result = count_substring_in_string(given_string, substring)
print(result)