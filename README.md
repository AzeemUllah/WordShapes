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
- ```get_word_shape('BBC') --> 'X' ```
- ```get_word_shape('iPhone') --> 'xXx'```
- ```get_word_shape('£24.4m') --> '£9.9x'```

Further examples on how to use the code can be found in the IPython notebook in this repository.

The .py program can be used as follow (you will need to install regex and use python 3):

```python word_shapes.py -text_path PATH_TO_TEXT_FILE```

```
Shape                                      Examples
------------------------------------------------------------------------------------------
x          layby                swans                bunny                frigid              
Xx         Nuri                 Chignell             Shakilus             Yade                
X          OUT                  ALEXANDRIA           LNG                  OCD                 
9          0283                 2004                 904                  372                 
'x         'the                 'see                 'higher              'smart              
x-x        month-long           muscle-wasting       side-footed          brick-laying        
Xx.        Inc.                 Col.                 Messrs.              Pkwy.               
9.9        9.77                 27.50                57.7                 0.68                
x'x        y'all                was'nt               l'architecture       l'état              
9,9        92,000               310,000              87,296               8,800               
XxXx       GeForce              LegalTech            McDowell             LaBrie              
X.X.       Y.O.                 U.K.                 J.P.                 S.C.                
9x         15m                  9lb                  21st                 6mins               
9-9        0-40                 266-154              14-12                76-43               
Xx-Xx      Hanks-Steven         Douglas-Roberts      Schleswig-Holstein   El-Erian            
Xx-x       Earth-bound          Vassar-educated      Oscar-conscious      Da-vid              
9-x-x      13-year-old          43-year-old          10-day-old           44-year-old         
9-x        10-day               53-nation            30-day               20-ounce            
x-x-x      five-million-pound   bricks-and-mortar    right-to-buy         ins-and-outs        
X.         P.                   X.                   H.                   E.                  
x-Xx       all-Irish            then-Indiana         al-Janabi            al-Thani            
x—x        slow—a               homer—and            paramilitary—in      shared—an           
X9         MI5                  A519                 A399                 XX2                 
x.x        year..a              drivers.com          icasualties.org      bricktheater.com    
£9         £135                 £27000               £175                 £338                
9:9        7:05                 1:51                 1:31                 5:32                
X.X        N.M                  N.J                  WB.N                 CBS.UL              
xXx        eHarmony             iLike                iCys                 exSILentia          
£9,9       £7,800               £43,622              £81,900              £23,000             
X-x        C-section            NATO-dominated       E-mail               G-protein           
9.9x       75.4m                23.5p                2.8bn                160.45p   
```
