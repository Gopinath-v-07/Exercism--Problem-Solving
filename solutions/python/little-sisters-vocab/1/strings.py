def add_prefix_un(word):
    Pre_word='un'+word
    
    return Pre_word


def make_word_groups(vocab_words):
   prefix=vocab_words[0]
   result=[prefix]

   for i in vocab_words[1:]:
    result.append(prefix+i)
   return " :: ".join(result)
def remove_suffix_ness(word):
   root = word[:-4]
   if root.endswith('i'):
       word=root[:-1]+'y'
       return word
   else:
       return root
def adjective_to_verb(sentence, index):
    
    words=sentence.split()
    word=words[index].strip(".?,!")
    return word+"en"
    

    
