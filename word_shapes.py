"""
A program to process a text corpus and extract word shapes.
"""

from collections import defaultdict
import regex as re
import argparse


def get_word_shape(word):
    """
    Given a word, return its shape. Exploits regular expressions.
    """
    
    # Replace all lower case letters with ’x’
    word_shape = re.sub(r"[[:lower:]]", 'x', word)
    
    # Replace all upper case letters with ’X’
    word_shape = re.sub(r"[[:upper:]]", 'X', word_shape)
    
    # Replace all digits letters with ’9’
    word_shape = re.sub('\d', '9', word_shape)
    
    # Deduplicate: any sequence of n > 1 identical characters c
    # is replaced by a single copy of c
    word_shape = re.sub(r'(.)\1{1,}', r'\1', word_shape) 
    
    return word_shape  


def generate():
    """
    Read text file from user, and generate summary statistics.
    """

    DISCR = 'Generate word shapes from text corpus.'
    parser = argparse.ArgumentParser(description=DISCR)

    parser.add_argument('-text_path', type=str, help='Path to corpus.', required=True)
    
    args = parser.parse_args()

    # collect word frequency (and word shape) statistics 

    word_counts = defaultdict(int)
    shape_counts = defaultdict(int)
    words_per_shape = defaultdict(set)

    with open(args.text_path) as f:
        for line in f:
            for word in line.split():
                word_counts[word] += 1

    for word in word_counts:
        w_shape = get_word_shape(word) 
        shape_counts[w_shape] += word_counts[word]
        words_per_shape[w_shape].add(word)


    # sort word shapes by frequency 
    shape_counts_sorted = sorted(shape_counts.items(), key=lambda x: x[1], reverse=True)

    # print some output
    s = "{0:10} {1:20} {2:20} {3:20} {4:20} {5:20}"

    print("{0:10} {1:>50}".format('Shape', 'Examples'))
    print(''.join('-' for _ in range(110)))

    for (w_shape, count) in shape_counts_sorted[:50]:
        words = [w for w in words_per_shape[w_shape]]
        
        if len(words) > 5:
            print(s.format(w_shape, *words[:5]))


def main():
    generate()

if __name__ == '__main__':
    main()
