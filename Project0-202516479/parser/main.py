import structure as gen
import conditions as cd
import instructions as inst
import read_file as rd
import utils as u
import block as bk

#Main function: function to execute in order to get the parser of a text file
#The function is called with the code corresponding to the one given in 
#the guidelines of correct code for the project (file: "code.txt")
#If after being executed, it prints "The code is correct ! " then the code is valid
#Otherwise, it prints "The code is incorrect" and the error that caused the failure

def main(filename):
    """
    The main function reads code from a file, processes it to check for correct structure and syntax,
    and returns True if the code is correct.
    
    :param filename: text file (it has to be .txt) to parse
    :return: boolean  - True if the code is correct and False if
    there are any errors detected during the processing of the code.
    """
    with open(filename, "r", encoding="utf-8") as file:
        print("Here is the given code:")
        code = file.read()
        print(code)
        print("Result:")
        g = gen.var_declaration(code, "g")
        if not g: 
                (global_var, indice) = ([], 0)
        else: 
            (global_var, indice) = g
        code = rd.clean_text(code)
        procs = {}
        while indice< len(code):
            p = gen.is_proc_declaration(code, indice)
            if p != False: 
                try: 
                    (proc_name, parameters, and_types, indice) = gen.is_proc_declaration(code, indice)
                    bi = rd.extract_nested_block(code, "[", "]", indice)
                    if bi == False: 
                        print("The code is incorrect")
                        print("The structure for the", proc_name, " procedure is wrong")
                        return False
                    (block, indice) = bi
                    block = rd.clean_text(block)
                    try: 
                        b = gen.is_proc_block(block, global_var, parameters, procs)
                        if b!= False: 
                            procs[proc_name] = [parameters, and_types]
                        else: 
                            print("The code is incorrect")
                            print("The block inside the procedure ", proc_name, " is invalid")
                            return False
                    except: 
                        print("The code is incorrect")
                        print("The block inside the procedure ", proc_name, " is invalid")
                        return False
                except: 
                    print("The code is incorrect")
                    print("The block inside the procedure ", proc_name, " is invalid")
                    return False
            else:    
                try: 
                    bi = rd.extract_nested_block(code, "[", "]", indice)
                    if bi == False: 
                        print("The code is incorrect")
                        print("The structure", code[indice:],"does not correspond to either a block or a procedure")
                        return False
                    (block, indice) = bi
                    block = rd.clean_text(block)
                    try: 
                        b = bk.is_block(block, global_var, [], procs)
                        if b!= False: 
                            continue
                        else: 
                            print("The code is incorrect")
                            print("The block ", block, " is invalid")
                            return False
                    except: 
                        print("The code is incorrect")
                        print("The block  ", proc_name, " is invalid")
                        return False
                except: 
                    print("The code is incorrect")
                    print("The block ", block, " is invalid")
                    return False
        print("The code is correct ! ")
        return True

filename = "code.txt"           
main(filename)





