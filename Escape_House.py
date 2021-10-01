#==========ESCAPE HOUSE=============
# Project by : DHANESH GAURI


thief = 0

code = 0
bullets = 0
gun = 0
fire = False
car_keys = 0
time = 0
class Room1:
   
    def sneakWindow(self):
        self.window = print('''\tYou Find out no one is out there 
        You are in first floor of a bunglow
        You can see lobby to other rooms and stairs to downwards''')
        
        return self.window

    def openDoor(self):
        global thief
        if thief == 0:
            print("the door is locked I need to find something to open the door")
            
        elif thief == 1:
            print("You want to open the door\n1. open door\n2. dont open the door")
            c = int(input("Enter the option: "))
            
            if c== 1:
                print("You open the door [Skill Aquired: Thief]")  
                return False  
            elif c == 2:
                print("you choose to stay inside")
                opendoor = room1.openDoor()
            else: 
                print("Invalid Choice")
                opendoor = room1.openDoor()
    def search(self):
         while(True):
                print('''
                Searching options:
                1. Under the bed
                2. open 1st drowr
                3. open 2nd drowr
                4. leave searching''')
            
                search = int(input("Enter the option: "))
                
                if search == 1:
                    print("there is nothing in here")
                    
                elif search == 2:
                    print('''\n\n\tSome paper clips and screwdriver [Common Items]\n
                    (this might help to unlock the door, Now you have skill to unlock the Door Locked With Keys)\n\n''')
                    
                    global thief
                    thief = 1
                elif search == 3:
                    print("sissor is here\n1. keep it\n2. leave it")

                    sis = int(input("Enter the option: "))
                    if sis == 1:
                        print("you have sissor now")
                        
                    else:
                        print("you choose to leave the sissor")
                elif search == 4:
                    return False
                else:
                    print("invalid choice")
room1 = Room1()


class Room2:
    def sneakWindow(self):
        self.sneak = print("\n\nThe room looks Empty *(There might be something Useful in there)\n")
        
        return self.sneak

    def insideOfRoom2(self):
        self.room = print('''
        There is one window which opens outside.
        There's an empty table with two drowrs in.
        And the rest of the room is empty
        ==============================================
        ''')
        return self.room

    def search(self):
        while(True):
            print('''
            1. look from Window
            2. look in drowr 1
            3. look in drowr 2
            4. leave room
            ''')
            c = int(input("Enter the option: "))
            if c == 1:
                print('''\tThe bunglow is in the middle of the jungle
                There is a long rope hanging from a window,
                do you want to climb down the rope to escape the house?
                ============================================================
                press "Y" for yes
                press "N" for no''')
                
                c = input("Enter the option: ")
                if c == "y":
                    print('''\t[ ACT OF FOOLISHNESS ]\n\n
                    You fell down while climbing down the rope because of your ankel,
                    kidnappers heard the sound and come for you and shoot you
                    \n\tYOU DIED ''')
                    exit()
                elif c == "n":
                    
                    continue
                else:
                    print("\n\nInvalid Choice\n\n")
                    
            elif c == 2:
                print('''
                You found a GUN [Unique Item Found]\t*(but you never handel a gun in your life)
                1. take it
                2. leave it
                ''')
                gunChoice = int(input("Enter your choice: "))
                if gunChoice == 1:
                    
                    print("You have a GUN now")
                    global gun
                    gun = 1
                elif gunChoice == 2:
                    gun = 0
                else:
                    print("\n\ninvalid choice\n\n")
            elif c == 3:
                print("\nthere is nothing in here\n")
                
            elif c == 4:
                return False
            else:
                print("Invalid Choice")
room2 = Room2()

