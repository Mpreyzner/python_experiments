import markovgen

file_ = open('./jeeves.txt')
# from https://www.gutenberg.org/ebooks/8164
markov = markovgen.Markov(file_)

print(markov.generate_markov_text())
