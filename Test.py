def reverse_word(word):
    reversed = ""
    for letter in word:
         reversed = letter + reversed
    return reversed

def check_all_palindromes( arr):
    if arr[0] == reverse_word(arr[0]):
         if arr[1] == reverse_word(arr[1]):
              if arr[2] == reverse_word(arr[2]):
                  print(True)
    print(False)    
check_all_palindromes(["madam", "racecar", "level"])