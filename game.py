from tkinter import *  # Importing the necessary modules
import numpy as np

symbol_thickness = 50
dot_color = "black"
player1_color = "blue2"
player1_color_light = '#67B0CF'
player2_color = "red2"
player2_color_light = '#EE7E77'
Green_color = 'saddle brown'

# defines a class Dots_and_Boxes that has several functions to handle the game logic


class Dots_and_Boxes():
    # ------------------------------------------------------------------
    # Initialization functions
    # ------------------------------------------------------------------
    def __init__(self,level):
        self.level = level
        # Create a new Tkinter window
        self.window = Tk()
        # Set the window title
        self.window.title('Dots and Boxes Game')

        # Define game settings based on level
        if level == "easy":
            self.size_of_board = 300
            self.number_of_dots = 3
        elif level == "medium":
            self.size_of_board = 500
            self.number_of_dots = 5
        elif level == "hard":
            self.size_of_board = 700
            self.number_of_dots = 7

        # Define game symbols and colors
        self.symbol_size = (self.size_of_board / 3 -
                            self.size_of_board / 8) / 2
        self.dot_width = 0.25*self.size_of_board/self.number_of_dots
        self.edge_width = 0.1*self.size_of_board/self.number_of_dots
        self.distance_between_dots = self.size_of_board / (self.number_of_dots)

        # Create a new Canvas widget within the window
        self.canvas = Canvas(
            self.window, width=self.size_of_board, height=self.size_of_board)
        # Pack the Canvas widget
        self.canvas.pack()
        # Bind the left mouse button click event to the 'click' function of this class
        self.window.bind('<Button-1>', self.click)
        # Set player1_starts variable to True
        self.player1_starts = True

        # Call the refresh_board function to initialize the game board
        self.refresh_board()
        # Call the play_again function to ask if players want to play again
        self.play_again()

    # this function resets the board for a new game
    def play_again(self):
        # Clear the board and reset the board status, row status, and column status arrays
        self.refresh_board()
        self.board_status = np.zeros(
            shape=(self.number_of_dots - 1, self.number_of_dots - 1))
        self.row_status = np.zeros(
            shape=(self.number_of_dots, self.number_of_dots - 1))
        self.col_status = np.zeros(
            shape=(self.number_of_dots - 1, self.number_of_dots))

        # Switch the starting player and reset the turn-related variables
        self.player1_starts = not self.player1_starts
        self.player1_turn = not self.player1_starts
        self.reset_board = False
        self.turntext_handle = []

        # Reset the list of already marked boxes and display the current player's turn
        self.already_marked_boxes = []
        self.display_turn_text()

        # This method starts the main event loop of the Tkinter window, which waits for user input and events to occur and processes them. The window will remain open until the user closes it or the program exits.
    def mainloop(self):
        self.window.mainloop()

    # ------------------------------------------------------------------
    # Logical Functions:
    # The modules required to carry out game logic
    # ------------------------------------------------------------------

    # this method of a class that is used to check if a particular grid is already occupied or not
    def is_grid_occupied(self, logical_position, type):
        # Here, the row and column of the logical position are extracted from the logical_position tuple and assigned to r and c variables respectively
        r = logical_position[0]
        c = logical_position[1]
        # Initially, the occupied flag is set to True, which means that the grid is considered to be occupied by default
        occupied = True
        # This block of code checks if the type of the grid is 'row' and if the corresponding row status is equal to 0, which means that the grid is not yet occupied. If this condition is satisfied, then the occupied flag is set to False, indicating that the grid is not occupied
        if type == 'row' and self.row_status[c][r] == 0:
            occupied = False
        # This block of code checks if the type of the grid is 'col' and if the corresponding column status is equal to 0, which means that the grid is not yet occupied. If this condition is satisfied, then the occupied flag is set to False, indicating that the grid is not occupied
        if type == 'col' and self.col_status[c][r] == 0:
            occupied = False

        # Finally, the value of the occupied flag is returned, indicating whether the grid is occupied or not
        return occupied


    def convert_grid_to_logical_position(self, grid_position):
        # Convert the grid position to a numpy array
        grid_position = np.array(grid_position)

        # Convert the grid position to a logical position by dividing by the distance between dots
        # and rounding down to the nearest integer
        position = (grid_position - self.distance_between_dots /
                    4) // (self.distance_between_dots/2)

        # Initialize type to False and logical_position to an empty list
        type = False
        logical_position = []

        # If the position is on a row and the column is even
        if position[1] % 2 == 0 and (position[0] - 1) % 2 == 0:
            # Calculate the row and column based on the position
            r = int((position[0] - 1) // 2)
            c = int(position[1] // 2)
            logical_position = [r, c]
            type = 'row'
            # Set the row status to 1 (indicating that the row has been clicked)
            # self.row_status[c][r]=1

        # If the position is on a column and the row is even
        elif position[0] % 2 == 0 and (position[1] - 1) % 2 == 0:
            # Calculate the row and column based on the position
            c = int((position[1] - 1) // 2)
            r = int(position[0] // 2)
            logical_position = [r, c]
            type = 'col'

        # Return the logical position and type
        return logical_position, type

    # The function mark_box() takes the current game board's status and marks boxes that have been completed by players
    # The boxes are marked with a different color based on which player completed them
    def mark_box(self):
        # Find all boxes that have been completed by player 1 and mark them
        # Get the indices of all boxes that have been completed by player 1
        boxes = np.argwhere(self.board_status == -4)
        for box in boxes:
            # Check if the box has already been marked or is empty
            if list(box) not in self.already_marked_boxes and list(box) !=[]:
                # Add the box to the list of already marked boxes
                self.already_marked_boxes.append(list(box))
                color = player1_color_light  # Choose the color for player 1
                # Shade the box with the chosen color.
                self.shade_box(box, color)
        # Find all boxes that have been completed by player 2 and mark them
        # Get the indices of all boxes that have been completed by player 2
        boxes = np.argwhere(self.board_status == 4)
        for box in boxes:
            # Check if the box has already been marked or is empty
            if list(box) not in self.already_marked_boxes and list(box) !=[]:
                # Add the box to the list of already marked boxes
                self.already_marked_boxes.append(list(box))
                # Choose the color for player 2
                color = player2_color_light
                # Shade the box with the chosen color
                self.shade_box(box, color)
    # The function update_board() updates the game board with the current player's move
    def update_board(self, type, logical_position):
        # Extract the row and column indices from the logical position.
        r = logical_position[0]
        c = logical_position[1]

        # Set the value that will be added to the board status based on which player's turn it is.
        val = 1
        if self.player1_turn:
            val = -1

        # Update the board status for the current move.
        # Check that the move is within the bounds of the board.
        if c < (self.number_of_dots-1) and r < (self.number_of_dots-1):
            # Update the status of the box that contains the move.
            self.board_status[c][r] += val

        # If the move is a row move, update the row status and the status of the box above it.
        if type == 'row':
            # Update the row status to indicate that the row has been completed.
            self.row_status[c][r] = 1
            if c >= 1:    # Check that the box above the current one exists.
                # Update the status of the box above the current one.
                self.board_status[c-1][r] += val

        # If the move is a column move, update the column status and the status of the box to the left of it.
        elif type == 'col':
            # Update the column status to indicate that the column has been completed.
            self.col_status[c][r] = 1
            if r >= 1:    # Check that the box to the left of the current one exists.
                # Update the status of the box to the left of the current one.
                self.board_status[c][r-1] += val

    # The function checks whether the game is over by checking if all rows and columns have been completed
    def is_gameover(self):
        return (self.row_status == 1).all() and (self.col_status == 1).all()

    # ------------------------------------------------------------------
    # Drawing Functions:
    # The modules required to draw required game based object on canvas
    # ------------------------------------------------------------------

    # The function creates a line segment (an edge) between two dots on the game board
    def make_edge(self, type, logical_position):
        # Calculate the start and end points of the edge based on the type of edge and the logical position.
        if type == 'row':
            # The start x-coordinate is the center of the left dot in the row.
            start_x = self.distance_between_dots/2 + \
                logical_position[0]*self.distance_between_dots
            # The end x-coordinate is the center of the right dot in the row.
            end_x = start_x+self.distance_between_dots
            # The y-coordinate is the center of the dots in the row.
            start_y = self.distance_between_dots/2 + \
                logical_position[1]*self.distance_between_dots
            end_y = start_y
        elif type == 'col':
            # The start y-coordinate is the center of the top dot in the column.
            start_y = self.distance_between_dots / 2 + \
                logical_position[1] * self.distance_between_dots
            # The end y-coordinate is the center of the bottom dot in the column.
            end_y = start_y + self.distance_between_dots
            # The x-coordinate is the center of the dots in the column.
            start_x = self.distance_between_dots / 2 + \
                logical_position[0] * self.distance_between_dots
            end_x = start_x

        # Set the color of the edge based on which player's turn it is.
        if self.player1_turn:
            color = player1_color
        else:
            color = player2_color

        # Create the line segment (edge) using the start and end points and the chosen color.
        self.canvas.create_line(start_x, start_y, end_x,
                                end_y, fill=color, width=self.edge_width)


    def display_gameover(self):
        # Get the scores of both players
        player1_score = len(np.argwhere(self.board_status == -4))
        player2_score = len(np.argwhere(self.board_status == 4))

        # Determine the winner or if it's a tie
        if player1_score > player2_score:
            text = 'Winner: Player 1 '
            color = player1_color
        elif player2_score > player1_score:
            text = 'Winner: Player 2 '
            color = player2_color
        else:
            text = 'Its a tie'
            color = 'maroon'

        # Clear the canvas and display the winner and scores
        self.canvas.delete("all")
        self.canvas.create_text(
            self.size_of_board / 2, self.size_of_board / 3, font=("Arial Bold", 18),fill=color, text=text)

        score_text = 'Scores \n'
        self.canvas.create_text(self.size_of_board / 2, 5 * self.size_of_board / 8,
                                font=("Arial Bold", 13), fill=Green_color, text=score_text)

        score_text = 'Player 1 : ' + str(player1_score) + '\n'
        score_text += 'Player 2 : ' + str(player2_score) + '\n'
        self.canvas.create_text(self.size_of_board / 2, 3 * self.size_of_board / 4,
                                font=("Arial Bold", 13), fill=Green_color, text=score_text)

        # Set the board to be reset
        self.reset_board = True

        score_text = 'Click to play again \n'
        self.canvas.create_text(self.size_of_board / 2, 15 * self.size_of_board /
                                16, font=("Arial Bold", 13), fill="black", text=score_text)
    # This function refreshes the board, creating the dots and gridlines
    def refresh_board(self):
        # Create vertical grid lines
        for i in range(self.number_of_dots):
            x = i*self.distance_between_dots+self.distance_between_dots/2
            self.canvas.create_line(x, self.distance_between_dots/2, x,
                                    self.size_of_board-self.distance_between_dots/2,
                                    fill='gray', dash = (2, 2))
            # Create horizontal grid lines
            self.canvas.create_line(self.distance_between_dots/2, x,
                                    self.size_of_board-self.distance_between_dots/2, x,
                                    fill='gray', dash=(2, 2))
        # Create the dots
        for i in range(self.number_of_dots):
            for j in range(self.number_of_dots):
                start_x = i*self.distance_between_dots+self.distance_between_dots/2
                end_x = j*self.distance_between_dots+self.distance_between_dots/2
                self.canvas.create_oval(start_x-self.dot_width/2, end_x-self.dot_width/2, start_x+self.dot_width/2,end_x+self.dot_width/2, fill=dot_color,outline=dot_color)
    # This function updates the displayed text indicating whose turn it is
    def display_turn_text(self):
        # Determine whose turn it is
        text = 'Next turn: '
        if self.player1_turn:
            text += 'Player1'
            color = player1_color
        else:
            text += 'Player2'
            color = player2_color

        # Remove the old turn text from the canvas
        self.canvas.delete(self.turntext_handle)
        # Add the new turn text to the canvas
        self.turntext_handle = self.canvas.create_text(self.size_of_board - 5*len(text),
                                                       self.size_of_board-self.distance_between_dots/8,
                                                       font="cmr 15 bold", text=text, fill=color)
    '''
    The above function first sets the initial text to "Next turn: ", and then adds "Player1" or "Player2" to the end of the string depending on whose turn it is. It also sets the color of the text to the appropriate player's color.

    Next, it deletes the old turn text from the canvas (if it exists), and creates a new turn text using the create_text method of the canvas. The new turn text is positioned towards the bottom right corner of the board, and uses the appropriate color and font size. The function stores a reference to the new turn text in the turntext_handle attribute of the class instance so it can be deleted later.
    '''

    # This function takes a box represented by its top-left coordinate and a color as input, and shades the box with that color on the canvas
    def shade_box(self, box, color):
        # Calculate the coordinates of the top-left and bottom-right corners of the box
        start_x = self.distance_between_dots / 2 + \
            box[1] * self.distance_between_dots + self.edge_width/2
        start_y = self.distance_between_dots / 2 + \
            box[0] * self.distance_between_dots + self.edge_width/2
        end_x = start_x + self.distance_between_dots - self.edge_width
        end_y = start_y + self.distance_between_dots - self.edge_width
        # Draw a rectangle on the canvas with the calculated coordinates and the given color
        self.canvas.create_rectangle(start_x, start_y, end_x, end_y, fill=color, outline='')

    # This is a method that displays the text indicating whose turn it is
    def display_turn_text(self):
        # Set the initial text
        text = 'Next turn: '
        # If it's player 1's turn, append 'Player1' to the text and set the color to player1_color
        if self.player1_turn:
            text += 'Player1'
            color = player1_color
        # If it's player 2's turn, append 'Player2' to the text and set the color to player2_color
        else:
            text += 'Player2'
            color = player2_color
        # Delete the previous turn text and create a new text with the updated information
        self.canvas.delete(self.turntext_handle)
        self.turntext_handle = self.canvas.create_text(self.size_of_board - 5*len(text),
                                                       self.size_of_board-self.distance_between_dots/8,
                                                       font="cmr 15 bold",text=text, fill=color)
        '''
        The above method checks whose turn it is by accessing the player1_turn attribute of the instance of the class. Depending on whose turn it is, the method appends the appropriate player number to the text and sets the text color accordingly. The method then deletes the previous turn text (if any) and creates a new text with the updated information at the bottom of the canvas.
        '''

    # This is a method that is triggered whenever a player clicks on the game board
    def click(self, event):
        # Check if the board has not been reset
        if not self.reset_board:
            # Get the position of the click on the grid
            grid_position = [event.x, event.y]
            # Convert the grid position to logical position
            logical_positon, valid_input = self.convert_grid_to_logical_position(grid_position)
            # Check if the input is valid and the logical position is not already occupied
            if valid_input and not self.is_grid_occupied(logical_positon, valid_input):
                # Update the board with the move of current player
                self.update_board(valid_input, logical_positon)
                # Make the edge and check if a box has been marked
                self.make_edge(valid_input, logical_positon)
                self.mark_box()
                # Refresh the board
                self.refresh_board()
                # Switch the player's turn
                self.player1_turn = not self.player1_turn

                # Check if the game is over
                if self.is_gameover():
                    # Display the game over message
                    self.display_gameover()
                else:
                    # Display whose turn it is
                    self.display_turn_text()
        else:
            # Reset the board
            self.canvas.delete("all")
            self.play_again()
            self.reset_board = False

# This code defines a function called startgame that creates an instance of the Dots_and_Boxes class and starts the main event loop
def startgame(toClose,level):
    toClose.destroy()
    # create an instance of the Dots_and_Boxes class
    game_instance = Dots_and_Boxes(level)
    # start the main event loop
    game_instance.mainloop()

