def disemvowel(word):
    result = ''
    for letter in word:
        if letter.lower() not in 'aeiou':
            result += letter
    print (result)
    
word = input("What is your word?")
disemvowel(word)
