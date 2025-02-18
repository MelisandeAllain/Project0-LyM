import structure as main


#The purpose of this file is to implement useful functions, for example to 
#find specific words that are part of a set (like variables for example)

def smthing_in_text(txt, indice, n, set): 
    """
    This function takes a text, starting index, ending index, and a set of words (of things), 
    and returns the index of the next word in the text that matches a word in the set (a something)
    
    :param txt: string - the text with the potential 'something'
    :param indice:  starting index in the text from where you want to extract a 'something' 
    :param n: total length of the text 
    :param set: set - set of things the 'something' should be a part of 

    :return: `False` if the something does not exist  or the updated value of `indice`, the index
    """
    t = ""
    if indice == n or indice>n: 
        return False
    while indice<n and txt[indice] != " " and txt[indice] != ":" and txt[indice] != "." and txt[indice] != "["\
        and txt[indice] != "[": 
        t += (txt[indice]) 
        indice+=1
    if not t in set: return False 

    else: return indice 

def and_in_text(txt, indice): 
    """
    Same as before but specifically for 'and' types in procedure declarations
    
    :param txt
    :param indice: the index position in where the function should start looking for the word "and"

    :return: tuple containing the index of the character after the
    colon (after the 'and') or False
    """
    t = ""
    n = len(txt)
    if indice == n or indice>n or txt[indice] == ":": 
        return False
    while txt[indice] != ":" and indice<n-1: 
        if txt[indice] == " ":
            return False
        t += (txt[indice]) 
        indice+=1
    return (indice +1, t)
    
def find_var(txt, indice, type): 
    """
    Same as before but specifically for 'variables' 
    
    :param txt
    :param indice: the index position in where the function should start looking for the variable
    :param type: "l" for local and "g" for global as it seems global variable are separated by space
    whereas local are separated by comas ","

    :return: tuple containing the index of the character after the
    colon (after the variable) or False
    """
    var = ""
    if txt[indice] == "|": return False
    while txt[indice] != " " and txt[indice] != "|": 
        var +=(txt[indice])
        indice+=1

    if var[-1] == ",": 
        if type == "g":
            return False
        elif type == "l": 
            var = var[:-1]
    return (var, indice)

def find_proc(txt, indice): 
    """
    Same as before but specifically for 'proc' in procedure declarations
    
    :param txt
    :param indice: the index position in where the function should start looking for the word "proc"

    :return: tuple containing the index of the character after the
     proc or False
    """
    var = ""
    if txt[indice] == ":": return False
    while txt[indice] != ":" and txt[indice] != "[": 
        var +=(txt[indice])
        indice+=1
    if txt[indice] == ":": 
        param = True
    else: 
        param = False
    return (var, indice, param)

def find_param(txt, indice): 
    """
    Same as before but specifically for parameters in procedure declarations
    
    :param txt
    :param indice: the index position in where the function should start looking for the parameter

    :return: tuple containing the index of the character after the parameter or False
    """
    var = ""
    if txt[indice] == " ": return False
    while txt[indice] != " " and txt[indice] != "[": 
        var +=(txt[indice])
        indice+=1
    return (var, indice)


def try_multiple_functions(segment, all_variables, parameters, procs, *functions):
    """
    The function `try_multiple_functions` iterates through a list of functions and attempts to execute
    each one with given parameters until one of them returns a non-False value.
    
    :param segment: string - that is being processed or analyzed
    within the context of the functions being called
    :param all_variables: list -  all the variables needed for the procedures to operate
    :param parameters: list  - all the parameters needed for the procedures to operate
    :param procs: dic -  collection of procedures or functions that can be called within the functions 
    given in parameter

    :return: boolean - return `True` if any of the functions provided
    as arguments return a result that is not equal to `False`. If all functions return `False` or if an
    exception is raised during the execution of any function, the function will return `False`.
    """
    for func in functions:
        try:
            result = func(segment, all_variables, parameters, procs)
            if result != False: 

                return True
            else: 
                continue 
        except Exception as e:
            continue  
    return False


