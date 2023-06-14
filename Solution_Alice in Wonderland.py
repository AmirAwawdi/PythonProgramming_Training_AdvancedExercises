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

    # print("The word with the highest score is: " + highest_word)
    return str(highest_word)


def main():

    sentence = str(input("Please enter a sequence of sentences and hit Enter after each one: "))
    sentences = list()
    highest_word_list = list()
    counter = 0

    while sentence != "":
        sentences.append(sentence)
        highest_word_list.append(sentence)
        sentence = str(input("Enter another sentence or finnish the sequence by hitting Enter: "))

    for sentence in sentences:
        highest_word_list[counter] = highest_score(sentence)
        counter += 1

    if not highest_word_list:
        print("You didn't enter any sentence")
    else:
        counter = 1
        for word in highest_word_list:
            print("In sentence #" + str(counter) + ", the highest-scoring word is " + word)
            counter += 1

    new_highest_word_list = []
    for word in highest_word_list:
        if word not in new_highest_word_list:
            new_highest_word_list.append(word)

    for word in new_highest_word_list:
        counter = 0
        for sentence in sentences:
            sentence_list_words = sentence.split()
            for sentword in sentence_list_words:
                if word.lower() == sentword.lower():
                    counter += 1
        print(word + ":" + str(counter))


main()


