def reverse_word():
    word = input("what is your word ? ")
    for i in range (len(word)- 1,-1,1):
        print(word[i], end="")
reverse_word()

# range pattern = range(start, stop, step)

# len(word) - 1
# means start at the last index,
# because the length of a word is 1 greater than its last index.

# -1 at stop
# means stop before -1.
# Because the stop value is exclusive, this allows index 0
# (the first character) to be included.

# -1 at step
# means move backwards by 1.