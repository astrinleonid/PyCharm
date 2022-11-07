
import time
from def_classes import Puzzle

# functions in the module:
# puzzle.check_solution() After the list line is assembled, check if it fits
# puzzle.make_list_of_options(pos_num)
# puzzle.is_any_options_left(options_list)
# option = puzzle.try_option(options_list,pos_num)
# option_list = puzzle.reject_the_option(option_list,pos_num)
# puzzle.finish_the_line(option, pos_num+1)
# puzzle.show_solution()


PUZZLE = """ 0,[10, 18, 2, 0]; 1,[1, 15, 11, 6]; 2,[5, 0, 9, 6]; 3,[11, 13, 0, 9]; 4,[1, 0, 0, 17];
5,[6, 4, 0, 3]; 6,[0, 18, 16, 9]; 7,[6, 2, 20, 17]; 8,[10, 4, 16, 6]; 9,[16, 9, 19, 10];
10,[1, 9, 17, 0]; 11,[11, 8, 6, 9]; 12,[16, 10, 0, 17]; 13,[2, 1, 8, 17]; 14,[14, 15, 4,
2]; 15,[0, 17, 17, 7]; 16,[6, 0, 5, 11]; 17,[12, 7, 13, 2]; 18,[12, 6, 18, 2]; 19,[18, 8,
15, 18]; 20,[9, 8, 16, 17]; 21,[13, 1, 10, 11]; 22,[0, 2, 8, 8]; 23,[6, 4, 18, 1];
24,[13, 12, 4, 2]; 25,[0, 12, 4, 9]; 26,[16, 12, 2, 2]; 27,[20, 17, 8, 9]; 28,[0, 2, 3,
0]; 29,[14, 6, 12, 18]; 30,[20, 2, 12, 11]; 31,[0, 6, 4, 19]; 32,[0, 7, 5, 0]; 33,[9, 10,
18, 17]; 34,[18, 12, 13, 3]; 35,[14, 10, 9, 6]; 36,[19, 18, 8, 18]; 37,[6, 19, 12, 0];
38,[2, 6, 11, 4]; 39,[15, 17, 11, 6]; 40,[4, 0, 8, 11]; 41,[12, 18, 18, 19]; 42,[18, 7,
14, 2]; 43,[6, 5, 20, 16]; 44,[6, 4, 4, 19]; 45,[2, 1, 0, 3]; 46,[4, 14, 20, 15]; 47,[18,
9, 0, 15]; 48,[0, 5, 16, 5]; 49,[8, 14, 14, 5]; 50,[14, 18, 18, 1]; 51,[19, 15, 18, 16];
52,[15, 18, 2, 12]; 53,[6, 0, 11, 11]; 54,[12, 0, 10, 11]; 55,[6, 15, 6, 3]; 56,[12, 15,
13, 18]; 57,[15, 5, 16, 5]; 58,[9, 6, 20, 8]; 59,[6, 19, 10, 17]; 60,[10, 11, 15, 20];
61,[7, 15, 10, 3]; 62,[7, 6, 11, 10]; 63,[5, 8, 8, 10]; 64,[14, 6, 15, 9]; 65,[9, 16, 5,
19]; 66,[4, 6, 17, 0]; 67,[3, 14, 14, 4]; 68,[9, 8, 17, 0]; 69,[20, 7, 5, 5]; 70,[8, 10,
15, 2]; 71,[2, 8, 0, 1]; 72,[16, 1, 0, 4]; 73,[10, 20, 11, 7]; 74,[0, 5, 15, 7]; 75,[15,
3, 11, 16]; 76,[6, 10, 10, 4]; 77,[11, 13, 8, 14]; 78,[16, 16, 1, 3]; 79,[13, 14, 5, 0];
80,[11, 18, 16, 19]; 81,[7, 20, 4, 0]; 82,[10, 3, 0, 19]; 83,[4, 12, 4, 19]; 84,[4, 12,
0, 0]; 85,[8, 7, 16, 3]; 86,[13, 15, 0, 8]; 87,[2, 8, 10, 3]; 88,[11, 0, 1, 1]; 89,[7,
10, 0, 12]; 90,[18, 13, 4, 11]; 91,[13, 4, 14, 10]; 92,[5, 1, 3, 9]; 93,[2, 0, 5, 14];
94,[6, 15, 11, 18]; 95,[0, 12, 11, 18]; 96,[11, 12, 4, 9]; 97,[4, 11, 13, 15]; 98,[14, 6,
10, 2]; 99,[5, 3, 2, 16]"""


PUZZLE_SIZE = 10
BORDER_VALUE = 0

def parse_puzzle_string(string):

    list = []
    list_of_piece_strings = string.split(';')
    print(len(list_of_piece_strings))
    for piece_string in list_of_piece_strings:
        [num_str, sides_str] = piece_string.split('[')
        number = int(num_str.rstrip(' ,'))
        sides = [int(side.strip(' ]')) for side in sides_str.split(',')]
        list.append((number,sides))
    return list

def finish_the_line(puzzle, position):
    """
    Tries to finish the line from the position in 'position',
    Returns True if successfull, false otherwise
    """

    options = puzzle.make_list_of_options(position)
    while puzzle.try_option(options):

        puzzle.show_solution()
        if (position + 1) == puzzle.size**2:
           return True
        else:
           if finish_the_line(puzzle, position + 1):
               return True

        options = puzzle.reject_the_option(options)


    return False






def solve_the_puzzle(puzzle_set,puzzle_size,border_value):

    puzzle = Puzzle(puzzle_set,puzzle_size,border_value)
    if finish_the_line(puzzle, 0):
        puzzle.show_solution()
    else:
        print("Solution not found")


if __name__ == '__main__':

    solve_the_puzzle(parse_puzzle_string(PUZZLE),PUZZLE_SIZE,BORDER_VALUE)

