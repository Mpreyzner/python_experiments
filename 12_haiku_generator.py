from random_words import RandomWords
from nltk.corpus import cmudict
import nltk
import markovgen

# The essence of haiku is "cutting" (kiru).[1]
#  This is often represented by the juxtaposition of two images or ideas and a kireji ("cutting word") between them,[2] a kind of verbal punctuation mark which signals the moment of separation and colours the manner in which the juxtaposed elements are related.

#  Traditional haiku consist of 17 on (also known as morae though often loosely translated as "syllables"),
# in three phrases of 5, 7, and 5 on, respectively.
#  A kigo (seasonal reference), usually drawn from a saijiki, an extensive but defined list of such terms.


# it fails from time to time because nlkt dict and RandomWords dict are incompatible
nltk.download('cmudict')
dict = cmudict.dict()
file = open('./Resources/alice.txt')


def count_syllables(word):
    # it fails when encounter hyphenated words a
    word = ''.join(ch for ch in word if ch.isalpha())
    return (len(list(y for y in x if y[-1].isdigit())) for x in dict[word.lower()])


rw = RandomWords()
markov = markovgen.Markov(file)


def generate_phase(syllabes_count):
    syllables_count_total = 0
    words = markov.generate_markov_text(syllabes_count).split(' ')
    phase = []
    # there is a case where last word may be longer we would need to generate a new chain
    for i in range(len(words)):
        syllabes_in_word = next(count_syllables(words[i]))
        if syllabes_in_word < syllabes_count:
            phase.append(words[i])
            syllables_count_total = syllables_count_total + syllabes_in_word

        if syllables_count_total == syllabes_count:
            return words
        elif syllables_count_total > syllabes_count:
            phase.pop()
            syllables_count_total = syllables_count_total - syllabes_in_word

    return words


first_phase = ' '.join(generate_phase(5))
second_phase = ' '.join(generate_phase(7))
third_phase = ' '.join(generate_phase(5))

haiku = first_phase + ", \n" + second_phase + ", \n" + third_phase + '.'
print(haiku)

# TODO add seasonal words
# add markov gen so it maybe makes sence?
