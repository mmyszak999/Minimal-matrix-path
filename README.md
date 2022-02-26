# What the code does?
  Code is responsible for setting the matrix path consisting of the lowest possible sum of the fields.
 ## Some explanation how the path is being set:
This is matrix of digits:  
**3** 4 1 2 8 6  
6 1 8 2 7 4  
5 9 3 9 9 5   
8 4 1 3 2 6  
3 7 2 8 6 4  

Let's say we start from the 1st row (path always start from field in the 1st column)
We can move to the next column in 3 ways:  
1. Go to an upper row  
2. Stay in the same row  
3. Go to the lower row  

In the case, when the we are in the first row, move to an upper row equals to being in the last row  
If we are in the last row, move to a lower row equals to being in the first row  

So in the first move, we can go to three fields:  
**7** (treated as an upper row move)  
**4** (in the same row)  
**1** (an lower row move)

That step is repeated until a path is in the last column.

A path result contain the sum of the path fields (numbers) and list of fields row indexes (index is a number decreased by 1)




# How to run the script in command line (Windows CMD)?
1. Download the .zip file with files from GitHub
2. Unzip that file  
3. Run command line (CMD)  
4. In command line, go to the directory where the code is, using commands (**cd.. and cd file_name)**
5. 


