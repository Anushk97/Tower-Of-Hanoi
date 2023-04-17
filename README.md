# Tower-Of-Hanoi

The Tower of Hanoi is a mathematical puzzle invented by the French mathematician Édouard Lucas in 1883. 
There is a story about an Indian temple in Kashi Vishwanath which contains a large room with three time-worn posts in it, 
surrounded by 64 golden disks. Brahmin priests, acting out the command of an ancient prophecy, have been moving 
these disks in accordance with the immutable rules of Brahma since that time. 

The puzzle configuration and rules are as follows:
• There are n disks and three pegs: A, B, C. The n disks are different in size, and all disks are initially placed on peg A that their sizes increase from top to bottom.
• Only one disk can be moved at a time,from the top of a peg to an empty peg or to a peg with larger disk than itself on top.
• The goal is to move all n disks from pegA to either pegB or pegC– this is the goal of the original tower of Hanoi puzzle, but our goal in this question is slightly different.

It is easy to prove that the minimum number of moves needed to complete the puzzle with n disks 
is 2n-1 using recursion. Given a state with all disks on peg A, A simple algorithm to move
all disks to another peg with the minimum number of moves is to move the smallest disk (disk 1: D1) on odd moves (the 1st, 3rd, 5th... moves) 
in a circular manner ABCABC... (clockwise, as shown left); and make the only possible move which does not involve 
disk 1 on even moves (the 2nd, 4th, 6th... moves). For example, with 3 disks initially placed on peg A, 5 moves 
will lead to a state of having D1 on A, D2 on C and D3 on B. According to the simple algorithm above, the 5 moves are: (D1:A→B), (D2:A→C),
(D1:B→C), (D3:A→B) and (D1:C→A) where D1 is the smallest disk, D3 is the largest disk and (D2:A→C) means disk 2 (the middle disk) is moved from peg A to peg C.
Given a state of n disks placed on pegs A, B and C with their sizes increasing from top to bottom, 
we need to determine which peg the disks were initially placed, and how many moves there were to reach this state.
