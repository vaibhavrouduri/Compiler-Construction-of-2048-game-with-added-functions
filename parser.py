from lexer import *
from sly import Parser
import random
import sys

stdout_fileno = sys.stdout
stderr_fileno = sys.stderr


def add_new_tile(mat):
  r = random.randint(0, 3)
  c = random.randint(0, 3)

  while(mat[r][c] != 0):
    r = random.randint(0, 3)
    c = random.randint(0, 3)

  mat[r][c] = random.randrange(2, 5, 2)

def assign(mat, r, c, x):
  mat[r-1][c-1] = x
  printState(mat)
  current_state = mat
  return 0

def initialize():
  mat = []
  for i in range(4):
    mat.append([0] * 4)

  add_new_tile(mat)
  printState(mat)
  return mat

def printState(state):
  for i in state:
    print(i, end = ' ')
    print()

def compress(mat):

  changed = False

  new_mat = []

  for i in range(4):
    new_mat.append([0] * 4)

  for i in range(4):
    pos = 0
    for j in range(4):
      if(mat[i][j] != 0):
        new_mat[i][pos] = mat[i][j]

        if(j != pos):
          changed = True
        pos += 1
  
  return new_mat, changed

def merge_add(mat):

  changed = False

  for i in range(4):
    for j in range(3):
      if(mat[i][j] == mat[i][j+1] and mat[i][j] != 0):
        mat[i][j] = mat[i][j] * 2
        mat[i][j + 1] = 0

        changed = True
  return mat, changed

def merge_subtract(mat):

  changed = False

  for i in range(4):
    for j in range(3):
      if(mat[i][j] == mat[i][j+1] and mat[i][j] != 0):
        mat[i][j] = 0
        mat[i][j + 1] = 0

        changed = True
  return mat, changed

def merge_multiply(mat):

  changed = False

  for i in range(4):
    for j in range(3):
      if(mat[i][j] == mat[i][j+1] and mat[i][j] != 0):
        mat[i][j] = mat[i][j] * mat[i][j]
        mat[i][j + 1] = 0

        changed = True
  return mat, changed

def merge_divide(mat):

  changed = False

  for i in range(4):
    for j in range(3):
      if(mat[i][j] == mat[i][j+1] and mat[i][j] != 0):
        mat[i][j] = 1
        mat[i][j + 1] = 0

        changed = True
  return mat, changed

def reverse(mat):
  new_mat = []
  for i in range(4):
    new_mat.append([])
    for j in range(4):
      new_mat[i].append(mat[i][3 - j])
  return new_mat

def transpose(mat):
  new_mat = []
  for i in range(4):
    new_mat.append([])
    for j in range(4):
      new_mat[i].append(mat[j][i])
  return new_mat

def move_left_add(grid):
  global current_state
  new_grid, changed1 = compress(grid)
  new_grid, changed2 = merge_add(new_grid)
  changed = changed1 or changed2
  new_grid, temp = compress(new_grid)
  add_new_tile(new_grid)
  printState(new_grid)
  current_state = new_grid
  return new_grid, changed

def move_left_subtract(grid):
  global current_state
  new_grid, changed1 = compress(grid)
  new_grid, changed2 = merge_subtract(new_grid)
  changed = changed1 or changed2
  new_grid, temp = compress(new_grid)
  add_new_tile(new_grid)
  printState(new_grid)
  current_state = new_grid
  return new_grid, changed

def move_left_multiply(grid):
  global current_state
  new_grid, changed1 = compress(grid)
  new_grid, changed2 = merge_multiply(new_grid)
  changed = changed1 or changed2
  new_grid, temp = compress(new_grid)
  add_new_tile(new_grid)
  printState(new_grid)
  current_state = new_grid
  return new_grid, changed

def move_left_divide(grid):
  global current_state
  new_grid, changed1 = compress(grid)
  new_grid, changed2 = merge_divide(new_grid)
  changed = changed1 or changed2
  new_grid, temp = compress(new_grid)
  add_new_tile(new_grid)
  printState(new_grid)
  current_state = new_grid
  return new_grid, changed

def move_left_add_without_printing(grid):
  global current_state
  new_grid, changed1 = compress(grid)
  new_grid, changed2 = merge_add(new_grid)
  changed = changed1 or changed2
  new_grid, temp = compress(new_grid)
  add_new_tile(new_grid)
  return new_grid, changed

