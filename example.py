def sorted_words(word_list):
    result = []
    for word in word_list:
        if is_alphabetically_sorted_word(word):
            result.append(word)
    
    result.sort()
    return result

def is_alphabetically_sorted_word(word):
    if len(word) <= 1:
        return True
    else:
        is_sorted = True
        previous_character = word[0]
        for index in range(1, len(word)):
            character = word[index]
            if previous_character > character:
                is_sorted = False
            previous_character = character

        return is_sorted

print sorted_words(["bet", "abacus", "act", "celebration", "door"])
print sorted_words(["apples", "bananas", "spam"])
print sorted_words(["aims", "Zip"])