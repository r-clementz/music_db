import curses
from os import times
from database import run,get,run_many,get_id
from music_data import artists, albums, songs,cross_table
from query_helper import *
from curses import wrapper
title = "MUSIC DATABASE" 
main_menu = 'Search'
print_all_songs()