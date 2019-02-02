s = "Python CS 5590"
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)
words = s.split()
num_words=0
num_words = len(words)
print(num_words)