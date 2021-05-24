def wordMixer(sentence):
    from random import shuffle
    sentence_list = sentence.split(" ")
    sentence = ""
    for word in sentence_list:
        if len(word) == 1:
            sentence += word[0] + " "
        else:
            word_middle = word[1:-1]
            word_middle_list = [word_middle[i] for i in range(len(word_middle))]
            shuffle(word_middle_list)
            word_middle = "".join(word_middle_list)
            sentence += word[0] + word_middle + word[-1] + " "

    return sentence    
