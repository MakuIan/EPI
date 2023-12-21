author = "8168265, Karabacak, 8175858, Braun"

Analysis:
=========
The program is developed according to the EVA design pattern.
Input and output are done in the console.

Output: Output is done in the console.

Description of the program:
===========================
The program does not require any further libraries other than timeit and copy, it needs the ue_07.py.
The program is written and tested in Python 3.9.6. A Python interpreter must be installed.
The program can be started with the command "python3 ue07.py" in the terminal.

The program uses timeit to measure the time it takes to run the functions. We measure by exectuting the function 100000 times, so that the result is more readable.

Testing the program:
====================
| matrix | greedy_traversal | find_best_way |
| ----- | ----- | ----- |
| [[2 , 9, -4], [-7 , 6, 8], [-3 , 1, 5]] | 0.18738345799647504 | 4.07500720799726|
| [[5 , 6, 3], [9 , 8, 3], [4 , 4, 2]] | 0.18008870800258592 | 4.102660749998904|
| [[5 , 3], [-6 , 7]] | 0.115518874998088 | 0.31541554200157407|