class Room3:
    def sneakWindow(self):
        self.sneak = print('''
                    *There are two men Dirnking Beer*\n 
                    Charls --> "This is a shitty job! Kevin, Where are the car keys? I need to get out from this jungle
                                as soon as possible"
                    Kevin --> "Relax Charls! The Guard has the keys, and you know he is directly under our boss
                                You can't take the keys from him, so just relax and drink with me"
                    \n(They look preety relaxed,There might be a chance that I took both of them with my GUN) 
                    =====================================================================================================''')
        
                    
        return self.sneak

    def openDoor(self):
        global gun
        if gun == 0:
            print('''
            You don't have a appropriate weapon
            to kill the kidnappers
            They kill you the instant they saw you
            
            [YOU DIED]
            ''')
            exit()
        elif gun == 1:
            print('''
            [THERE IS THIN LINE BETWEEN BRAVERY AND STUPIDITY]\n\n
            Your gun is empty, that gun fire BLANKS at the kidnapper,
            they took their gun and shoot at you
            \t\nYOU DIED''')
            exit()
        else:
            print("Invalid Choice")
room3 = Room3()

class MainDoor:
    def sneakWindow(self):
        self.sneak = print('''
        There is Guard with a Gun in his hand.
        And a car is parked in front of the house.
        There is only car that is here 
        If I drove away with this car no one could follow me
        I hope Guard have car-keys 
        This door is the only way to escape from this house 
        ==============================================================
        ''')
        
        return self.sneak

    def openDoor(self):
        global code
        if code == 0:
            print('''
            This door have a number locked system, can't be open with thief skill
            I need to find the 6 digit code to open this door''')
            
        elif code == 1:
            co = input("Enter code:  ")
            if co == "416121":
                print("\nYou open the door\n")
                
                return False
            else:
                print('''
                Due to wrong code the siren went on,
                all the mens come to kill you.
                \t\nYOU DIED ''')
                exit()
maindoor = MainDoor()


class Kitchen:
    def insideOfKitchen(self):
        self.kitchen = print('''
        This is a dirty and old kitchen with so many drowrs
        ''')
        
        return self.kitchen
        
    def search(self):
        while(True):
            print('''
            0. leave Kitchen
            searching options:
            1. Oven
            2. Refrigirator
            3. drowr-3
            4. drowr-4
            5. drowr-5
            6. drowr-6
            7. drowr-7
            8. drowr-8
            9. drowr-9
            10. drowr-10 ''')
            c = int(input("Enter your option: "))
            if c == 1:
                print("Just an old pizza inside it (There are important things right now than just eating food)")
                
            elif c == 2:
                print('''
                =================================================
                |              REFRIGIRATOR NOTE                |
                |     TO,                                       |
                |        unlucky 6 & unlucky 8                  |
                |                                               |
                |        DOOR CODE : 416121                     |
                |                                               |
                |                    FROM,                      |
                |                         lucky 7               |
                =================================================
                ''')
                
                global code
                code = 1
            elif c == 7:
                print("Knife is here\n1. take it\n2. leave it\n")
                ch = int(input("Enter your choice: "))
                if ch == 1:
                    print("You have knife now [Rare Item]")
                    
                    global knife
                    knife = 1
                elif ch == 2:
                    print("you choose to leave knife")
                else:
                    print("Invalid Choice")
            elif c == 6 or c == 8:
                print('''
                The drowr was already Rusted
                all the utensils in the drowr fell down & make noise
                All the men come to kitchen & shoot you
                \n\tYOU DIED ''')
                exit()
            elif c == 0:
                return False
            elif c<=10:
                print("There is nothing useful in it")
                
            else:
                print("Invalid Choice")
kitchen = Kitchen()

class GroundRoom1:
    def sneakWindow(self):
        self.sneak = print('''
        This room is empty
        A dead body lying on the ground
        An empty table with some drowrs
        Better hurry to make decision before someone come''')
        
        return self.sneak
    
    def insideOfRoom(self):
        while(True):
            print('''
            0. To leave the room
            1. Search the dead body
            2. Drowr1
            3. Drowr2 ''')
            c = int(input("Enter your choice: "))
            if c == 0:
                return False
            elif c == 1:
                
                print(''' 
                ==========================================
                Chemical Plant ID:  
                Name - Dr. James Kennedy
                Age  - 38 yrs
                Designation - Reacher in Bio Chemical Developer
                ID No. - t0ps3(r3t
                ==========================================

                And you find two bullets that matches Your GUN


                1. Take bullets
                2. Leave bullets
                ''')
                b = int(input("Enter option: "))
                if b == 1:
                    
                    global bullets
                    bullets = 1
                    print("You have bullets now")
                elif b == 2:
                    print("You choose to leave the bullets")
                else:
                    print("Invalid Choice")
            elif c == 2 or c == 3:
                print("There is nothing in here")
                
            else:
                print("Invalid Choice")
