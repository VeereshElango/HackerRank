no_of_rocks, stren  = input().strip().split()
no_of_rocks = int(no_of_rocks)
stren = int(stren)
count = 0
break_st = 1
rocks = [ int(y) for y in input().strip().split()]
for x in rocks:
    if x <= stren :
        count+=1
    else:
        if break_st != 0:
            break_st -=1
        else:
            break
print(count)       
