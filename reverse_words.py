# The function accepts a string ‘str’ as its argument. The function needs to reverse the order of
# the words in the string.

s=input()
words = s.split(' ')
# print(words) ['hello','world']
reversed_words = words[::-1]
print(' '.join(reversed_words))
