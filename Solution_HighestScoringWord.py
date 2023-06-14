def highest_score(sentence):
    sentence_list_words = sentence.split()
    lsentence = sentence.lower()
    lsentence_list_words = lsentence.split()
    word_value = list(range(len(lsentence_list_words)))

    import string
    alphabet_list = list(string.ascii_lowercase)
    alphabet_value_list = alphabet_list
    for letter_value in range(len(alphabet_list)):
        alphabet_value_list[letter_value] = letter_value + 1
    alphabet_list = list(string.ascii_lowercase)

    word_index = 0
    for word in lsentence_list_words:
        word_list_letters = list(word)
        for letter in word_list_letters:
            letter_index = alphabet_list.index(letter)
            word_value[word_index] = alphabet_value_list[letter_index] + word_value[word_index]
        word_index += 1

    highest_word_index = word_value.index(max(word_value))
    highest_word = sentence_list_words[highest_word_index]

    print("The word with the highest score is: " + highest_word)


def main():
    sentence = str(input("Please enter a sentence: "))
    highest_score(sentence)


main()
