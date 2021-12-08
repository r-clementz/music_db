from query_helper import *
from search_queries import *
from add_queries import *
from get_data_queries import *
from delete_data_queries import *

#UPDATE FUNCTIONS
def update_database():
    print('1. ADD NEW DATA 2. UPDATE EXISTED INFO ')
    update_choice = input('Please Choose:')
    if update_choice == 1:
    
        add_choice = int(input('ADD.. 1. Artist 2.Album 3. Song'))
        if add_choice == 1:
            add_artist()
        elif add_choice == 2:
            add_album()
        elif add_choice == 3: 
            add_song()    
        else:
            print('Wrong input')       

    elif update_choice == 2:
        update_menu =int(input('1. Update album released year 2. More feature comming soon'))
        if update_menu == 1:
            update_released_year()
        elif update_menu == 2:
            print ('This feature coming soon! ')
        else: 
            print('Wrong input') 

#DELETE FUNCTIONS
def delete_data():
    delete_choice = int(input('DELETE.. 1. Artist 2.Album 3. Song'))

    if delete_choice == 1:
        delete_artist()    
    elif delete_choice == 2:
        delete_album()
    elif delete_choice == 3: 
        delete_song()    
    else:
        print('Wrong input') 

#SEACH FUNCRIONS 
# aritst_search, song_search, album_search, search_in_db
def artist_search():
    search_name =  input('Name or Keyword to search an artist: ')
    search_result = search_artist(search_name)
    
    if search_result is True:
        further_choice= int(input('Check the album(s) for this artist?\n 1. Yes 2.No'))
        if further_choice == 1:
            all_albums_of_artist(search_name)
            
            fur_more_choice = int(input('1.Check more detail 2.Exit'))
            if fur_more_choice == 1:
                get_album_list_w_details(search_name)
                
                last_choice = int(input('Go furhter! 1. number of songs & duration  2. All songs 3. Exit')) 
                if last_choice == 1:
                    get_nr_of_songs_and_total_durations(search_name)
                elif last_choice == 2:     
                    get_all_songs_in_albums_w_details(search_name)
                else: 
                        pass    
            
            else: 
                    pass 
    else:
        pass  

def song_search():     
    search_name = input('Name or Keyword to search a song: ')
    search_result = search_song(search_name)
   
    if search_result is True:
         further_choice= int(input('Check the album(s) for this artist?\n 1. Yes 2.No'))
         if further_choice == 1:
            get_album_list_w_details
            fur_more_choice = int(input('1.Check more detail 2.Exit'))
            
            if fur_more_choice == 1:
                get_album_list_w_details(search_name)
                
                last_choice = int(input('Go furhter! 1. number of songs & duration  2. All songs 3. Exit')) 
                if last_choice == 1:
                    get_nr_of_songs_and_total_durations(search_name)
                elif last_choice == 2:     
                    get_all_songs_in_albums_w_details(search_name)
                else: 
                        pass    
            
            else: 
                    pass 
    else:
        pass  

def album_search():
    search_name = input('Name or Keyword to search an album: ') 
    search_result = search_song(search_name)
   
    if search_result is True:
        further_choice= int(input('Check the artist for this song?\n 1. Yes 2.No'))
        if further_choice == 1:
           get_number_of_songs_in_albums(search_name) 
           get_longest_song_in_album()

    else:
        pass    

def seach_in_db():
    search_choice = int(input('SEARCH... 1. Artist 2.Album 3. Song'))
    if search_choice == 1:
           artist_search()
    elif search_choice == 2:
            album_search()
    elif search_choice == 3: 
            song_search()    
    else:
            print('Wrong input')

def fun_fact():
    fact_choice = int(input('''DO YOU WANNA KNOW... 
    1. Average duration of all songs 2. Oldest Album in db 3. Longest Albun in db'''))            
    if fact_choice == 1:
       get_average_duration_of_songs()
    elif fact_choice == 2: 
        print_oldest_album()
    elif fact_choice == 3:
        print_longest_album()
    else: 
        pass 

def show_data():
    data_choice =int(input('SEE 1.All Aritists 2. All albums 3. All songs '))
    if data_choice == 1:
        print_all_artists()
    elif data_choice == 2:    
        print_all_albums()
    elif data_choice == 3: 
        print_all_songs()    
            
