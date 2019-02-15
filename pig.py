# pig latin function
# pig --> igpay
# apple --> appleway

def igpay(english_word):
    vowels = "aeiouAEIOU"
    # if word starts with vowels: A, E, I, O, U add "way" to the end of the word
    if english_word[0] in vowels: 
        return english_word+"way"
    # else move the first letter to the end and add "ay" to the end
    else:
        return english_word[1:]+english_word[0]+"ay"

the_word='desendent'

print("{0} in pig latin is {1}".format(the_word,igpay(the_word)))