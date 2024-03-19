from tkinter import *

# Declare all my parameters as global variables
WINDOW_SIZE = 600
GRID_LINE_WIDTH = 2
SYMBOL_WIDTH = WINDOW_SIZE / 12
SYMBOL_SIZE = 0.5
CELL_SIZE = WINDOW_SIZE / 3
# Prettification of our app
X_COLOR = 'dodger blue'
O_COLOR = 'tomato'
DRAW_SCREEN_COLOR = 'light sea green'
GRID_COLOR = 'light grey'
BG_COLOR = 'white'
# Keep track of game states
STATE_TITLE_SCREEN = 0
STATE_X_TURN = 1
STATE_O_TURN = 2
STATE_GAME_OVER = 3
FIRST_PLAYER = 2
EMPTY = 0
X = 1
O = 2

"""
    > Create a class called Game that inherits from the Tk class
    > Create a constructor for the Game class
    > [ Inside the constructor ]> call the Tk constructor
    > [Inside the constrictor]> Create a canvas object using the Canvas() method
    > [Inside the constrictor]> [Inside the Canvas method]> Set the height of the canvas to the WINDOW_SIZE
    > [Inside the constrictor]> [Inside the Canvas method]> Set the width of the canvas to the WINDOW_SIZE
    > [Inside the constrictor]> [Inside the Canvas method]> Set the background color of the canvas to the BG_COLOR
    > [Inside the constrictor]> Pack the canvas using the pack() method
    > [Inside the constrictor]> Bind the x key to the exit function using the bind() method
    > [Inside the constrictor]> Bind the left mouse button to the click function using the bind() method
    
    > [Inside the constrictor]> Set the gamestate to the STATE_TITLE_SCREEN
    > [Inside the constrictor]> Call the title_screen() function

    > [Inside the constrictor]> Create a board variable using a list comprehension
    > [Inside the constrictor]> [Inside the list comprehension]> Create a list of 3 empty cells using a list comprehension
    > [Inside the constrictor]> [Inside the list comprehension]> [Inside the list comprehension]> Set the value of the cell to the EMPTY variable
    
"""


