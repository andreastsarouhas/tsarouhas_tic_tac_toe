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

        position = int(input("Select position: ")) - 1
        
        if not position <= 8 and position >= 0:
            print("Position out of range")
            print_board()
            position = int(input("Select position: ")) - 1

        boxes[position] = input("Fill with X or O: ")

        if not boxes[position] == "X" or boxes[position] == "O":
            print("Invalid input") 
            boxes[position] = input("Fill with X or O: ")

        if (boxes[0] == "X" and boxes[1] == "X" and boxes[2] == "X") \
            or (boxes[0] == "X" and boxes[3] == "X" and boxes[6] == "X") \
            or (boxes[3] == "X" and boxes[4] == "X" and boxes[5] == "X") \
            or (boxes[1] == "X" and boxes[4] == "X" and boxes[7] == "X") \
            or (boxes[0] == "X" and boxes[4] == "X" and boxes[8] == "X") \
            or (boxes[2] == "X" and boxes[5] == "X" and boxes[8] == "X") \
            or (boxes[6] == "X" and boxes[7] == "X" and boxes[8] == "X") \
            or (boxes[2] == "X" and boxes[4] == "X" and boxes[6] == "X"):
            print_board()
            print("Player 1 wins")
            break
        if (boxes[0] == "O" and boxes[1] == "O" and boxes[2] == "O") \
            or (boxes[0] == "O" and boxes[3] == "O" and boxes[6] == "O") \
            or (boxes[3] == "O" and boxes[4] == "O" and boxes[5] == "O") \
            or (boxes[1] == "O" and boxes[4] == "O" and boxes[7] == "O") \
            or (boxes[0] == "O" and boxes[4] == "O" and boxes[8] == "O") \
            or (boxes[2] == "O" and boxes[5] == "O" and boxes[8] == "O") \
            or (boxes[6] == "O" and boxes[7] == "O" and boxes[8] == "O") \
            or (boxes[2] == "O" and boxes[4] == "O" and boxes[6] == "O"):
            print_board()
            print("Player 2 wins")
            break
        
