import curses
from os import times
from database import run,get,run_many,get_id
from music_data import artists, albums, songs,cross_table
from query_helper import *
from curses import wrapper
title = "MUSIC DATABASE" 
main_menu = 'Search'
def main(stdscr):
    stdscr.clear()
    #add text
    stdscr.addstr(0,20,"MUSIC DATABASE")


    stdscr.refresh()
    stdscr.getch()



    curses.init＿pair(1,curses.COLOR_BLUE, curses.COLOR_WHITE)
    curses.init＿pair(2,curses.COLOR_GREEN, curses.COLOR_WHITE)
    BLUE_AND_WHITE = curses.color_pair(1)
    GREEN_AND_WHITE = curses.color_pair(2)
    window = curses.newwin(3,18,2,2)
    for i in range(100):
        window.clear()
        color = BLUE_AND_WHITE
    if i % 2 == 0:
        color = GREEN_AND_WHITE  
        stdscr.addstr(5,10,"MUSIC DATABASE")   
        window.refresh()
        times.sleep(0.2)
    stdscr.getch()

wrapper(main)


