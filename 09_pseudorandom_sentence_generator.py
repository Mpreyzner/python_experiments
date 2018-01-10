import markovgen

file_ = open('./jeeves.txt')
# from
markov = markovgen.Markov(file_)

print(markov.generate_markov_text())