def move_right_add(grid):
  global current_state
  new_grid = reverse(grid)
  new_grid, changed = move_left_add_without_printing(new_grid)
  new_grid = reverse(new_grid)
  printState(new_grid)
  current_state = new_grid
  return new_grid, changed

def move_left_subtract_without_printing(grid):
  global current_state
  new_grid, changed1 = compress(grid)
  new_grid, changed2 = merge_subtract(new_grid)
  changed = changed1 or changed2
  new_grid, temp = compress(new_grid)
  add_new_tile(new_grid)
  return new_grid, changed

def move_right_subtract(grid):
  global current_state
  new_grid = reverse(grid)
  new_grid, changed = move_left_subtract_without_printing(new_grid)
  new_grid = reverse(new_grid)
  printState(new_grid)
  current_state = new_grid
  return new_grid, changed

def move_left_multiply_without_printing(grid):
  global current_state
  new_grid, changed1 = compress(grid)
  new_grid, changed2 = merge_multiply(new_grid)
  changed = changed1 or changed2
  new_grid, temp = compress(new_grid)
  add_new_tile(new_grid)
  return new_grid, changed

def move_right_multiply(grid):
  global current_state
  new_grid = reverse(grid)
  new_grid, changed = move_left_multiply_without_printing(new_grid)
  new_grid = reverse(new_grid)
  printState(new_grid)
  current_state = new_grid
  return new_grid, changed

def move_left_divide_without_printing(grid):
  global current_state
  new_grid, changed1 = compress(grid)
  new_grid, changed2 = merge_divide(new_grid)
  changed = changed1 or changed2
  new_grid, temp = compress(new_grid)
  add_new_tile(new_grid)
  return new_grid, changed

def move_right_divide(grid):
  global current_state
  new_grid = reverse(grid)
  new_grid, changed = move_left_divide_without_printing(new_grid)
  new_grid = reverse(new_grid)
  printState(new_grid)
  current_state = new_grid
  return new_grid, changed

def move_up_add(grid):
  global current_state
  new_grid = transpose(grid)
  new_grid, changed = move_left_add_without_printing(new_grid)
  new_grid = transpose(new_grid)
  printState(new_grid)
  current_state = new_grid
  return new_grid, changed

def move_up_subtract(grid):
  global current_state
  new_grid = transpose(grid)
  new_grid, changed = move_left_subtract_without_printing(new_grid)
  new_grid = transpose(new_grid)
  printState(new_grid)
  current_state = new_grid
  return new_grid, changed

def move_up_multiply(grid):
  global current_state
  new_grid = transpose(grid)
  new_grid, changed = move_left_multiply_without_printing(new_grid)
  new_grid = transpose(new_grid)
  printState(new_grid)
  current_state = new_grid
  return new_grid, changed

def move_up_divide(grid):
  global current_state
  new_grid = transpose(grid)
  new_grid, changed = move_left_divide_without_printing(new_grid)
  new_grid = transpose(new_grid)
  printState(new_grid)
  current_state = new_grid
  return new_grid, changed

def move_right_add_without_printing(grid):
  global current_state
  new_grid = reverse(grid)
  new_grid, changed = move_left_add_without_printing(new_grid)
  new_grid = reverse(new_grid)
  return new_grid, changed

def move_down_add(grid):
  global current_state
  new_grid = transpose(grid)
  new_grid, changed = move_right_add_without_printing(new_grid)
  new_grid = transpose(new_grid)
  printState(new_grid)
  current_state = new_grid
  return new_grid, changed

def move_right_subtract_without_printing(grid):
  global current_state
  new_grid = reverse(grid)
  new_grid, changed = move_left_subtract_without_printing(new_grid)
  new_grid = reverse(new_grid)
  return new_grid, changed

def move_down_subtract(grid):
  global current_state
  new_grid = transpose(grid)
  new_grid, changed = move_right_subtract_without_printing(new_grid)
  new_grid = transpose(new_grid)
  printState(new_grid)
  current_state = new_grid
  return new_grid, changed

def move_right_multiply_without_printing(grid):
  global current_state
  new_grid = reverse(grid)
  new_grid, changed = move_left_multiply_without_printing(new_grid)
  new_grid = reverse(new_grid)
  return new_grid, changed

def move_down_multiply(grid):
  global current_state
  new_grid = transpose(grid)
  new_grid, changed = move_right_multiply_without_printing(new_grid)
  new_grid = transpose(new_grid)
  printState(new_grid)
  current_state = new_grid
  return new_grid, changed