class Game(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.canvas = Canvas(
            height=WINDOW_SIZE, width=WINDOW_SIZE,
            bg=BG_COLOR)

        self.canvas.pack()

        self.bind('<x>', self.exit)
        self.canvas.bind('<Button-1>', self.click)

        self.gamestate = STATE_TITLE_SCREEN
        self.title_screen()

        self.board = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

    """
        > Create a function called title_screen
        > [Inside the function]> Delete all objects on the canvas using the delete() method
        
        > [Inside the function]> Create a rectangle using the create_rectangle() method
        > [Inside the function]> [Inside the create_rectangle method]> Set the x1 coordinate to 0
        > [Inside the function]> [Inside the create_rectangle method]> Set the y1 coordinate to 0
        > [Inside the function]> [Inside the create_rectangle method]> Set the x2 coordinate to the WINDOW_SIZE
        > [Inside the function]> [Inside the create_rectangle method]> Set the y2 coordinate to the WINDOW_SIZE
        > [Inside the function]> [Inside the create_rectangle method]> Set the fill color to the O_COLOR
        > [Inside the function]> [Inside the create_rectangle method]> Set the outline to an empty string

        > [Inside the function]> Create a rectangle using the create_rectangle() method
        > [Inside the function]> [Inside the create_rectangle method]> Set the x1 coordinate to the WINDOW_SIZE divided by 15
        > [Inside the function]> [Inside the create_rectangle method]> Set the y1 coordinate to the WINDOW_SIZE divided by 15
        > [Inside the function]> [Inside the create_rectangle method]> Set the x2 coordinate to the WINDOW_SIZE multiplied by 14 divided by 15
        > [Inside the function]> [Inside the create_rectangle method]> Set the y2 coordinate to the WINDOW_SIZE multiplied by 14 divided by 15
        > [Inside the function]> [Inside the create_rectangle method]> Set the width to the WINDOW_SIZE divided by 20
        > [Inside the function]> [Inside the create_rectangle method]> Set the outline to the X_COLOR

        > [Inside the function]> Create a rectangle using the create_rectangle() method
        > [Inside the function]> [Inside the create_rectangle method]> Set the x1 coordinate to the WINDOW_SIZE divided by 10
        > [Inside the function]> [Inside the create_rectangle method]> Set the y1 coordinate to the WINDOW_SIZE divided by 10
        > [Inside the function]> [Inside the create_rectangle method]> Set the x2 coordinate to the WINDOW_SIZE multiplied by 9 divided by 10
        > [Inside the function]> [Inside the create_rectangle method]> Set the y2 coordinate to the WINDOW_SIZE multiplied by 9 divided by 10
        > [Inside the function]> [Inside the create_rectangle method]> Set the fill color to the X_COLOR
        > [Inside the function]> [Inside the create_rectangle method]> Set the outline to an empty string

        > [Inside the function]> Create a text object using the create_text() method
        > [Inside the function]> [Inside the create_text method]> Set the x coordinate to the WINDOW_SIZE divided by 2
        > [Inside the function]> [Inside the create_text method]> Set the y coordinate to the WINDOW_SIZE divided by 3
        > [Inside the function]> [Inside the create_text method]> Set the text to 'TIC TAC TOE'
        > [Inside the function]> [Inside the create_text method]> Set the font to ('Arial', 40)
        > [Inside the function]> [Inside the create_text method]> Set the fill color to the BG_COLOR

        > [Inside the function]> Create a text object using the create_text() method
        > [Inside the function]> [Inside the create_text method]> Set the x coordinate to the WINDOW_SIZE divided by 2
        > [Inside the function]> [Inside the create_text method]> Set the y coordinate to the WINDOW_SIZE divided by 2
        > [Inside the function]> [Inside the create_text method]> Set the text to 'Press any key to continue'
        > [Inside the function]> [Inside the create_text method]> Set the font to ('Arial', 20)
        > [Inside the function]> [Inside the create_text method]> Set the fill color to the BG_COLOR
    """

    def title_screen(self):
        # placeholder title screen
        self.canvas.delete('all')  # just in case

        self.canvas.create_rectangle(
            0, 0,
            WINDOW_SIZE, WINDOW_SIZE,
            fill=O_COLOR,
            outline='')

        self.canvas.create_rectangle(
            int(WINDOW_SIZE/15), int(WINDOW_SIZE/15),
            int(WINDOW_SIZE*14/15), int(WINDOW_SIZE*14/15),
            width=int(WINDOW_SIZE/20),
            outline=X_COLOR)

        self.canvas.create_rectangle(
            int(WINDOW_SIZE/10), int(WINDOW_SIZE/10),
            int(WINDOW_SIZE*9/10), int(WINDOW_SIZE*9/10),
            fill=X_COLOR,
            outline='')

        self.canvas.create_text(
            WINDOW_SIZE/2,
            WINDOW_SIZE/3,
            text='TIC TAC TOE', fill='white',
            font=('Franklin Gothic', int(-WINDOW_SIZE/12), 'bold'))

        self.canvas.create_text(
            int(WINDOW_SIZE/2),
            int(WINDOW_SIZE/2.5),
            text='[PLAY]', fill='white',
            font=('Franklin Gothic', int(-WINDOW_SIZE/25)))

    """
        > Create a function called new_board
        > [Inside the function]> Delete all objects on the canvas using the delete() method

        > [Inside the function]> Reset the board variable to an empty list
        > [Inside the function]> [Inside the empty list]> Add a list with 3 EMPTY values
        > [Inside the function]> [Inside the empty list]> Add a list with 3 EMPTY values
        > [Inside the function]> [Inside the empty list]> Add a list with 3 EMPTY values

        > [Inside the function]> Draw the grid lines using the create_line() method
        > [Inside the function]> [Inside the create_line method]> Set the x1 coordinate to the CELL_SIZE
        > [Inside the function]> [Inside the create_line method]> Set the y1 coordinate to 0
        > [Inside the function]> [Inside the create_line method]> Set the x2 coordinate to the CELL_SIZE
        > [Inside the function]> [Inside the create_line method]> Set the y2 coordinate to the WINDOW_SIZE
        > [Inside the function]> [Inside the create_line method]> Set the width to the GRID_LINE_WIDTH
        > [Inside the function]> [Inside the create_line method]> Set the outline to the GRID_COLOR

        > [Inside the function]> Draw the grid lines using the create_line() method
        > [Inside the function]> [Inside the create_line method]> Set the x1 coordinate to the CELL_SIZE multiplied by 2
        > [Inside the function]> [Inside the create_line method]> Set the y1 coordinate to 0
        > [Inside the function]> [Inside the create_line method]> Set the x2 coordinate to the CELL_SIZE multiplied by 2
        > [Inside the function]> [Inside the create_line method]> Set the y2 coordinate to the WINDOW_SIZE
        > [Inside the function]> [Inside the create_line method]> Set the width to the GRID_LINE_WIDTH
        > [Inside the function]> [Inside the create_line method]> Set the outline to the GRID_COLOR
    """

    def new_board(self):
        """
        Clears canvas and game board memory, draws a new board on the canvas
        """

        # delete all objects
        self.canvas.delete('all')

        # reset
        self.board = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

        # draw grid
        for n in range(1, 3):
            # vertical
            self.canvas.create_line(
                CELL_SIZE*n, 0,
                CELL_SIZE*n, WINDOW_SIZE,
                width=GRID_LINE_WIDTH, fill=GRID_COLOR)
            # horizontal
            self.canvas.create_line(
                0, CELL_SIZE*n,
                WINDOW_SIZE, CELL_SIZE*n,
                width=GRID_LINE_WIDTH, fill=GRID_COLOR)

    """
        > Create a function called gameover_screen
        > [Inside the function]> Delete all objects on the canvas using the delete() method
        > [Inside the function]> If the outcome is 'X WINS' then
        > [Inside the function]> [Inside the if statement]> Set the wintext variable to 'X wins'
        > [Inside the function]> [Inside the if statement]> Set the wincolor variable to the X_COLOR

        > [Inside the function]> Else if the outcome is 'O WINS' then
        > [Inside the function]> [Inside the else if statement]> Set the wintext variable to 'O wins'
        > [Inside the function]> [Inside the else if statement]> Set the wincolor variable to the O_COLOR

        > [Inside the function]> Else if the outcome is 'DRAW' then
        > [Inside the function]> [Inside the else if statement]> Set the wintext variable to 'Draw'
        > [Inside the function]> [Inside the else if statement]> Set the wincolor variable to the DRAW_SCREEN_COLOR

        > [Inside the function]> Draw a rectangle on the canvas using the create_rectangle() method
        > [Inside the function]> [Inside the create_rectangle method]> Set the x1 coordinate to 0
        > [Inside the function]> [Inside the create_rectangle method]> Set the y1 coordinate to 0
        > [Inside the function]> [Inside the create_rectangle method]> Set the x2 coordinate to the WINDOW_SIZE
        > [Inside the function]> [Inside the create_rectangle method]> Set the y2 coordinate to the WINDOW_SIZE
        > [Inside the function]> [Inside the create_rectangle method]> Set the fill to the wincolor variable
        > [Inside the function]> [Inside the create_rectangle method]> Set the outline to ''

        > [Inside the function]> Draw a text on the canvas using the create_text() method
        > [Inside the function]> [Inside the create_text method]> Set the x coordinate to the WINDOW_SIZE divided by 2
        > [Inside the function]> [Inside the create_text method]> Set the y coordinate to the WINDOW_SIZE divided by 2
        > [Inside the function]> [Inside the create_text method]> Set the text to the wintext variable
        > [Inside the function]> [Inside the create_text method]> Set the fill to 'white'
        > [Inside the function]> [Inside the create_text method]> Set the font to ('Franklin Gothic', the WINDOW_SIZE divided by -6, 'bold')

        > [Inside the function]> Draw a text on the canvas using the create_text() method
        > [Inside the function]> [Inside the create_text method]> Set the x coordinate to the WINDOW_SIZE divided by 2
        > [Inside the function]> [Inside the create_text method]> Set the y coordinate to the WINDOW_SIZE divided by 1.65
        > [Inside the function]> [Inside the create_text method]> Set the text to 'Click to play again'
        > [Inside the function]> [Inside the create_text method]> Set the fill to 'white'
        > [Inside the function]> [Inside the create_text method]> Set the font to ('Franklin Gothic', the WINDOW_SIZE divided by -12, 'bold')
    """

    def gameover_screen(self, outcome):
        # placeholder gameover screen

        self.canvas.delete('all')

        if outcome == 'X WINS':
            wintext = 'X wins'
            wincolor = X_COLOR

        elif outcome == 'O WINS':
            wintext = 'O wins'
            wincolor = O_COLOR

        elif outcome == 'DRAW':
            wintext = 'Draw'
            wincolor = DRAW_SCREEN_COLOR

        self.canvas.create_rectangle(
            0, 0,
            WINDOW_SIZE, WINDOW_SIZE,
            fill=wincolor, outline='')

        self.canvas.create_text(
            int(WINDOW_SIZE/2), int(WINDOW_SIZE/2),
            text=wintext, fill='white',
            font=('Franklin Gothic', int(-WINDOW_SIZE/6), 'bold'))

        self.canvas.create_text(
            int(WINDOW_SIZE/2), int(WINDOW_SIZE/1.65),
            text='[click to play again]', fill='white',
            font=('Franklin Gothic', int(-WINDOW_SIZE/25)))

    """
        > Create a function called click
        > [Inside the function]> Create a variable called x and set it to the ptgrid() function with the event.x as the parameter
        > [Inside the function]> Create a variable called y and set it to the ptgrid() function with the event.y as the parameter

        > [Inside the function]> If the gamestate is STATE_TITLE_SCREEN then
        > [Inside the function]> [Inside the if statement]> Call the new_board() function
        > [Inside the function]> [Inside the if statement]> Set the gamestate to FIRST_PLAYER

        > [Inside the function]> Else if the gamestate is STATE_X_TURN and the board at the y and x coordinates is EMPTY then
        > [Inside the function]> [Inside the else if statement]> Call the new_move() function with the X, x and y variables as the parameters

        > [Inside the function]> [Inside the else if statement]> If the has_won() function with the X variable as the parameter is True then
        > [Inside the function]> [Inside the else if statement]> [Inside the if statement]> Set the gamestate to STATE_GAME_OVER
        > [Inside the function]> [Inside the else if statement]> [Inside the if statement]> Call the gameover_screen() function with the 'X WINS' string as the parameter

        > [Inside the function]> [Inside the else if statement]> Else if the is_a_draw() function is True then
        > [Inside the function]> [Inside the else if statement]> [Inside the else if statement]> Set the gamestate to STATE_GAME_OVER
        > [Inside the function]> [Inside the else if statement]> [Inside the else if statement]> Call the gameover_screen() function with the 'DRAW' string as the parameter

        > [Inside the function]> [Inside the else if statement]> Else
        > [Inside the function]> [Inside the else if statement]> [Inside the else statement]> Set the gamestate to STATE_O_TURN
    """

    def click(self, event):
        """
        Handles most of the game logic
        """

        x = self.ptgrid(event.x)
        y = self.ptgrid(event.y)

        if self.gamestate == STATE_TITLE_SCREEN:
            self.new_board()
            self.gamestate = FIRST_PLAYER

        elif (self.gamestate == STATE_X_TURN and
                self.board[y][x] == EMPTY):
            self.new_move(X, x, y)

            if self.has_won(X):
                self.gamestate = STATE_GAME_OVER
                self.gameover_screen('X WINS')

            elif self.is_a_draw():
                self.gamestate = STATE_GAME_OVER
                self.gameover_screen('DRAW')

            else:
                self.gamestate = STATE_O_TURN

        elif (self.gamestate == STATE_O_TURN and
                self.board[y][x] == EMPTY):
            self.new_move(O, x, y)

            if self.has_won(O):
                self.gamestate = STATE_GAME_OVER
                self.gameover_screen('O WINS')

            elif self.is_a_draw():
                self.gamestate = STATE_GAME_OVER
                self.gameover_screen('DRAW')

            else:
                self.gamestate = STATE_X_TURN

        elif self.gamestate == STATE_GAME_OVER:
            # reset
            self.new_board()
            self.gamestate = FIRST_PLAYER

    """
        > Create a function called new_move
        > If the player X
    """

    def new_move(self, player, grid_x, grid_y):

        if player == X:
            self.draw_X(grid_x, grid_y)
            self.board[grid_y][grid_x] = X

        elif player == O:
            self.draw_O(grid_x, grid_y)
            self.board[grid_y][grid_x] = O

    def draw_X(self, grid_x, grid_y):
        """
        draw the X symbol at x, y in the grid
        """

        x = self.gtpix(grid_x)
        y = self.gtpix(grid_y)
        delta = CELL_SIZE/2*SYMBOL_SIZE

        self.canvas.create_line(
            x-delta, y-delta,
            x+delta, y+delta,
            width=SYMBOL_WIDTH, fill=X_COLOR)

        self.canvas.create_line(
            x+delta, y-delta,
            x-delta, y+delta,
            width=SYMBOL_WIDTH, fill=X_COLOR)

    def draw_O(self, grid_x, grid_y):
        """
        draw an O symbol at x, y in the grid
        """

        x = self.gtpix(grid_x)
        y = self.gtpix(grid_y)
        delta = CELL_SIZE/2*SYMBOL_SIZE

        self.canvas.create_oval(
            x-delta, y-delta,
            x+delta, y+delta,
            width=SYMBOL_WIDTH, outline=O_COLOR)

    def has_won(self, symbol):
        for y in range(3):
            if self.board[y] == [symbol, symbol, symbol]:
                return True

        for x in range(3):
            if self.board[0][x] == self.board[1][x] == self.board[2][x] == symbol:
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol:
            return True

        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == symbol:
            return True

        # no win sequence found
        return False

    def is_a_draw(self):
        for row in self.board:
            if EMPTY in row:
                return False

        # no empty cell left, the game is a draw
        return True

    def gtpix(self, grid_coord):
        # gtpix = grid_to_pixels
        # for a grid coordinate, returns the pixel coordinate of the center
        # of the corresponding cell

        pixel_coord = grid_coord * CELL_SIZE + CELL_SIZE / 2
        return pixel_coord

    def ptgrid(self, pixel_coord):
        # ptgrid = pixels_to_grid
        # the opposit of gtpix()

        # somehow the canvas has a few extra pixels on the right and bottom side
        if pixel_coord >= WINDOW_SIZE:
            pixel_coord = WINDOW_SIZE - 1

        grid_coord = int(pixel_coord / CELL_SIZE)
        return grid_coord

    def exit(self, event):
        self.destroy()


def main():
    root = Game()
    root.mainloop()


main()
