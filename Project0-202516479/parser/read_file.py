import re

#The purpose of this file is to read the given text, clean it to make it more simple to decode 
#and to manage to find blocks within the text 

def split_text_by_symbol(text, symbol="."):
    """
    The function `split_text_by_symbol` splits a text into segments using a specified symbol as the
    delimiter and returns a list of cleaned segments.
    
    :param text: string 
    :param symbol: char - used to split the text into
    segments. By default, the `symbol` parameter is set to "." 

    :return: list - list of the stripped segments
    """
    segments = text.split(symbol) 
    return [segment.strip() for segment in segments if segment.strip()]


def clean_text(text):
    """
    The `clean_text` function cleans up input text by removing newline and carriage return
    characters, reducing multiple spaces to single spaces, lowercasing the text and adjusting spacing around 
    certain characters like brackets, dots, colons, and equal signs. The goal of this function 
    is to return the most simple text that will later be analyzed. Therefore, it removes all 
    unnecessary spaces and indents (like spaces between ":" and "[") as according to the project guidelines, 
    they should be ignored. The text is converted to lower caps as according to the guide lines
    thos should also be ignored.
    
    :param text - string

    :return: string 
    """
    text = text.replace("\n", "").replace("\r", "")
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\s*([\[\]\.:=])\s*", r"\1", text)
    return text.lower()


def extract_nested_block(text, open_symbol, close_symbol, start_index):
    """
    The function extracts a nested block of text enclosed by specified open and close symbols starting
    from a given index in the input text. This function is central for the recursion, in order
    to find blocks within a block of text.
    
    :param text: string
    :param open_symbol: string - This symbol is used to identify the start of the nested block that needs 
    to be extracted
    :param close_symbol: string - used to specify the symbol that marks the end of a nested block within
    the given text
    :param start_index: int - index in the `text` string where the function should start looking for the nested block 
    defined by the `open_symbol`

    :return: bool | (string, int) - returns either the extracted nested block of text along
    with the index of the closing symbol, or `False` if a nested block is not found starting from the
    specified index in the input text
    """
    if not text.startswith(open_symbol, start_index):
        return False

    stack = [] 
    open_len = len(open_symbol)
    close_len = len(close_symbol)

    i = start_index 
    while i < len(text):
        if text.startswith(open_symbol, i):
            stack.append(i)  
            i += open_len  
        elif text.startswith(close_symbol, i):
            if stack:
                stack.pop() 
            if not stack:
                return text[start_index + open_len:i], i + close_len  
            i += close_len  
        else:
            i += 1 

    return False
