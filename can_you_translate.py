
from collections import deque
import sys
# This function combines the two lists as one dictonary.
def lists_to_dict(l1,l2):
    if len(l1) != 0 and len(l2) != 0:
        return dict(zip(l1,l2))
    else:
        raise Exception("Please enter valid lists.")
        # Upon encountering an invalid input, the program will exit. 
        sys.exit(1)


def guess_words_from_french(list_of_french_words, list_of_correct_english_translations):
     
    wordDict = lists_to_dict(list_of_french_words,list_of_correct_english_translations)
    frenchWords = deque(list_of_french_words)
    
    while len(frenchWords) != 0:   
        w1 = frenchWords.popleft() 
        print(f'What is the English word for {w1} ? Input: ', end = "")
        user_input = str(input())
            
        if wordDict[w1].lower() == user_input.lower():
            print("Correct!")
        else:
            print("Incorrect")
            frenchWords.append(w1)
                    
        if len(frenchWords) == 0:
            print("All words are translated correctly!")           
    
if __name__ == '__main__':
    guess_words_from_french(["Chat", "Chien", "Poisson","Gateau"], ["Cat", "Dog", "Fish","Cake"])
    