
class hotel:
    def __init__(self,room_number,guest_name):
        self.room_number=room_number
        self.guest_name=guest_name
        self.occupied=0
        
    def view_rooms(self):
        max_rooms=10
        print("Room\tGuest Name\tOccupied\n");
        for i in range(1,max_rooms+1):
            print(f"room_number {self.room_number}\t\tguest_name {self.guest_name}",end="")
            if (self.occupied): 
                print("Yes\n")
            else: 
                print("No\n")
            break
    
    def add_guest(self):
        room_number=int(input("enter room number"))
        guest_name=input("enter guestname")
        #occupied=int(input("enter number"))
        h=hotel(room_number,guest_name)
        #Initialize all rooms as unoccupied
        for i in range(1,11):
            room_number = i
            guest_name.append("")
            occupied = 0;

# main
while (1):
#  Display menu options
    print("Hotel Management System:\n");
    print("1. View all rooms\n");
    print("2. Add a guest\n");
    print("3. Remove a guest\n");
    print("4. Exit\n");

# Get user choice
    choice=int(input("Enter your choice: "))
    
    if(choice==1):
        #View all rooms
        h.view_rooms()

    if(choice==2):
        
        h.add_guest()
        #Add a guest
        
    if(choice==3):
        #Remove a guest
        room_number=int(input("Enter room number: "))
        if (room_number < 1 or room_number > 11):
            print("Invalid room number. Please try again.\n")
        elif (not(h.room_number - 1 is occupied)):
                    print("Room %d is already unoccupied. Please try again.\n", room_number);
        else:
            rooms[room_number - 1].occupied = 0;
            strcpy(rooms[room_number - 1].guest_name, "");
            printf("Guest removed from room %d.\n", room_number);
            break

    if(choice==4):
    # Exit the program
        print("Exiting program.\n");
        break

            