# 题意: 给一个单词的列表，假如单词里的字母是按'字母表排序'，加入到结果中，最后将结果排序后返回

def sorted_words(word_list):
    result = []
    for word in word_list:
        if is_alphabetically_sorted_word(word):
            result.append(word)
    
    # 将符合字母表排序的单词列表排序后返回
    result.sort()
    return result

# check if a word where the letters are alphabetically sorted
# alphabetically sorted: 按字母表排序，题目中提到字母排序基于"Unicode Values"，
# "Unicode"是"字符集(Character Set)"中的一种，里面每一个字(如: a, b, c）在字符集中都有一个编号
# 如a的编号是61, b的编号是62，而且大小写字符编号也不同，如a的编号是61, A的编号是41。
# "Unicode" 字符集可以参考https://unicode-table.com/en/
def is_alphabetically_sorted_word(word):
    if len(word) <= 1:
        return True
    else:
        is_sorted = True
        previous_character = word[0]
        for index in range(1, len(word)):
            character = word[index]
            # 编程语言内置的比较方法就是按字母表排序，因此直接比较即可，题目中红字的说明有写。
            if previous_character > character:
                is_sorted = False
            previous_character = character

        return is_sorted

print sorted_words(["bet", "abacus", "act", "celebration", "door"])
print sorted_words(["apples", "bananas", "spam"])
print sorted_words(["aims", "Zip"])