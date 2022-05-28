# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from tabnanny import check
word = input("word ")
anagram = input("anagram ")

def find_anagram(word, anagram):
    # [assignment] Add your code here
    if(sorted(word) == sorted(anagram)):
        print("True")
    else:
        print("false")

    return True

find_anagram(word, anagram)
