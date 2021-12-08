from query_helpers.db_flow_helper import *
# db_flow_helper,add_queries,get_data_queries,delete_data_queries import *

print("-------MUSIC DATABASE-------")
main_menu = ("1) SEARCH 2) SEE DATA 3) ADD DATA 4) DELETE DATA 5) FUN FACT ")
second_menu = ("1) MAIN MENU 2) EXIT")
stay = True


while stay is True:

    first_choice = int(input(f"{main_menu}"))
    if first_choice == 1:
        seach_in_db()    
    elif first_choice == 2:
        show_data()   
    elif first_choice == 3: 
        update_database()   
    elif first_choice == 4:
        delete_data()
    elif first_choice == 5:
        fun_fact()
    else:
        print('wrong input')  

    second_choice = int(input(f"{second_menu}"))
    if second_choice ==2:
        stay = False 
                     

