#-*- coding: utf-8 -*-
'''
Author: Alberto Ferreira
Course: Datastructures and algorithms (Umeå University)
Teacher: Lena Kallin Westin
Python 3.3
'''
import string
import random
import sys

from DirectedList import *

#function to read a directed list.
def read_DirList(dir_list):
    pos = dir_list.first()
    while dir_list.isEnd(pos) != True:
        print (dir_list.inspect(pos))
        pos = dir_list.next(pos) 
    
#Function that will sort the list. The input needed is a list, the position of the letter, the place that will be sorted and a final list
#where the first time should be a empty list ([]).
def radix_sort(test, position, letter_place, final_list):        
    #This part will check if the list given is a python list. In that case, the python list will be transformed to a directedlist
    if type(test) is list:
        temp_list = DirectedList()
        temp_pos = temp_list.first()
        for i in test:
            temp_list.insert(temp_pos, i)
            temp_pos = temp_list.next(temp_pos)        
        d_list = DirectedList()
        pos = d_list.first()        
        for i in test:
            d_list.insert(pos, i)
            pos = d_list.next(pos)
        test = d_list
          
    #It will check if the list has one item or no item (that does not need to be sorted)
    pos = test.first()
    #list with no item
    if (test.isEnd(pos) == True):
        pass
    
    #The item is the last one in the list, in that case it will be appended to the final list because it means it is sorted.    
    if (test.isEnd(test.next(pos))):        
        final_list.append(test.inspect(test.first()))
        return test.inspect(test.first())

    #variable needed to make the right amount of empty lists where in a later moment it will needed for the sorting
    #originally I used "place =  ord('ü') - ord(' ')" where ü would give 252 and ' ' would give 32 (max and min) but since may be
    #some other word that I could't think of, I will just write a little higher number than 252-32=220.
    place =  250

    #creating empty lists for the sorting placement
    x_list = DirectedList()    
    pos = x_list.first()
    for x in range(place+2):
        x_list.insert(pos, DirectedList())
        pos = x_list.next(pos)    
    
    
    pos = test.first()    
    #read each word from the "main" list and place in the right sorting list
    while test.isEnd(pos) != True:
        #word by word        
        i = test.inspect(pos)
        i_p = i[position]
        #In the case the position is the rating, this dictionary is needed for the right sorting.
        if position == 3:
            dic = {'NR-': '01', 'NR': '02', 'NR+': '03', 'G-': '04', 'G': '05', 'G+': '06', 'VG-': '07', 'VG': '08', 'VG+': '09', 'M-': '10', 'M': '11', 'M+': '12'}
            i_p = dic[i_p]
        
        #which position the word will be placed        
        if len(i_p)-1 >= letter_place:            
            nr = ord(i_p[letter_place]) - ord(' ')              
            pos2 = x_list.first()        
            for j in range(nr+1):            
                pos2 = x_list.next(pos2)        
            
            #inserting the word in the right list in the right position                        
            x_list.inspect(pos2).insert(x_list.inspect(pos2).first(), i)                            
            pos = test.next(pos)

        #This is in the case of the word be repeated word, then it does not need to recheck.            
        else:
            final_list.append(i)            
            pos = test.next(pos)            
   
    pos = x_list.first()    
    while x_list.isEnd(pos) != True:
        #it will check each list from the x_list
        a = x_list.inspect(pos)
        #if there is some item in the list:                        
        if a.isempty() != True:            
            pos3 = a.first()
            Lash = []
            #now it will check each item from the list            
            while a.isEnd(pos3) != True:                                
                Lash.append(a.inspect(pos3))            
                pos3 = a.next(pos3)
            #it will sort each letter of each item (for example if it is the words: Ad and Ab they are saved in a list and resorted)            
            Lash = radix_sort(Lash, position, letter_place+1, final_list)                
        pos = x_list.next(pos)
    return (final_list)


#this function will print the sorted list for a better visualisation.
def header(listan):    
    print ("%-40s %-40s %-3s %-5s" %("ARTIST","ALBUM", "TYPE", "RATE"))
    lines = 0
    print (listan[-1])
    for i in listan:
        lines +=1
        #This will stop the list after each 20 lines
        if lines%20 == 0:
            print ("Press b to go back to main menu, q to quit or any other button to continue")
            answer = input ("")
            if answer == 'b':
                sort_menu(listan)
            elif answer == 'q':                
                sys.exit("Thank you for using this software. If you like it, donate to the owner ;)")                
            else:
                print ("%-40s %-40s %-3s %-5s" %("ARTIST","ALBUM", "TYPE", "RATE"))
        artist = i[0]
        album = i[1]
        typ = i[2]
        betyg = i[3]
        print ("%-40s %-40s %-3s %-5s" %(artist, album, typ, betyg))
        #If the list gets to the last item, then the user will have the option to go back or to quit.
        if i == listan[-1]:
            print ("End of list. Press b to go back to the main menu or q to quit.")
            last_answer = input (" ")
            if last_answer == 'q':
                sys.exit('Thank you for using this software. If you like it, donate to the owner ;)')
            elif last_answer == 'b':
                main_menu(listan)
            else:
                input ("Please press b (main menu) or q (quit): ")
                        

