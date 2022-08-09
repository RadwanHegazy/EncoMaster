import random
from string import ascii_lowercase

class encrypt_word :

    def __init__(self, text) :
        word_after = text
        words = []
        for i in ascii_lowercase : words.append(i)


        enc = []

        for i in range(len(word_after)) :
            for x in range(10) : enc.append(words[random.randrange(0,len(words))])
            enc.append(word_after[i])


        self.get_enc_text = ''.join(enc)

class decrypt_text:
    def __init__ (self,text) :
        word_after = text
        final_word = []
        if len(word_after) >= 100 :
            final_word.append(word_after[10])
            a = 21
            for i in range(len(word_after)) :
                try :
                    final_word.append(word_after[a])
                    a = a + 11
                except IndexError :
                    break
        else:
            for i in range( int(f'{str(len(word_after))[0]}') ) : final_word.append(word_after[int(f"{i+1}{i}")])
        self.decrypted_text =  ''.join(final_word)



        
