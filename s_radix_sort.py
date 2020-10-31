from DirectedList import *


def read_DirList(dir_list):
    pos = dir_list.first()
    while dir_list.isEnd(pos) != True:
        print (dir_list.inspect(pos))
        pos = dir_list.next(pos) 
    
#Function that will sort the list. The input needed is a list and the place of the letter.
def radix_sort(test, position, letter_place = 0, final_list = []):
    #print (final_list)    
    #This part will check if the list given is a python list. In that case, the python list will be transformed to a directedlist
    if type(test) is list:
        temp_list = DirectedList()
        temp_pos = temp_list.first()
        for i in test:
            temp_list.insert(temp_pos, i)
            temp_pos = temp_list.next(temp_pos)
        #read_DirList(temp_list)
        d_list = DirectedList()
        pos = d_list.first()        
        for i in test:
            d_list.insert(pos, i)
            pos = d_list.next(pos)
        test = d_list
          
    #It will check if the list has one item or no item (that does not need to be sorted)
    pos = test.first()
    #list with 1 item
    
        
    if (test.isEnd(pos) == True):
        pass
    
    #list with no item
    
    if (test.isEnd(test.next(pos))):    
        #print (test.inspect(test.first()))
        final_list.append(test.inspect(test.first()))
        return test.inspect(test.first()) 
    
    
    

    #variable needed to make the right amount of empty lists where in a later moment it will needed for the sorting
    place =  ord('z') - ord('0')
    
    #creating empty lists for the sorting placement
    x_list = DirectedList()    
    pos = x_list.first()
    for x in range(place+1):
        x_list.insert(pos, DirectedList())
        pos = x_list.next(pos)    
    
    
    pos = test.first()    
    #read each word from the "main" list and place in the right place
    while test.isEnd(pos) != True:
        #word by word        
        i = test.inspect(pos)
        #which position the word will be placed
        #print ('fl', final_list)
        #print (i)
        #if len(final_list) > 0:
            #if (final_list[-1] == i):
                #print ("equal")
        #print (i, letter_place)
        if len(i[position])-1 >= letter_place:
            #print (letter_place)
            #print (i[position])        
            nr = ord(i[position][letter_place]) - ord('0')              
            pos2 = x_list.first()        
            for j in range(nr+1):            
                pos2 = x_list.next(pos2)        
            
            #inserting the word in the right list
            x_list.inspect(pos2).insert(x_list.inspect(pos2).first(), i)                
            pos = test.next(pos)
            
        else:
            final_list.append(i)            
            print (i)
            pos = test.next(pos)
                      

    

    #Checking each item from the list x_list
    pos = x_list.first()    
    while x_list.isEnd(pos) != True:
        #it will check each list from the x_list
        a = x_list.inspect(pos)
        #if there is some item in the list:                        
        if a.isempty() != True:            
            pos3 = a.first()
            Lash = []
            #now it will check each item from the list a            
            while a.isEnd(pos3) != True:                                
                Lash.append(a.inspect(pos3))            
                pos3 = a.next(pos3)
            #it will sort each letter
            #print (Lash)
            #print (Lash[-1])            
            #print (Lash)
            Lash = radix_sort(Lash, 0, letter_place+1, final_list)            
            #print (final_result)
                                    
            #if Lash != None:                
                #final_result.append(Lash)
            
                
        pos = x_list.next(pos)
    print (final_list)
    #print (len(final_list))
    return (final_list)

def header():    
    print ("%-40s %-40s %-3s %-5s" %("ARTIST","ALBUM", "TYP", "BETYG"))

def open_file(text):
    filen = open(text, 'r')
    lines = filen.readlines()
    all_file = []        
    for i in lines:
        i = i.strip()
        i = i.split(";")
        all_file.append(i)            
        #artist = i[0]
        #album = i[1]
        #typ = i[2]
        #betyg = i[3]
        #print ("%-40s %-40s %-3s %-5s" %(artist, album, typ, betyg))        
    return all_file


L = open_file('data100poster.txt')
print (L)
asdsaa = [['aaa', 'ggg'], ['ddd', 'ccc'], ['abb', 'lll']]

tas = radix_sort(L, 0)
print (tas)
