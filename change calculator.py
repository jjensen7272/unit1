#jacob jensen
#9/21/18
#change sorter

def change():
    #1 get input from user on how much change
    total_change = int(input("add up the change in your pocket and input the total "))
    #2 calculate total for Q N D P
    quarters = total_change // 25
    whats_left = total_change % 25
    dimes = whats_left // 10
    whats_left = whats_left % 10
    nickles = whats_left // 5
    whats_left = whats_left % 5
    cents = whats_left
    
    
    #3 display back to user
    print ("Quarters:", quarters, "\ndimes: ", dimes, "\nnickles:", nickles, "\npennies:", cents)



change()
    
def change2(total_change):
    #1 get input from user on how much change
    total_change = total_change
    #2 calculate total for Q N D P
    quarters = total_change // 25
    whats_left = total_change % 25
    dimes = whats_left // 10
    whats_left = whats_left % 10
    nickles = whats_left // 5
    whats_left = whats_left % 5
    cents = whats_left
    
    
    #3 return value
    return quarters, dimes, nickles, cents

total_change = int(input("add up the change in your pocket and input the total "))
quarters, dimes, nickles, cents = change2(total_change)
print ("Quarters:", quarters, "\ndimes: ", dimes, "\nnickles:", nickles, "\npennies:", cents)



















    
