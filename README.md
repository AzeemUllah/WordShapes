# Word Shapes

The code in this  repository (both the .py program and the IPython notebook) implements ideas introduced by prof. Hinrich Schütze in his word shapes lecture:
http://www.cis.lmu.de/~hs/teach/15w/intro/pdf/wordshapes.pdf  

Natural language processing (NLP) applications usually assume that language users are going to use words within a finite word vocabulary. However, this is an unrealistic assumption since new words are always produced by users due to the creative use of any human language. This limitation leads to unknown words or out-of-vocabulary words (OOV) problem.   

Even though it is not realistic to assume a finite word vocabulary, unknown words would usually have similar shapes to some other known words (i.e., in-vocabulary words). A word shape for any word can be obtained as follows:

- Replace all lower case letters with ’x’
- Replace all upper case letters with ’X’
- Replace all digits letters with ’9’
- “Deduplicate”: any sequence of n > 1 identical characters c is replaced by a single copy of c

For example:
- get_word_shape('BBC') --> 'X'
- get_word_shape('iPhone') --> 'xXx'
- get_word_shape('£24.4m') --> '£9.9x'

Further examples on how to use the code can be found in the IPython notebook in this repository. 
 
The .py program can be used as follow: 

python word_shapes.py -text_path PATH_TO_TEXT_FILE