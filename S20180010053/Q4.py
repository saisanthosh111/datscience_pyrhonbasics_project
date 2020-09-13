class LetterFilter:

    def __init__(self, s):
        self.s = s


# Enter your code here.
# Complete the classes below.
# Reading the inputs and writing the outputs are already done for you.
#
class LetterFilter:

    def __init__(self, s):
      self.s = s

    def filter_vowels(self):
        x=""
        for i in self.s:
            if i not in ["a","e","i","o","u"]:
                x=x+i
        return x
        # Enter your code here
        # Return a string

    def filter_consonants(self):
        x=""
        for i in self.s:
            if i in ["a","e","i","o","u"]:
                x=x+i

        return x
        # Enter your code here
        # Return a string

s = input()
f = LetterFilter(s)
print(f.filter_vowels())
print(f.filter_consonants())
