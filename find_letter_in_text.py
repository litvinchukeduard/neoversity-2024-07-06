"""
В нас є речення, потрібно написати функцію, яка буде шукати символ 
в цьому реченні та повертати його індекс
"""

# def find_letter_in_text(text: str, symbol: str) -> int:
#     return text.find(symbol)

def find_first_letter_in_text(text: str, searched_symbol: str) -> int: # Hello, world!, w
    for index, symbol in enumerate(text):
        # if symbol != searched_symbol:
        if symbol == searched_symbol:
            return index
    return -1
    # for i in range(len(text)):
    #     if text[i] == searched_symbol:
    #         return i
    # return -1
    # return None
        
# print(find_first_letter_in_text("Hello, world!", "l"))
