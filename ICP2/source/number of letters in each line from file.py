fname = "scratch.txt"

num_lines = 0
num_words = 0
num_chars = 0

with open(fname, 'r') as f:
        line = f.readline()

        while line !="":
         words = line.split(" ")
         num_lines += 1
         num_words = len(words)
         num_chars = len(line)
         line=f.readline()
         print(num_words)
         print(num_chars)
         print(num_lines)