from collections import Counter


def update_wins():
  global win_cases
  win_cases = [[inp[0], inp[1], inp[2]], [inp[3], inp[4], inp[5]], [inp[6], inp[7], inp[8]],
              [inp[0], inp[3], inp[6]], [inp[1], inp[4], inp[7]], [inp[2], inp[5], inp[8]],
              [inp[0], inp[4], inp[8]], [inp[2], inp[4], inp[6]]]


def draw_board():
  global inp
  print('---------')
  for j in range(3):
    print('| {} {} {} |'.format(inp[j*3], inp[j*3 + 1], inp[j*3 + 2]))
  print('---------')


def check_win():
  update_wins()
  if '_' not in inp:
    print('Draw')
    return True
  for item in win_cases:
    val = dict(Counter(item))
    if 'X' in val:
      if val['X'] == 3:
        print('X wins')
        return True
    if 'O' in val:
      if val['O'] == 3:
        print('O wins')
        return True
  return False


inp = ['_' for underscore in range(9)]
draw_board()
x_turn = True

while True:
  try:
    x, y = input('Enter coordinates: ').split()
    x = int(x)
    y = int(y)
    if x in range(1, 4) and y in range(1, 4):
      y_pos = {1:3, 2:2, 3:1}
      if inp[3*(y_pos[y]-1) + (x-1)] == '_' or inp[3*(y_pos[y]-1) + (x-1)] == ' ':
        if x_turn:
          inp[3*(y_pos[y]-1) + (x-1)] = 'X'
          draw_board()
          if check_win():
            break
          x_turn = False
        else:
          inp[3*(y_pos[y]-1) + (x-1)] = 'O'
          draw_board()
          if check_win():
            break
          x_turn = True
      else:
        print('This cell is occupied! Choose another one!')
    else:
      print('Coordinates should be from 1 to 3!')
  except ValueError:
    print('You should enter numbers!')
