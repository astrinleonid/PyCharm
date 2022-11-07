import os
import time


class Option:

    def __init__(self, piece_sides, piece_number, rotation):

        self.top = piece_sides[(0 - rotation) % 4]
        self.right = piece_sides[(1 - rotation) % 4]
        self.bottom = piece_sides[(2 - rotation) % 4]
        self.left = piece_sides[(3 - rotation) % 4]
        self.number = piece_number
        self.rotation = rotation

class Puzzle:

    pieces_set = set()
    solution = []
    solution_set = []
    border = 0
    size = 0


    def show_solution(self):
        printout = []
        string_number = (len(self.solution)-1) // self.size
        position_in_string = len(self.solution) - string_number * self.size

        for i in range(self.size):
            if i > string_number:
                break
            line1 = ""
            line2 = ""
            line3 = ""

            for j in range(self.size):
                if i == string_number and j > position_in_string -1:
                    break
                top = str(self.solution[i*self.size+j].top).rjust(2,' ')
                left = str(self.solution[i*self.size+j].left).rjust(2,' ')
                right = str(self.solution[i*self.size+j].right).rjust(2,' ')
                bottom = str(self.solution[i*self.size+j].bottom).rjust(2,' ')
                number = str(self.solution[i*self.size+j].number).rjust(2,' ')
                line1 += "    " + top + "    "
                line2 += " " + left + " " + number + " " + right + " "
                line3 += "    " + bottom + "    "
            printout.append(line1)
            printout.append(line2)
            printout.append(line3)
        os.system('cls' if os.name == 'nt' else 'clear')
        for line in printout:
            print(line)
        time.sleep(0.05)

    def list_empty(self,options):
        if len(options) == 0:
            return True
        else:
            return False

    def fetch_option(self,options):
        return options[0]

    def pop_first_option(self,options):
        options.pop(0)
        return options

    def piece_fits(self,option,position):
        # get constraints
        right = option.right        #default
        bottom = option.bottom      #default
        if position % self.size > 0:
            left = self.solution[position - 1].right
        else:
            left = self.border
        if position // self.size > 0:
            top = self.solution[position - self.size].bottom
        else:
            top = self.border
        if position % self.size == self.size - 1:
            right = self.border
        if position // self.size == self.size - 1:
            bottom == self.border
        if option.left == left and option.top == top and option.bottom == bottom and option.right == right:
            return True
        return False

    def check_solution(self):
        for i in range(self.size*(self.size-1),self.size**2):
            if self.solution[i].bottom != self.border:
                return False
        return True

    def make_list_of_options(self,position):
        """
        Returns the list of all possible options to fill the spot with left and top neighbours defined
        as a list of (piece,turn) tuples

        """
        options = []
        for piece in self.pieces_set:  #TODO: define what is a piece
            if not piece.number in self.solution_set:
                for rotation in range(4):
                    option = Option(piece.sides, piece.number, rotation)
                    if self.piece_fits(option,position):
                        options.append(option)
        if len(options) == 0:
            print("No options found")
        return options


    def try_option(self, options):
        """
        Choose the first element from the list of options
        mark the piece as taken in the pull of pieces
        put it at the position in the solution
        Returns False if the list is empty (nothing to try), otherwise True
        """
        if self.list_empty(options):
            return False

        option = self.fetch_option(options) # take the first option from the list
        self.solution.append(option)
        self.solution_set.append(option.number)


        return True


    def reject_the_option(self,options):
        """
        # Choose the first element from the list of options
        # mark the piece as not taken in the pull of pieces
        # delete it from the position in the solution
        # pop it from the list
        """
        self.solution.pop()
        self.solution_set.pop()
        options = self.pop_first_option(options)
        return options


    def __init__(self, pool_of_pieces, size, border_value):
        self.size = size
        self.border = border_value
        self.solution = []
        self.solution_set = []
        for number, sides in pool_of_pieces:
            self.pieces_set.add(self.Piece(number,sides))


    class Piece:

        def __init__(self, number, sides):
            self.sides = sides
            self.number = number



