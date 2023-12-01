import random
import mojimoji
import jaconv

def ranndom_convert(input_str):
    result = ''
    for char in input_str:
        choice = random.choices(['fullwidth', 'halfwidth', 'kana', 'keep'])[0]
        
        if choice == 'fullwidth':
            result += mojimoji.han_to_zen(char)
        elif choice == 'halfwidth':
            result += mojimoji.zen_to_han(char)
        elif choice == 'kana':
            result += jaconv.z2h(jaconv.hira2hkata(char),digit=True, ascii=True)
        else:
            result += char
    return result