def anagrams(word, words):
    return [anam for anam in words if sorted(anam)==sorted(word)] 