import instructions as inst
import conditions as cd
import utils as u
import read_file as rd
import block as bk

#The purpose of this file is to implement important functions 
#to determine if the structure of the code is correct (if it hols normal instructions, conditions, ifs, 
# loops, procedures)

#Assignation 
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
turns = {"#left", "#right", "#around"}
cardinals = {"#north", "#south", "#west", "#east"}
direction = {"#front", "#right", "#left", "#back"}
types = {"#balloons", "#chips"}

def is_instruction(txt, variables, parameters, proc_dic): 
    """
    The function `is_instruction` checks if a given text represents a valid instruction based 
    on the functions given in the instructions.py file
    
    :param txt
    :param variables: list - stores the current state of variables in the
    program
    :param parameters: list - stores the current state of parameters in the
    program
    :param proc_dic: dic- stores the current state of procedures in the
    program

    :return: returns a boolean value based on whether the input text
    `txt` corresponds to any of the supported instruction types
    """
    return inst.is_variable_assignement(txt, variables, parameters) or inst.is_goto(txt, variables) or\
    inst.is_move_simple(txt, variables) or inst.is_turn(txt) or inst.is_turn(txt) or inst.is_face(txt) or \
    inst.is_put(txt, variables) or inst.is_pick(txt, variables) or inst.is_move_dir(txt, variables) or inst.is_move_card(txt, variables) or \
    inst.is_jump_dir(txt, variables) or inst.is_jump_card(txt, variables) or inst.is_nop(txt) or inst.is_proc_call(txt, variables, proc_dic)

def is_condition(txt, variables):
    """
    The function checks if a given text represents a valid condition based 
    on the functions given in the conditions.py file
    
    :param txt
    :param variables: list - stores the current state of variables in the
    program
    
    :return: returns a boolean value based on whether the input text
    `txt` corresponds to any of the supported conditions types
    """
    return cd.is_canJump_card(txt, variables) or cd.is_canJump_dir(txt, variables) or cd.is_canMove_card(txt, variables) or cd.is_canMove_dir(txt, variables)\
    or cd.is_canPick(txt, variables) or cd.is_canPut(txt, variables) or cd.is_facing(txt) or cd.is_not(txt, variables)

def var_declaration(txt, type):
    """
    The function `var_declaration` parses a text input to extract and return variables of a
    specified type (global or local).
    
    :param txt
    :param type: Wether the searched variables are global or local

    :return: either a list of  variables if the
    condition is met, or False
    """
    if txt[0] != "|": 
        return False
    
    else: 
        global_var = []
        i = 1
        while i< len(txt) and txt[i] != "|": 
            if u.find_var(txt, i, type) == False: 
                return global_var
            else:
                (var, indice) = u.find_var(txt, i, type)
                global_var.append(var)
                if txt[indice] == "|": 
                    return(global_var, indice+1)
                i = indice +1
        return False

def is_while(block, all_variables, parameters, procs):
    """
    The function checks if a given text represents a valid while based 
    on the functions given in the instructions.py file and the is_block function
    
    :param block
    :param all_variables: list - stores the current state of variables(global and local) in the
    program
    :param parameters: list - stores the current state of parameters in the
    program
    :param procs: dic- stores the current state of procedures in the
    program

    :return: returns a boolean value based on whether the input text
    `txt` corresponds to a valid while 
    """
    if block[:6] != "while:": 
        return False 
    if rd.extract_nested_block(block, "while:", "do:", 0) == False: 
        return False 
    (passage, i) = rd.extract_nested_block(block, "while:", "do:", 0)
    try: 
        bool = is_condition(passage, all_variables)
    except: 
        bool = False 
    if bool:
        try: 
            potential_block = rd.extract_nested_block(block, "[", "]", i)
            if potential_block == False: 
                return False
            else: 
                return bk.is_block(potential_block, all_variables, parameters, procs)
        except:
            return False
    
