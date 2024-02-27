import itertools
all_sequences = itertools.permutations('abc')
for sequence in all_sequences:
    print(sequence)