#function to open the file
def open_file(text):
    filen = open(text, 'r')
    lines = filen.readlines()
    all_file = []        
    for i in lines:
        i = i.strip()
        i = i.split(";")
        all_file.append(i)            
                
    return all_file

#this function is just for aesthetics where when the program is started this will be shown 
def head_menu():
    print ("************************************************************")
    print ("********* Welcome to Albertos sorting list program **********")
    print ("")
    main_menu([])
    
#this is the first menu of the program where the user can opt for open a list, sort/print the list or quit.
def main_menu(listan):
    print ("****************** Main Menu *******************************")
    print ("Choose your option:")
    print ("1. Open list")
    print ("2. Sort and print list")    
    print ("3. Quit")
    answer = input("(Press 1, 2, or 3 (and Enter) for your choice: ")
    if answer == '1':
        listan = open_menu()        
        main_menu(listan)    
    elif answer == '2':
        listan = sort_menu(listan)                        
    elif answer == '3':
        sys.exit('Thank you for using this software. If you like it, donate to the owner ;)')
    else:
        main_menu(listan)
        
#This function will open predetermined files or one where the user can choose him/herself        
def open_menu():
    print ("****************** Open list menu **************************")
    print ("Choose your option:")
    print ("1. Open data100poster.txt")
    print ("2. Open dataAllaPoster.txt")
    print ("3. Choose your own txt file")        
    print ("4. Quit")
    answer = input("(Press 1, 2, 3, or 4 (and Enter) for your choice: ")
    if answer == '1':
        try:
            result = open_file('data100poster.txt')
        except:            
            sys.exit("The file you tried to open does not exist. Be sure to have the file in the right path and to write the right name.\nThe program will quit now.")        
    elif answer == '2':
        try:
            result = open_file('dataAllaPoster.txt')
        except:
            sys.exit("The file you tried to open does not exist. Be sure to have the file in the right path and to write the right name.\nThe program will quit now.")
    elif answer == '3':
        try:
            result = open_file(input("Write the name of the file (make sure you have the file and that you write .txt in the end: "))
        except:
            sys.exit("The file you tried to open does not exist. Be sure to have the file in the right path and to write the right name.\nThe program will quit now.")        
    elif answer == '4':
        sys.exit('Thank you for using this software. If you like it, donate to the owner ;)')
    return result    
        
#Here the user can choose between sort the list by artist, album, type or rating and print the list.
def sort_menu(listan):    
    print ("*********************** Sorting menu ***********************")
    print ("")
    print ("Choose your option:")
    print ("1. Sort your list by artist")
    print ("2. Sort your list by album")
    print ("3. Sort your list by type of record")
    print ("4. Sort your list by rate")
    print ("5. Print the list")
    print ("6. Back to main menu")
    print ("7. Quit")
    answer = input("(Press 1, 2, 3, 4, 5 or 6 (and Enter) for your choice: ")
    #1 will sort by artist    
    if answer == '1':
        try:
            print ("Sorting list by artist...")               
            listan = radix_sort(listan,0, 0, [])        
            print ("Done.")                                   
            sort_menu(listan)
            return listan
        except:
            sys.exit("You have to open a file first. Open the program again and choose open file before trying to sort.")
    #2 will sort by album
    elif answer == '2':
        try:        
            print ("Sorting list by album...")        
            listan = radix_sort(listan,1, 0, [])                
            print ("Done.")               
            sort_menu(listan)
            return listan
        except:
            sys.exit("You have to open a file first. Open the program again and choose open file before trying to sort.")
    #3 will sort by type
    elif answer == '3':
        try:
            print ("Sorting list by type...")
            listan = radix_sort(listan, 2, 0, [])        
            print ("Done.")        
            sort_menu(listan)
            return listan
        except:
            sys.exit("You have to open a file first. Open the program again and choose open file before trying to sort.")
    #4 will sort by rate
    elif answer == '4':
        try:
            print ("Sorting list by rate...")
            listan = radix_sort(listan, 3, 0, [])
            print ("Done.")        
            sort_menu(listan)
            return listan
        except:
            sys.exit("You have to open a file first. Open the program again and choose open file before trying to sort.")
    elif answer == '5':
        header(listan)
    elif answer == '6':
        main_menu(listan)
    elif answer == '7':
        sys.exit('Thank you for using this software. If you like it, donate to the owner ;)')    
    return listan

if __name__ == "__main__":
    head_menu()