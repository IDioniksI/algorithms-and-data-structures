"""
Print all words that start with a letter other than
letter with which the first word of the text begins. Replace the first in the words
capital letter.
"""

cyan = '\033[36m'
red = '\033[31m'
purple = '\033[35m'
bold = '\033[1m'
end = '\033[0m'

while True:
    text = str(input('\nWrite the text, the text must end with a period and contain lowercase letters,'
                     ' with at least one space between words: '))

    if text.islower() and text.endswith('.'):
        print(f'\n{cyan}Our initial text:{end}\n', text)

        text_finally = text.replace(",", "").replace(".", "").lower().split(" ")

        if len(text_finally) == 0 or len(text_finally) == 1:
            print(f'\n{red}Your text does not pass verification.\n'
                  f'You may be submitting an empty value or just one word{end}')
            continue

        words = list(filter(bool, text_finally))

        letter = words[0][0]
        list_words = []
        list_words_up = []

        for word in words:
            if word[0] != letter:
                list_words.append(word)
                list_words_up.append(word.capitalize())

        if list_words:
            print(f'\n{cyan}All words that do not start with the first letter of the first word in the list:{end}\n',
                  list_words)
            print(f'\n{cyan}All words that do not begin with the first letter of the first word,'
                  f' and each word begins with a capital letter:{end}\n', list_words_up)
            break
        else:
            print(f'\nThere are no words that start with a different letter from the first word')
    else:
        print(f'\n{red}Your text does not pass verification.\n'
              f'Check for yourself that all words are in lowercase letters and the text ends with a period'
              f'You may be submitting an empty value or just one word{end}')

print(f'\n{purple}{bold}Thank you!{end}')
