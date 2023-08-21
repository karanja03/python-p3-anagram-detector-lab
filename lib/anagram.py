class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, anagrams):
        matching_anagrams = []

        for anagram in anagrams:
            # Check if anagram is not the same as the original word
            if anagram.lower() != self.word.lower():
                # Check if the sorted characters of both words are the same
                if sorted(self.word.lower()) == sorted(anagram.lower()):
                    matching_anagrams.append(anagram)

        return matching_anagrams
