import random

# The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows:
# start with any positive integer n.
# Then each term is obtained from the previous term as follows:
# if the previous term is even, the next term is one half the previous term.
# Otherwise, the next term is 3 times the previous term plus 1.
#
# The conjecture is that no matter what value of n, the sequence will always reach 1.

root = random.randint(1, 99999999999999)
sequence = []


def get_next(number):
    if number % 2 == 0:
        return number//2
    else:
        return number * 3 + 1


current = root
while current != 1:
    sequence.append(current)
    current = get_next(current)

print(sequence)
print("Reached 1 in " + str(len(sequence)) + ' steps')
# Now form a sequence by performing this operation repeatedly, beginning with any positive integer, and taking the result at each step as the input at the next.#
