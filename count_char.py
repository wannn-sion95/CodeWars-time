from collections import Counter 

def count_word(s):
        
        return dict(Counter(s) if s else{})
    
print(count_word("RIDWAN NASUTION"))
print(count_word(""))
        
