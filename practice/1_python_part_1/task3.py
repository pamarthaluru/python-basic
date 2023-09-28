"""
Write function which receives list of text lines (which is space separated words) and word number.
It should enumerate unique words from each line and then build string from all words of given number.
Restriction: word_number >= 0
Examples:
    >>> build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1)
    'b 2 dog'
    >>> build_from_unique_words('a b c', '', 'cat dog milk', word_number=0)
    'a cat'
    >>> build_from_unique_words('1 2', '1 2 3', word_number=10)
    ''
    >>> build_from_unique_words(word_number=10)
    ''
"""
from typing import Iterable


def build_from_unique_words(*lines: Iterable[str], word_number: int) -> str:
    unique_words=[]
    
    for line in lines:
        words=line.split()
        unique_words.extend(words)

    word_count={}
    
    for word in unique_words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count=1
    if word_number<0:
        selected_word=""
    else:
        selected_word=""
        for word, count in word_count.items():
            if count ==word_number:
                if selected_word:
                    selected_word +=' '
                selected_word+=word
    
    
    return selected_word

print(build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1))
print(build_from_unique_words('a b c', '', 'cat dog milk', word_number=0))
print(build_from_unique_words('1 2', '1 2 3', word_number=10))
print(build_from_unique_words(word_number=10))

