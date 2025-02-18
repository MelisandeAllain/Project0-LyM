
import structure as gen
import instructions as inst
import conditions as cd
import block as bk
import utils as u
import read_file as rd
import main as main 

#This file is just a set of primary tests on the functions that are used in the parser, in order to verify that 
#everything was correct 
#It uses the files block.txt,  if.txt and test.txt
#The "test.txt" file was made by me inspired by the given file with a few variations (loops within loops, other 
# instructions, for) to test the parser

#test instructions
print("INSTRUCTIONS")
print("variable:", inst.is_variable_assignement("t1:=3 .", ["t1"], [] ))
print("goto:", inst.is_goto("goto:1 with:5 .", []))
print("move simple:",inst.is_move_simple("move:t1 .", ["t1"]))
print("turn:", inst.is_turn("turn:#left ."))
print("face:", inst.is_face("face:#north ."))
print("put:", inst.is_put("put:t1 oftype:#balloons .", ["t1"]))
print("put:", inst.is_put("put:c oftype:#chips", ["c"]))
print("pick:", inst.is_pick("pick:4 oftype:#balloons .", []))
print("move dir:", inst.is_move_dir("move:t2 tothe:#right .", ["t2"]))
print("move car:", inst.is_move_card("move:t1 indir:#east .", ["t1"]))
print("jump dir:", inst.is_jump_dir("jump:t1 tothe:#left .", ["t1"]))
print("jump card:", inst.is_jump_card("jump:t2 indir:#east .", ["t2"]))
print("nop:", inst.is_nop("nop"))
print("____________________________________________")

#test conditions
print("____________________________________________")
print("CONDITIONS")
print("is facing:", cd.is_facing("facing:#north ."))
print("is move dir:", cd.is_canMove_dir("canmove:5 tothe:#right .", []))
print("is not:", cd.is_not("not: canput:6 oftype:#chips .", []))
print("____________________________________________")

# variable declaration
print("____________________________________________")
print("VARIABLE DECLARATIONS")
print("global var declaration:", gen.var_declaration("|nom x y one|", "g"))
print("local var declaration:", gen.var_declaration("|c, b|", "l"))
print("____________________________________________")

#blocks 
block_test = "block.txt"
with open(block_test, "r", encoding="utf-8") as file:
    block = file.read()
block = rd.clean_text(block)
print("____________________________________________")
print("BLOCK")
print("block:", bk.is_block(block, ["c"], [], {}))
print("____________________________________________")


#if 
if_test = "if.txt"
with open(if_test, "r", encoding="utf-8") as file:
    if_block = file.read()
if_block = rd.clean_text(if_block)
print("____________________________________________")
print("IF")
print("if:", gen.is_if(if_block, [], [], {}))
print("____________________________________________")

#procurations
#procuration declaration
print("____________________________________________")
print("Procedure declaration")
print("is proc declaration:", gen.is_proc_declaration("proc putchips:n and:k andok:z and:m[", 0))
(proc_name, param, ands, i) = gen.is_proc_declaration("proc putchips:n and:k andok:z and:m[", 0)
print("____________________________________________")

#for 
print("____________________________________________")
print("FOR")
print("is for:", gen.is_for("for:3 repeat:[move:1 indir:#west]", [], [], {}))
print("____________________________________________")


#code 
print("____________________________________________")
print("CODE TEST")
print(main.main("test.txt"))