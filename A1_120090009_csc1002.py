import random #import module
list,list2,direction=[],[],[] #Declare global variables
l,r,u,d,instruction="","","","",""
def output(): #a function to output the sliding puzzle
    global list, dn 
    for i in range(0, dn):
        for k in range(i * dn,(i+1) * dn):
            print(list[k], "\t", end="") 
        print("\n")   #line feed

def move(): #To change the position of numbers according to the instruction of movement
    global list, dn, a
    for i in range(dn**2):
        if list[i] == " ":
            a = i
    if instruction == l: #case left
        list[a], list[a+1]=list[a+1], list[a]
        output()
    if instruction == r: #case right
        list[a], list[a-1]=list[a-1], list[a]
        output()
    if instruction == u: #case up
        list[a], list[a+dn]=list[a+dn], list[a]
        output()
    if instruction == d: #case down
        list[a], list[a-dn]=list[a-dn], list[a]
        output()

def order(): #use letters input by user to represent the instructions
    global l, r, u, d, direction
    while True:
        direction=[]
        try:
            directions = input("enter four letters used to represent left, right, up and down:") 
            for i in directions:
                if i != " " and i != ",":
                    direction.append(i)
            l,r,u,d = direction 
            if l != r != u != d: #avoid robust input 
                break
            else:
                continue   
        except:
            continue      

def produce_valid_puzzle_board():
    global list,list2,dn 
    while True:
        list=[] 
        list2=[]
        for i in range(1,dn**2): #initial board
            list.append(i)
        list.append(" ")
        if dn%2 != 0: #case odd
            random.shuffle(list) #generate the random seed
            inverse_number=0 
            for i in list:
                list2.append(i)
            list2.remove(" ")
            for n in range(dn*dn - 2):
                for i in range(n+1,dn*dn - 1):
                    if list2[n] > list2[i]:
                        inverse_number += 1 #to calculate the inverse number of sliding board
            if inverse_number%2 == 0: #judge odevity of inverse number
                output()
                return list    #if the inverse number is odd, then reproduce the puzzle
            else:
                continue
        if dn%2 == 0: #case even
            random.shuffle(list)
            inverse_number = 0
            for i in list:
                list2.append(i)
            list2.remove(" ") 
            for n in range(dn*dn-2):
                for i in range(n+1,dn*dn-1):
                    if list2[n] > list2[i]:
                        inverse_number += 1
            for i in range(dn**2):
                if list[i] == " ":
                    a=i                                  #a is where the white space initially at 
            if inverse_number%2 == 0:
                if ((dn**2-a)//dn)%2 == 0:     #If the reverse number is even, the difference between the number of lines
                    output()                   #with the current space and the number of lines with the original space is even.
                    break
                else:
                    continue
            else:
                if ((dn**2-1-a)//dn)%2 == 1:  #If the reverse number is odd, the difference between the number of lines 
                    output()                  #with the current space and the number of lines with the original space is odd      
                    break
                else:
                    continue

def instruction_move():
    global instruction, list2, dn, l, u, d, r
    step=0
    while True: #To check the position of blank place and give a unique feedback
        if list[0] == " ": #upper left
            instruction=input("Enter your move(left-"+l+","+"up-"+u+")")
            if instruction == d or instruction == r:
                continue
        for i in range(dn*(dn-1) + 1,dn*dn - 1): #down
            if list[i] == " ":
                instruction = input("Enter your move(right-"+r+","+"left-"+l+","+"down-"+d+")")
                if instruction == u:
                    continue
        if list[dn-1] == " ": #upper right
            instruction=input("Enter your move(right-"+r+","+"up-"+u+")")
            if instruction == d or instruction == l:
                continue
        for i in range(dn*2-1,dn*dn-1,dn): #right
            if list[i] == " ":
                instruction=input("Enter your move(right-"+r+","+"up-"+u+","+"down-"+d+")")
            if instruction == l:
                continue
        if dn > 3: 
            for i in range(dn+1,dn*(dn-1)-1): #middle
                if list[i] == " " and i&dn !=0 and (i-1)&dn != 0:
                    instruction=input("Enter your move(left-"+l+","+"right-"+r+","+"up-"+u+","+"down-"+d+")")
        elif dn == 3:
            if list[4] == " ":
                instruction=input("Enter your move(left-"+l+","+"right-"+r+","+"up-"+u+","+"down-"+d+")")
        for i in range(dn,dn*(dn-1),dn): #left
            if list[i] == " ":
                instruction=input("Enter your move(left-"+l+","+"up-"+u+","+"down-"+d+")")
                if instruction == r:
                    continue
        if list[dn*(dn-1)] == " ": #left lower
            instruction=input("Enter your move(left-"+l+","+"down-"+d+")")
            if instruction == r or instruction == u:
                continue 
        for i in range(1,dn-1): #up
            if list[i] == " " :
                instruction=input("Enter your move(left-"+l+","+"up-"+u+","+"right-"+r+")")
                if instruction == d:
                    continue
        if list[dn**2-1] == " ":  #right lower
            list2.sort()
            if list == list2+[" "]:
                print("Congratulations!","You solved the puzzle in",step,"moves!")
                break
            else:
                instruction = input("Enter your move(right-"+r+","+"down-"+d+")")
                if instruction == l or instruction == u:
                    continue 
        move()
        step += 1
print("Welcome to Junhua’s puzzle game, …..")
while True:
    robust_dn = input("Enter the desired dimension of the puzzle: (with range [3, 10])")
    if robust_dn.isdigit() and 3 <= int(robust_dn) <= 10:
        dn = int(robust_dn)
        order() 
        produce_valid_puzzle_board()
        instruction_move()
        break
    else:
        print('Not valid! Please enter an integer within range [3, 10]')