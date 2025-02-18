import structure as gen
import utils as u

#The purpose of this file is to implement simple functions that 
#return if a segment of text is a condition

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

"""All of the following take in parameter a block of text, the variables and potential parameters
        and returns a boolean on wheter or not the text is a condition of the type given by 
        the name of the function
"""

def is_facing(inst):
    n = len(inst)
    if inst[0:7] != "facing:":
        return False 
    
    if not u.smthing_in_text(inst, 7, n, gen.cardinals): 
        return False 
    
    #i = u.smthing_in_text(inst, 8, n, main.cardinals)
    #return u.ends_point(inst, i)
    return True

def is_canPut(inst, variables): 
    n = len(inst)
    if inst[0:7] != "canput:":
        return False 
    
    set = variables + numbers
    if not u.smthing_in_text(inst, 7, n, set): 
        return False 
    
    i = u.smthing_in_text(inst, 7, n, set)
    if inst[i:i+8] != " oftype:":
        return False 
    
    if not u.smthing_in_text(inst, i+8, n, gen.types): 
        return False 
    
    i = u.smthing_in_text(inst, i+8, n, gen.types)
    #return u.ends_point(inst, i)
    return True


def is_canPick(inst, variables):
    n = len(inst)
    if inst[0:8] != "canpick:":
        return False 
    
    set = variables + numbers
    if not u.smthing_in_text(inst, 8, n, set): 
        return False 
    
    i = u.smthing_in_text(inst, 8, n, set)
    if inst[i:i+8] != " oftype:":
        return False 
    
    if not u.smthing_in_text(inst, i+8, n, gen.types): 
        return False 
    
    i = u.smthing_in_text(inst, i+8, n, gen.types)
    #return u.ends_point(inst, i)
    return True


def is_canMove_card(inst, variables): 
    n = len(inst)
    if inst[0:8] != "canmove:":
        return False 
    
    set = variables + numbers

    if not u.smthing_in_text(inst, 8, n, set): 
        return False 
    
    i = u.smthing_in_text(inst, 8, n, set)
    if inst[i:i+7] !=  " indir:":
        return False 
    if not u.smthing_in_text(inst, i+7, n, gen.cardinals): 
        return False 
    
    i = u.smthing_in_text(inst, i+7, n, gen.cardinals)
    #return u.ends_point(inst, i)
    return True


def is_canJump_card(inst, variables): 
    n = len(inst)
    if inst[0:9] != "canjump:":
        return False 
    
    set = variables + numbers

    if not u.smthing_in_text(inst, 8, n, set): 
        return False 
    
    i = u.smthing_in_text(inst, 8, n, set)
    if inst[i:i+7] != " indir:":
        return False 
    
    if not u.smthing_in_text(inst, i+7, n, gen.cardinals): 
        return False 
    
    i = u.smthing_in_text(inst, i+7, n, gen.cardinals)
    #return u.ends_point(inst, i)
    return True

def is_canMove_dir(inst, variables):
    n = len(inst)
    if inst[0:8] != "canmove:":
        return False 
    
    set = variables + numbers
    if not u.smthing_in_text(inst, 8, n, set): 
        return False 
    
    i = u.smthing_in_text(inst, 8, n, set)
    if inst[i:i+7] != " tothe:":
        return False 
    
    if not u.smthing_in_text(inst, i+7, n, gen.direction): 
        return False 
    
    i = u.smthing_in_text(inst, i+7, n, gen.direction)
    #return u.ends_point(inst, i)
    return True

def is_canJump_dir(inst, variables):
    n = len(inst)
    if inst[0:8] != "canjump:":
        return False 
    
    set = variables + numbers

    if not u.smthing_in_text(inst, 8, n, set): 
        return False 
    
    i = u.smthing_in_text(inst, 8, n, set)
    if inst[i:i+7] != " tothe:":
        return False 
    
    if not u.smthing_in_text(inst, i+7, n, gen.direction): 
        return False 
    
    i = u.smthing_in_text(inst, i+7, n, gen.direction)
    #return u.ends_point(inst, i)
    return True

def is_not(inst, variables): 
    n = len(inst)
    if inst[0:5] != "not: ":
        return False 
    
    reste = inst[5:]
    return (is_facing(reste) or is_canJump_card(reste, variables) or is_canJump_dir(reste, variables) or is_canMove_card(reste, variables)\
            or is_canMove_dir(reste, variables) or is_canPick(reste, variables) or is_canPut(reste, variables))

