# Exercise 3: String Methods 

# Eric is considered offensive 

word_input = input("Enter a word: ")
split_word = word_input.split() 
capital_word_input = word_input.upper()
lowercase_word_input = word_input.lower()


if split_word == "Eric":
    if capital_word_input == True:
        remove_word = split_word.pop()
        if lowercase_word_input == True:
            remove_word = split_word.pop()

            