def move_right_divide_without_printing(grid):
  global current_state
  new_grid = reverse(grid)
  new_grid, changed = move_left_divide_without_printing(new_grid)
  new_grid = reverse(new_grid)
  return new_grid, changed

def move_down_divide(grid):
  global current_state
  new_grid = transpose(grid)
  new_grid, changed = move_right_divide_without_printing(new_grid)
  new_grid = transpose(new_grid)
  printState(new_grid)
  current_state = new_grid
  return new_grid, changed

def print_state_for_stderr(grid):
  ans = ""
  for i in range(0, 4):
    for j in range(0, 4):
      ans = ans + str(grid[i][j]) + "\40"
  for i in range(len(mapper)):
    for j in range(len(mapper[i])):
      if len(mapper[i][j]) > 0:
        ans = ans + str(i+1) + "," + str(j+1)
        for z in range(len(mapper[i][j])):
          ans = ans + str(mapper[i][j][z]) + ","
        ans = ans[:-1]
        ans = ans + " "
  return ans 

def name_tile(r, c, mapper, var):
  mapper[r-1][c-1].append(var)
  return mapper

def value_of_tile(r, c, grid):
  print(grid[r-1][c-1])
  return grid[r-1][c-1]

class BasicParser(Parser):
  tokens = BasicLexer.tokens

  def __init__(self):
    self.env = { }

  @_('')
  def statement(self, p):
    pass

  @_('ADD LEFT "."')
  def statement(self, p):
    return(move_left_add(current_state))

  @_('SUBTRACT LEFT "."')
  def statement(self, p):
    return(move_left_subtract(current_state))

  @_('MULTIPLY LEFT "."')
  def statement(self, p):
    return(move_left_multiply(current_state))

  @_('DIVIDE LEFT "."')
  def statement(self, p):
    return(move_left_divide(current_state))

  @_('ADD RIGHT "."')
  def statement(self, p):
    return(move_right_add(current_state))

  @_('SUBTRACT RIGHT "."')
  def statement(self, p):
    return(move_right_subtract(current_state))

  @_('MULTIPLY RIGHT "."')
  def statement(self, p):
    return(move_right_multiply(current_state))

  @_('DIVIDE RIGHT "."')
  def statement(self, p):
    return(move_right_divide(current_state))

  @_('ADD UP "."')
  def statement(self, p):
    return(move_up_add(current_state))

  @_('SUBTRACT UP "."')
  def statement(self, p):
    return(move_up_subtract(current_state))

  @_('MULTIPLY UP "."')
  def statement(self, p):
    return(move_up_multiply(current_state))

  @_('DIVIDE UP "."')
  def statement(self, p):
    return(move_up_divide(current_state))

  @_('ADD DOWN "."')
  def statement(self, p):
    return(move_down_add(current_state))

  @_('SUBTRACT DOWN "."')
  def statement(self, p):
    return(move_down_subtract(current_state))

  @_('MULTIPLY DOWN "."')
  def statement(self, p):
    return(move_down_multiply(current_state))

  @_('DIVIDE DOWN "."')
  def statement(self, p):
    return(move_down_divide(current_state))

  @_('expr')
  def statement(self, p):
    return (p.expr)

  @_('NUMBER')
  def expr(self, p):
    return('num', p.NUMBER)

  @_('ASSIGN NUMBER TO NUMBER "," NUMBER "."')
  def statement(self, p):
    global flag
    try:
      flag = 0
      return(assign(current_state, p.NUMBER1, p.NUMBER2, p.NUMBER0))
    except:
      flag = 1
      print("2048> List Index Out of Range")

  @_('NUMBER "," NUMBER IS NAME "."')
  def statement(self, p):
    global mapper
    global flag
    flag = 0
    return(name_tile(p.NUMBER0, p.NUMBER1, mapper, p.NAME))

  @_('VALUE IN NUMBER "," NUMBER "."')
  def statement(self, p):
    global flag
    try:
      flag = 0
      return(value_of_tile(p.NUMBER0, p.NUMBER1, current_state))
    except:
      flag = 1
      print("2048> List Index Out of Range")


if __name__ == '__main__':
  lexer = BasicLexer()
  parser = BasicParser()
  env = {}
  current_state = initialize()
  flag = 0
  mapper = [[[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []]]
  while True:
    text = input('\n2048> Please type a command\n---->')
    if text:
      if text == 'exit':
        break
      tree = parser.parse(lexer.tokenize(text))
      if tree == None or flag == 1:
        stderr_fileno.write("-1")
      else:
        stderr_fileno.write(print_state_for_stderr(current_state))





