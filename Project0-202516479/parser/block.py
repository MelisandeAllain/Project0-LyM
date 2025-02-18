import structure as gen 
import read_file as rd
import utils as u 

#This file holds the central function for the parser: is_block 
#It is a recursive function that allows to do a search of a text in order to find out if it is a block of instructions


def is_block(block, all_variables, parameters, proc_dic): 
    """
    The function `is_block` checks if a given block of code contains loops (like ifs, whiles or for) 
    or valid instructions.
    
    :param block: string - block to analyze
    :param all_variables: list - collection of all the variables that are
    accessible before getting to the code block being analyzed. These variables can include global
    variables, local variables
    :param parameters: list - arguments that can be used if the block is within a procedure
    :param proc_dic: dic - contains information about procedures already seen before 

    :return: boolean - indicating whether the given block of code is a valid block
    """
    try: 
        loop = u.try_multiple_functions(block, all_variables, parameters, proc_dic, gen.is_for, gen.is_if, gen.is_while)
    except: 
        loop = False 
    if not loop: 
        segments = rd.split_text_by_symbol(block)
        for segment in segments: 
            segment.strip()
            if gen.is_instruction(segment, all_variables, parameters, proc_dic):
                continue
            else:
                try:
                    return is_block(segment, all_variables, parameters, proc_dic)
                except Exception as e: 
                    print("This segment does not make sense", segment)
                    return False                  
    return True

