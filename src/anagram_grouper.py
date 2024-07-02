def anagram_grouper(word_list):
    grouped_anagrams = {}

    for word in word_list:
        sorted_word = ''.join(sorted(word))
        if sorted_word in grouped_anagrams:
            grouped_anagrams[sorted_word].append(word)
        else:
            grouped_anagrams[sorted_word] = [word]

    return list(grouped_anagrams.values())


words = ["bat", "nat", "ate", "tan", "tea", "eat"]
print(anagram_grouper(words))