def is_for(block, all_variables, parameters, procs): 
    """
    The function checks if a given text represents a valid for based 
    on the functions given in the instructions.py file and the is_block function
    
    :param block
    :param all_variables: list - stores the current state of variables(global and local) in the
    program
    :param parameters: list - stores the current state of parameters in the
    program
    :param procs: dic- stores the current state of procedures in the
    program

    :return: returns a boolean value based on whether the input text
    `txt` corresponds to a valid for 
    """
    lines = block.splitlines()
    line = lines[0].strip()
    if line[:4] != "for:": 
        return False 
    try: 
        set = numbers + all_variables
        indice = u.smthing_in_text(line, 4, len(line), set)
        if indice == False: 
            return False 
    except: 
        return False 
    if line[indice:indice+8] != " repeat:":
        return False 
    try: 
        (potential_block, indice)  = rd.extract_nested_block(block, " repeat:[", "]", indice )
        if potential_block == False: 
                return False
        else: 
            return bk.is_block(potential_block, all_variables, parameters, procs)
    except:
        return False

def is_if(block, all_variables, parameters, procs): 
    """
    The function checks if a given text represents a valid if based 
    on the functions given in the instructions.py file and the is_block function
    
    :param block
    :param all_variables: list - stores the current state of variables(global and local) in the
    program
    :param parameters: list - stores the current state of parameters in the
    program
    :param procs: dic- stores the current state of procedures in the
    program

    :return: returns a boolean value based on whether the input text
    `txt` corresponds to a valid if 
    """
    block = rd.clean_text(block)
    lines = block.splitlines()
    line = lines[0].strip()
    if line[:3] != "if:": 
        return False 
    if rd.extract_nested_block(block, "if:", "then:", 0) == False: 
        return False 
    (passage, i) = rd.extract_nested_block(block, "if:", "then:", 0)
    try: 
        bool = is_condition(passage, all_variables)
        if bool == False: 
            return False
    except: 
        return False 
    try: 
        (potential_block, i) = rd.extract_nested_block(block, "[", "]", i)
        if potential_block == False: 
            return False
    except:
        return False
    try:
        b = bk.is_block(potential_block, all_variables, parameters, procs)
        if b == False: 
            return False 
    except: 
        return False 
    if block[i:i+4] != "else": 
        return False
    i+=4
    if block[i] != ":": 
        return False
    i+=1
    try: 
        (potential_block2, i) = rd.extract_nested_block(block, "[", "]", i)
        if potential_block2 == False: 
            return False
    except:
        return False
    try: 
        b2 = bk.is_block(potential_block2, all_variables, parameters, procs)
        if b2 == False: 
            return False 
        else: 
            return True
    except: 
        return False
    
def is_proc_declaration(txt, i): 
    """
    The function checks if a given text represents a valid procedure declaration 
    
    :param txt
    :param i: int - index from where the procedure declaration should start

    :return: returns False if not valid declaration or tuple with name, parameters, 
    ands of the procedure and the index where the declaration ends
    """
    if txt[i:i+5] != "proc ": 
        return False 
    
    if u.find_proc(txt, i+5) == False: 
        return False 
    
    (proc_name, indice, param) = u.find_proc(txt, i+5)
    and_types = []
    parameters = []
    if param: 
        if txt[indice: indice+1]!= ":": 
            return False 
        
        indice +=1
        is_next = True
        while is_next:
            if  u.find_param(txt, indice) == False: 

                return False 
            
            (para, i) = u.find_param(txt, indice)
            parameters.append(para)
            indice = i
            if txt[indice] == "[": 
                return (proc_name, parameters, and_types, indice)
            else: 
                indice = i +1
                if u.and_in_text(txt, indice) == False:
                    return False
                else: 
                    (indice, and_type) = u.and_in_text(txt, indice)
                    and_types.append(and_type)
    else: 
        return (proc_name, parameters, and_types, indice)

def is_proc_block(block, glob_var, parameters, procs):
    """
    The function checks if a given block represents a valid procedure block based on its parameters
    and the procedures that were already declared before. First it serached for local variables of the 
    procedure
    
    :param block
    :param glob_var - list of globally declared vairables
    :procs - dic of previsoulsy declared procedures

    :return: returns boolean on whetheror not is a valid procedure block 
    """ 
    i = 0
    try: 
        lo= var_declaration(block, "l") 
        if lo== False: 
            local_variables = []
        else: 
            (local_variables, i)= lo
    except: 
        local_variables = []
    all_variables = local_variables + glob_var 
    potential_block = block[i:]
    potential_block= rd.clean_text(potential_block)
    return bk.is_block(potential_block, all_variables, parameters, procs )


    
    

    



