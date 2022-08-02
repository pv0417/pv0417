Can you see how the above example works? As an exercise, try printing the following pattern using a while loop (Hint: use string concatenation):

```
          *
         **
        ***
       ****
      *****
     ******
      *****
       ****
        ***
         **
          *
```
```
       *
       **
       ***
       ****
       *****
       ******
       *******
       ******
       *****
       ****
       ***
       **
       *
```
Here's another one, putting the two together:


```
          *
         ***
        *****
       *******
      *********
     ***********
      *********
       *******
        *****
         ***
          *
```

max_length  = k = 7
j = 1
i = max_length -1
space = " " 
while i >0:
    while j <= max_length:
        print(" "*(len(space)*k)+"*"*j)
        j = j+1
        k = k-1
    k = k+1
    print(" "*(len(space)*k+1)+"*"*i)
    i = i-1

max_length  = 7
i = max_length -1
j = 1
space = " " 
while i >0:
    while j <= max_length:
        print(" "*(len(space)*max_length)+"*"*j)
        j = j+1
    print(" "*(len(space)*max_length)+"*"*i)
    i = i-1
        
max_length = 11
i = 0
j = max_length
space = " "
k = max_length
while i < max_length:
    if i % 2 != 0:
        print(" "*(len(space)*k//2)+"*"*i)
    i = i+1
    k = k-1
while j >= 0:
    if j % 2 != 0:
        print(" "*(len(space)*k//2)+"*"*j)
    j = j-1
    k = k+1