groundroom1 = GroundRoom1()


class GroundRoom2:
    def sneakWindow(self):
        self.sneak = print('''
        There are 4 people sitting in a round table
        Discussing something in low voice (coudn't hear properly what they are saying) 
        It's better to not interfear this room
        I don't think that I can handel all of them
        Better find a way to Escape this House
        =================================================================================''')
         
groundroom2 = GroundRoom2()

class Final_Area:
    global bullets
    global car_keys
    global time
    def bullet(self):
        
        if bullets == 0:
            print('''
            Your GUN is empty
            You fire BLANKS at the guard
            The Guard fire back at You
            \n\n[YOU DIED]
            ''')
            exit()
        elif bullets == 1:
            print('''
            You have to kill the Guard with your GUN
            Before he Notice!
            ===========================================================
            1. Fire one Bullet (You got one bullet left in your GUN)
            
            2. Fire both the Bullet (Make sure he's DEAD) ''')
            check = int(input("Enter Bullet Option: "))
            if check == 1:
                global fire
                fire = False
                print("\nYou choose to fire one bullet\n")
            elif check == 2:
                
                fire = True
                print("\nYou choose to fire Both the Bullets\n")
    def Last_options(self):
        
        options = True
        while(options == True):
            print(''' 
            Hurry up! All the people heard the gun shot 
            Escape from house before the people come for you!
            =================================================
            
            1. Run towards the forest 
            2. Run towards the car
            3. Search the Guard's Body
            ''')
            
            
            c = int(input("Enter option: "))
            if c == 1:
                print('''
                [ACT OF FOOLISHNESS]
                
                You can't outrun all the kidnappers
                They find you and kill you 
                
                [YOU DIED]
                ''')
                exit()
            if c == 2:
                global time
                global car_keys
                if car_keys == 0:
                    
                    print('''
                    You don't have the car keys
                    Guard must have the keys to the car''')
                    time += 1
                
                elif car_keys == 1:
                    if time == 0:
                        print('''
                        ****************** CONGRATULATION YOU WON THE GAME ******************
                        
                        TOU TAKE THE CAR AND GET AWAY FROM KIDNAPPERS
                        THEY DONT HAVE ANY VEICHEL TO CHASE YOU
                        [YOU FIND A MOBILE PHONE IN THE CAR]
                        
                            To be continued....... ''')
                        
                        exit()

                    else:
                        print('''
                        [TIME IS KEY]
                        
                        You take too much time
                        Kidnappers come to the Main Door and shoot you
                         
                        [YOU DIED]
                         ''')
                        exit()
            elif c == 3:
                global fire
                if fire == False:
                    print('''
                    The Guard still alive
                    When you go towards the Guard. He shot you rapidly 3 times 
                    
                    [YOU DIED]
                    
                    [YOU CAN'T LET GUARD DOWN]
                     ''')
                    exit()
                else:
                    while(c == 3):
                        
                        
                        print('''
                        Searching option's
                        0. Leave searching
                        1. Take Guard's GUN from his hand
                        2. Flip the Guard and take extra bullets from guard's back pocket
                        3. Take car keys from his waist
                        4. Remove the Belt and Take Guard's torch
                        5. Take Guard's Mobile Phone from his pant's pocket
                        6. Take Guard's Wallet from his back pocket
                        ''')
                        c = int(input("Enter option: "))
                        if c == 0:
                            break
                        elif c == 1:
                            print("\nYou got the GUN\n")
                            
                        elif c == 2:
                            print("\nYou goy extra bullets\n")
                            time +=1
                        elif c == 3:
                            print("\nYou got the car keys\n")
                            
                            car_keys = 1
                        elif c == 4:
                            print("\nyou got the Guards torch\n")
                            time +=1
                        elif c == 5:
                            print("\nYou got the Guard's Mobile Phone\n")
                            time +=1
                        elif c == 6:
                            print("\nYou got the Guard's Wallet\n")

final_area = Final_Area()

