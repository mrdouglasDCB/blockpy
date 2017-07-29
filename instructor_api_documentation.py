def compliment(message):
    '''
    Adds message to the list of complimentary feedback.
    
    Args:
        message (str): The text string to display to the user in the Feedback 
                       panel as complimentary feedback. This will appear as 
                       a tooltip.
        
    '''

def set_success():
    '''
    Marks the problem as completely correct. This immediately ends execution 
    by throwing a GracefulExit exception.
    '''

def explain(message, priority="medium", line=None):
    '''
    Gives student the message as corrective feedback (and higlights line 
    number). If this function is called multiple times, the student is given the
    first feedback of the highest priority found.
    
    Args:
        message (str): The HTML string to display to the user in the Feedback
                       panel as corrective feedback. 
		priority (str): Either "low", "medium", or "high", indicating the
                        ordering of the feedback if multiple occur.
		line (int): The specific line number to highlight for the user.
    '''

def suppress(type, subtype):
    '''
    Suppresses feedback of the given "type".  When also given a subtype, it
    instead suppresses the subtype (which is typically a specific error message
    or type of exception). Multiple subtypes can be specified with multiple
    calls, each call suppressing additional feedback.
    
    Args:
        type (str): Either 'verifier', 'parser', 'analyzer', or 'student',
                    corresponding to the phase of execution feedback that will
                    be suppressed.
        subtype (str): A specific type of exception (if 'student') or
                       specific type of issue (if 'analyzer'). Available issues:
                        - 'Unconnected blocks'
                        - 'Iteration variable is iteration list'
                        - "Undefined variables"
                        - "Possibly undefined variables"
                        - "Unread variables"
                        - "Overwritten variables"
                        - "Empty iterations"
                        - "Non-list iterations"
                        - "Incompatible types"
    '''
    
def run_student():
    '''
    Reruns the students' submitted code ("__main__") as a function call.
    This allows the instructor to run the student code under new conditions.
    After a call to run_student(), the instructor will most likely want
    to use get_output() or some other function to access the new state.
    If the students' code failed to parse, then the body is instead replaced
    with "pass" to prevent compilation errors.
    '''

def get_output():
    '''
    Returns a List containing the students' output. This can be used 
    '''
    
def reset_output():
    '''
    '''
    
	def get_output()
		description: returns an array containing the student's output (if anything to console) as a string,
			or an array of numbers in the case of plotting
	def log(messsage)
		description: prints message to the javascript console
	class AST()
		description: prints the AST to the javascript console
	class Types()
		description: prints the student program type information to the javascript console
	class Behavior()
		description: prints the Abstract interpretor behavior information to the javascript console
	class Trace()
		description: prints the student trace information to the javascript console
	class Issues
		description: prints the Abstract interpretor issues information to the javascript console
	class StudentData()
		description: ???
	def set_feedback(message) @deprecated
		description: throws an exception as an internal error and prints feedback to the student
	def set_finished()
		description: throws an exception and grades the student's code as correct?
	def get_value_by_name(name)
		description: ???
	def get_value_by_type(type)
		description: ???
	def parse_json(blob)
		description: ???
	def get_property(name)
		description: ???
	def calls_function(source, name)
		source: 
		name: 
		description: ???
	def count_components(source, component)
		source: 
		component: 
		description: ???
	def no_nonlist_nums(source)
		description: ???
	def only_printing_properties(source)
		description: ???
	def parse_program()
		description: returns the root node of the AST of the student code as an AstNode.
			see class AstNode
	def add_interrupt_feedback(feedback)
		description: adds feedback to an internal javascript list of feedback that
			can be posted to the javascript console when post_feedback is called
	def add_comp_feedback(feedback)
		description: adds feedback to an internal javascript list of feedback that
			can be posted to the javascript console when post_feedback is called
	def post_feedback()
		description: outputs to the javascript console all feedback given with 
			add_interrupt_feedback and add_comp_feedback
	def def_use_error(node)
		description: if node is an AST Name node and variable has not been initialized
			returns false, otherwise returns true
	class AstNode
		def __init__(self, id)
			description: This should NOT be used by an instructor, this is strictly used internally to
				match up with the already parsed Skulpt AST. "id" is used as the index for the AST node
				when doing an in-order traversal of the tree
		def __eq__(self, other)
			description: if other is an AstNode, checks whether they are the same AstNode.  If both nodes
				originate from the same AST, then a return true will indicate it is the same node, and false
				will indicate it's a different node. If it's not an AstNode, this will crash the program
		def has(self, astNode)
			description: returns true astNode is a Name astNode, or a number, AND if it is in the subtree of this node
		def find_all(self, type)
			type: a string denoting an AST node, e.g. "For", "Assign", "BinOp", etc.
			description: returns all AstNodes in this node's subtrees that are an ast Node of type
		data_type
			if this node is a Name node, returns the first data type that this variable has taken on
		ast_name
			returns the type of ast node this node (e.g. Name, For, Assign, etc.)
		Types of AST Nodes See greentree snakes API, which closely mimics our nodes, with some notable exceptions noted below
			Assign
				right now, Assign.targets returns a SINGLE AstNode instead of an array of AstNodes
			For nodes with ops, only returns the FIRST operator, so no comparison operator chaining

