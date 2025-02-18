import structure as gen
import utils as u

#The purpose of this file is to implement simple functions that 
#return if a segment of text is a instruction

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

"""All of the following take in parameter a block of text, the variables and potential parameters
        and returns a boolean on wheter or not the text is a instruction of the type given by 
        the name of the function
"""

def is_variable_assignement (inst, variables, parameters): 
    n = len(inst)
    if not u.smthing_in_text(inst, 0, n, variables): 
        return False 
    
    i = u.smthing_in_text(inst, 0, n, variables)
    if inst[i:i+2] != ":=":
        return False 
    
    set = parameters + numbers
    if not u.smthing_in_text(inst, i+2, n, set): 
        return False 
    
    i = u.smthing_in_text(inst, i+2, n, set)

    return True

def is_goto (inst, variables): 
    n = len(inst)
    if inst[0:5] != "goto:": 
        return False
    
    i = 5
    set = variables + numbers
    if not u.smthing_in_text(inst, i, n, set): 
        return False 
    
    i = u.smthing_in_text(inst, i, n, set)
    if inst[i:i+6] != " with:": 
        return False 
    
    i = i+6
    if not u.smthing_in_text(inst, i, n, set): 
        return False 
    
    i = u.smthing_in_text(inst, i, n, set)
    return True

def is_move_simple(inst, variables): 
    n = len(inst)
    if inst[0:5] != "move:": 
        return False
    
    i = 5

    set = variables + ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    if not u.smthing_in_text(inst, i, n, set): 
        return False
    i = u.smthing_in_text(inst, i, n, set)
    return True

def is_turn(inst): 
    n = len(inst)
    if inst[0:5] != "turn:": 
        return False 
    
    if not u.smthing_in_text(inst, 5, n, gen.turns): 
        return False 
    
    i = u.smthing_in_text(inst, 5, n, gen.turns)
    return True
    
def is_face(inst): 
    n = len(inst)
    if inst[0:5] != "face:":
        return False 
    
    if not u.smthing_in_text(inst, 5, n, gen.cardinals): 
        return False 
    
    i = u.smthing_in_text(inst, 5, n, gen.cardinals)
    return True

def is_put(inst, variables): 
    n = len(inst)
    if inst[0:4] != "put:":
        return False 
    
    set = variables + numbers
    if not u.smthing_in_text(inst, 4, n, set): 
        return False 
    
    i = u.smthing_in_text(inst, 4, n, set)
    if inst[i:i+8] != " oftype:":
        return False 
    
    if not u.smthing_in_text(inst, i+8, n, gen.types): 
        return False 
    
    i = u.smthing_in_text(inst, i+8, n, gen.types)
    return True

def is_pick(inst, variables):
    n = len(inst)
    if inst[0:5] != "pick:":
        return False 
    
    set = variables + numbers
    if not u.smthing_in_text(inst, 5, n, set): 
        return False 
    
    i = u.smthing_in_text(inst, 5, n, set)
    if inst[i:i+8] != " oftype:":
        return False 
    
    if not u.smthing_in_text(inst, i+8, n, gen.types): 
        return False 
    
    i = u.smthing_in_text(inst, i+8, n, gen.types)
    return True 

def is_move_dir(inst, variables):
    n = len(inst)
    if inst[0:5] != "move:":
        return False 
    
    set = variables + numbers
    if not u.smthing_in_text(inst, 5, n, set): 
        return False 
    
    i = u.smthing_in_text(inst, 5, n, set)
    if inst[i:i+7] != " tothe:":
        return False 
    
    if not u.smthing_in_text(inst, i+7, n, gen.direction): 
        return False 
    
    i = u.smthing_in_text(inst, i+7, n, gen.direction)
    return True

def is_move_card(inst, variables):
    n = len(inst)
    if inst[0:5] != "move:":
        return False 
    
    set = variables + numbers
    if not u.smthing_in_text(inst, 5, n, set): 
        return False 
    
    i = u.smthing_in_text(inst, 5, n, set)
    if inst[i:i+7] != " indir:":
        return False 
    
    if not u.smthing_in_text(inst, i+7, n, gen.cardinals): 
        return False 
    
    i = u.smthing_in_text(inst, i+7, n, gen.cardinals)
    return True

def is_jump_dir(inst, variables): 
    n = len(inst)
    if inst[0:5] != "jump:":
        return False 
    
    set = variables + numbers
    if not u.smthing_in_text(inst, 5, n, set): 
        return False 
    
    i = u.smthing_in_text(inst, 5, n, set)
    if inst[i:i+7] != " tothe:":
        return False 
    
    if not u.smthing_in_text(inst, i+7, n, gen.direction): 
        return False 
    
    i = u.smthing_in_text(inst, i+7, n, gen.direction)
    return True

def is_jump_card(inst, variables):
    n = len(inst)
    if inst[0:5] != "jump:":
        return False 
    
    set = variables + numbers
    if not u.smthing_in_text(inst, 5, n, set): 
        return False 
    
    i = u.smthing_in_text(inst, 5, n, set)
    if inst[i:i+7] != " indir:":
        return False 
    
    if not u.smthing_in_text(inst, i+7, n, gen.cardinals): 
        return False 
    
    i = u.smthing_in_text(inst, i+7, n, gen.cardinals)
    return True

def is_nop(inst): 
    return inst == "nop"

def is_proc_call(inst, variables, proc_dic): 
    n = len(inst)
    for proc_name in proc_dic: 
        its_that_proc = True
        if proc_dic[proc_name][1] == []: 
            if inst[:len(proc_name)] == proc_name: 
                return True
            else: 
                continue
        i = 0
        k = 0
        titles = [proc_name]
        titles += proc_dic[proc_name][1]
        m = len(titles)
        while k<m and its_that_proc: 
            title = titles[k]
            l = len(title)
            if inst[i:i+l] != title or inst[i+l:i+1+l] != ":": 
                its_that_proc = False 
                continue
            i += l+1
            set = variables + numbers
            if not u.smthing_in_text(inst, i, n, set): 
                its_that_proc = False 
                continue
            i = u.smthing_in_text(inst, i, n, set)
            if k == m-1: 
                return True 
            else: 
                if inst[i] != " ": 
                    its_that_proc = False 
                else: 
                    i +=1
                    k+=1
        if its_that_proc: 
            return True
    
    return False
        