if __name__=="__main__":
    print('''
    You are an important witness to a crime
    But, You have been kidnapped
    You are unconcious for long time
    When you open your eyes you are in a room
    You have no idea! where are you ?
    Your ankel is broken, you couldn't run
    All you have to do is walk
    You need to get out of this place and reach safe point 
    ========================================================''')
    while(True):
        print('''
        choose an option :
        1. Sneak from window to look outside the room
        2. Open the door and go outside
        ''')
   
        ch = int(input("Enter option: "))
        if ch == 1:
            room1.sneakWindow()
        elif ch == 2:
            if room1.openDoor() == False:
                break
            else:
                room1.openDoor()
                print("I need to search the room")
                room1.search()
    
     
    print('''
    Now You entered the lobby area

    There are two different rooms in lobby
    It's better to keep the rooms check before going downwards
    =============================================================''')
    lobby = True
    room_check = 0

    while(lobby == True):
        print('''
        1. check Room Left
        2. check Room Right ''')
        if room_check >= 2:
            print('''
            (Both the rooms are checked you can leave lobby now
            But keep it in mind once you leave the lobby area there is no point for coming back
            )
            3. leave lobby and go to downstairs
            ''')
            if c == 3:
                print('''
                Are you sure to leave the lobby?

                "y" for YES
                "n" for NO
                ''')
                op = input("Enter option: ")
                if op == "y":
                    break
                elif op == "n":
                    continue
                else:
                    print("Invalid Choice")
        c = int(input("Enter room option: "))
        if c == 1:
            while c == 1:
                print('''
                1. sneak window to look inside the room left
                2. open door and go inside to room left
                0. Goto lobby area''')
                check = int(input("Enter option: ")) 
                if check == 1:
                    room2.sneakWindow()
                    room_check +=1
                elif check == 2:
                    room2.insideOfRoom2()
                    print("\n\nI need to search this room\n\n")
                    if room2.search() == False:
                        continue
                    else:
                        room2.search()
                elif check == 0:
                    break
                else:
                    print("Invalid Choice")
        
        elif c == 2:
            while c == 2:
                print('''
                1. sneak window to look inside the room right
                2. open door and go inside to room right
                0. Goto lobby area''')
                window_see = 0
                check = int(input("Enter option: "))
                if check == 1:
                    room3.sneakWindow()
                    window_see = 1
                    room_check +=1
                elif check == 2:
                    if window_see == 1:
                        Room3.openDoor()
                    elif window_see == 0:
                        print('''
                        [You are not a hero you are a survivor]

                        There are two men present in the room 
                        who shot You the instant they saw you
                        \n\n[YOU DIED]
                        ''')
                        exit()
                elif check == 0:
                    break
                else:
                    print("Invalid Choice")
        
        else:
            print("Invalid Choice")
    


    print('''
    Now you entered the downstairs hall
    no one present in the hall
    There is a main door of EXIT 
    two rooms and a open Kitchen
    =======================================
    ''')
    hall = True
    while(hall == True):
        print
        ('''
        1. check main door
        2. check Kitchen 
        3. check Room1
        4. check Room2
        ''')
        check = int(input("Enter option: "))
        
        if check == 1:
            print('''
            1. Sneak window to look outside the house
            2. Open main door''')
            c = int(input("Enter option: "))
            if c == 1:
                maindoor.sneakWindow()
            elif c == 2:
                if maindoor.openDoor() == False:
                    break
                else:
                    maindoor.openDoor()
            else:
                print("Invalid Choice")
        elif check == 2:
            print('''
            1. Look inside the Kitchen
            2. Search Kitchen''')
            c = int(input("Enter option: "))
            if c == 1:
                kitchen.insideOfKitchen()
            elif c == 2:
                if kitchen.search() == False:
                    continue
                else:
                    kitchen.search()
        elif check == 3:
            print('''
            1. Sneak window to look inside the room1
            2. Go inside the room''')
            c = int(input("Enter option: "))
            if c == 1:
                groundroom1.sneakWindow()
            elif c == 2:
                if groundroom1.insideOfRoom() == False:
                    continue
                else:
                    groundroom1.insideOfRoom()
        elif check == 4:
            groundroom2.sneakWindow()
    
    final_area.bullet()
    final_area.Last_options()

    
