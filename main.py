player_1 = "X"
player_2 = "O"

box_1 = " "
box_2 = " "
box_3 = " "
box_4 = " "
box_5 = " "
box_6 = " "
box_7 = " "
box_8 = " "
box_9 = " "

boxes = [box_1, box_2, box_3, box_4, box_5, box_6, box_7, box_8, box_9]

def print_board():
    print(f"|{boxes[0]}|{boxes[1]}|{boxes[2]}|")
    print(f"|{boxes[3]}|{boxes[4]}|{boxes[5]}|")
    print(f"|{boxes[6]}|{boxes[7]}|{boxes[8]}|")


while True:    

    print_board()

    position = int(input("Select position: "))

    position -= 1

    boxes[position] = input("Fill with X or O: ")

    if (boxes[0] == player_1 and boxes[1] == player_1 and boxes[2] == player_1) \
            or (boxes[0] == player_1 and boxes[3] == player_1 and boxes[6] == player_1) \
            or (boxes[3] == player_1 and boxes[4] == player_1 and boxes[5] == player_1) \
            or (boxes[1] == player_1 and boxes[4] == player_1 and boxes[7] == player_1) \
            or (boxes[0] == player_1 and boxes[4] == player_1 and boxes[8] == player_1) \
            or (boxes[2] == player_1 and boxes[5] == player_1 and boxes[8] == player_1) \
            or (boxes[6] == player_1 and boxes[7] == player_1 and boxes[8] == player_1) \
            or (boxes[2] == player_1 and boxes[4] == player_1 and boxes[6] == player_1):
        print("Player 1 wins")
        break
    elif (boxes[0] == player_2 and boxes[1] == player_2 and boxes[2] == player_2) \
            or (boxes[0] == player_2 and boxes[3] == player_2 and boxes[6] == player_2) \
            or (boxes[3] == player_2 and boxes[4] == player_2 and boxes[5] == player_2) \
            or (boxes[1] == player_2 and boxes[4] == player_2 and boxes[7] == player_2) \
            or (boxes[0] == player_2 and boxes[4] == player_2 and boxes[8] == player_2) \
            or (boxes[2] == player_2 and boxes[5] == player_2 and boxes[8] == player_2) \
            or (boxes[6] == player_2 and boxes[7] == player_2 and boxes[8] == player_2) \
            or (boxes[2] == player_2 and boxes[4] == player_2 and boxes[6] == player_2):
        print("Player 2 wins")
        break
        
