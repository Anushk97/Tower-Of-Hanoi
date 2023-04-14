import sys

counter = 0
dict_3 = {}
starting_peg = 0

def tower_hanoi(n, state):
    dict_1 = {iter: item for iter, item in enumerate(state)}
    for i, k in dict_1.items():
        for j in k:
            dict_3[j] = i 
    
    def not_moved(n):
        global counter
        global starting_peg
        
        curr_pos = dict_3[n]
        starting_peg = dict_3[n]
        counter = 0
        
        if starting_peg == 0:
            starting_peg = "A"
        elif starting_peg == 1:
            starting_peg = "B"
        elif starting_peg == 2:
            starting_peg = "C"
        
        return compare(curr_pos, n-1)
        

    def moved(n):
        global counter
        global starting_peg

        counter = 0
   
        if n%2 ==0:
            starting_peg = (dict_3[n]+1) % 3
            curr_pos = (dict_3[n]-1) % 3
        elif n % 2 == 1:
            starting_peg = (dict_3[n]-1) % 3
            curr_pos = (dict_3[n]+1) % 3 
        counter += (2 **(n-1))
        
        if starting_peg == 0:
            starting_peg = "A"
        elif starting_peg == 1:
            starting_peg = "B"
        elif starting_peg == 2:
            starting_peg = "C"

        return compare(curr_pos,n-1)
        
    def compare(curr_pos, n):
        global starting_peg
        global counter
        if n == 1:
            if ((dict_3[n]) == (curr_pos + 1) % 3):
                counter += 1
                return starting_peg + " " + str(counter)
            if (dict_3[n]) == (curr_pos) % 3:
                return starting_peg + " " + str(counter)
            else:
                return "impossible"
        elif n % 2 == 0:
            if (dict_3[n]) == (curr_pos - 1) % 3: # if this runs, it moved
                counter += 2 ** (n-1)
                curr_pos = (dict_3[n]-1)%3
                return compare(curr_pos, n-1)           
            
            elif (dict_3[n]) == (curr_pos) % 3:
                return compare(curr_pos, n-1)
                
            else:
                return "impossible"
        else:
            if (dict_3[n]) == (curr_pos + 1) % 3: # if this runs, it moved
                counter += 2 ** (n-1)
                curr_pos = dict_3[n]+1
                return compare(curr_pos, n-1)

            elif (dict_3[n]) == (curr_pos) % 3:
                return compare(curr_pos, n-1)

            else:
                return "impossible"
                    
    y = not_moved(n)
    x = moved(n)

    if y == "impossible" and x == "impossible":
        return "impossible"
    
    elif y == "impossible":
        return x
                     
    elif x == "impossible":
        return y
