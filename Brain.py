print("brain world!")

HELLO_WORLD = """[ This program prints "Hello World!" and a newline to the screen, its
  length is 106 active command characters. [It is not the shortest.]

  This loop is an "initial comment loop", a simple way of adding a comment
  to a BF program such that you don't have to worry about any command
  characters. Any ".", ",", "+", "-", "<" and ">" characters are simply
  ignored, the "[" and "]" characters just have to be balanced. This
  loop and the commands it contains are ignored because the current cell
  defaults to a value of 0; the 0 value causes this loop to be skipped.
]
++++++++               Set Cell #0 to 8
[
    >++++               Add 4 to Cell #1; this will always set Cell #1 to 4
    [                   as the cell will be cleared by the loop
        >++             Add 2 to Cell #2
        >+++            Add 3 to Cell #3
        >+++            Add 3 to Cell #4
        >+              Add 1 to Cell #5
        <<<<-           Decrement the loop counter in Cell #1
    ]                   Loop until Cell #1 is zero; number of iterations is 4
    >+                  Add 1 to Cell #2
    >+                  Add 1 to Cell #3
    >-                  Subtract 1 from Cell #4
    >>+                 Add 1 to Cell #6
    [<]                 Move back to the first zero cell you find; this will
                        be Cell #1 which was cleared by the previous loop
    <-                  Decrement the loop Counter in Cell #0
]                       Loop until Cell #0 is zero; number of iterations is 8
"""

# setup a model for the interpreter
# Interpreter {
# 	ptr : int
# 	memory : List[int]
# }


# the algorithm itself

# How to run a program

# loop over the characters in the string

	# if the given character is not one of the valid characters it can be ignored
	
	# if character equaals '>"
		# increment the Interpreters pointer
		
	# if character equals "<"
		# decrement the Interpreters pointer
	
	# if character equals "+"
		# increment the Memory cell at Interpreter pointer
	
	# if character equals "-"
		# decrement the Memory cell at Interpreter pointer	
	
	# if character equals "."
		# output the byte at the Interpreter pointer as ASCII
	
	# if character equals ","at Interpreters datapointer
		# take one byte input that is stored in memory at Interpreter Pointer
		
	# if character equals "["
		# if the byte in memory at Interpreter datapointer is 0 jump to 1 char after the matching ] command
	# if character equls "]"
		# if the byte in memory at Interpreter datapointer != 0 jump back to 1 char after the matching [ command
		
# At the end of the program I should check if the two lists of
# expected outputs match with the first n values in the memory arrray
def run(program : str) -> list[int]:
	"run a program returning the memory_state in list"
	raise NotImplementedError("Not Yet run()!")

	
def start_of_list_equals(x, y):
	return x == y

def is_zero(x):
	return x == 0


def test(program : str, expected : list[int]) -> bool:
	given = run(program)
	# see if the given list does not spill over values beyond the expected values set.
	cut_given = given[:len(expected)]
	spill_list = given[len(expected):]
	assert all(map(is_zero, spill_list)), "There was a spill of values in spill_list"
	
	return all(map(start_of_list_equals, cut_given, expected))

assert test("+++", [3]), "Simple add does not work!"
