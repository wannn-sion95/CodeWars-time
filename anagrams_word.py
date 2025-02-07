def anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)

print(anagram("Ridwan", "Nawdir"))
print(anagram("Anita", "Tania"))
print(anagram("Rayna", "anyra"))
print(anagram("Fauzan", "Azura"))
