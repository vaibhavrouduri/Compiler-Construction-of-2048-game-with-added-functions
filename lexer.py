from sly import Lexer

class BasicLexer(Lexer):
	tokens = {ADD, SUBTRACT, MULTIPLY, DIVIDE, UP, DOWN, LEFT, RIGHT, ASSIGN, TO, IS, NUMBER, NAME, IN, VALUE}
	ignore = '\t '

	literals = {'.', ','}

	ADD = r'ADD'
	SUBTRACT = r'SUBTRACT'
	MULTIPLY = r'MULTIPLY'
	DIVIDE = r'DIVIDE'
	UP = r'UP'
	DOWN = r'DOWN'
	LEFT = r'LEFT'
	RIGHT = r'RIGHT'
	ASSIGN = r'ASSIGN'
	TO = r'TO'
	IS = r'IS'
	IN = r'IN'
	VALUE = r'VALUE'
	NAME = r'[a-zA-Z_][a-zA-Z0-9_]*' 

	@_(r'\d+')
	def NUMBER(self, t):
		t.value = int(t.value)
		return t

	@_(r'#.*')
	def COMMENT(self, t):
		pass

	@_(r'\n+')
	def newline(self, t):
		self.lineno = t.value.count('\n')

# if __name__ == '__main__':
# 	lexer = BasicLexer()
# 	env = {}
# 	while True:
# 		try:
# 			text = input('2048 > ')
# 		except EOFError:
# 			break
# 		if text:
# 			lex = lexer.tokenize(text)
# 			for token in lex:
# 				print(token)
