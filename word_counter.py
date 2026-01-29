def count_word() :
    sent = input("Enter you sentence :  ")
    word = sent.split()
    return len(word)

result = count_word()
print("Total number of words in the sentence is :  ",result)