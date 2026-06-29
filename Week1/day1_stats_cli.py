def day1_stats_cli():
    list_of_numbers = input("Enter a list of numbers separated by Comma: ")
    separator = list_of_numbers.split(",")
    Lists= list(map(int, separator))

    sum=0
    length=len(Lists)

    #Mean 
    for i in range(length):
        sum+=Lists[i]

    mean=sum/length

    # median
    for i in range(length):
        for j in range(1,length):
            temp=Lists[i]
            Lists[i]=Lists[j]
            Lists[j]=temp
    
    medianIndex=int(length/2)

    median=Lists[medianIndex]



    # mode
    nums = [1, 2, 2, 3, 3, 3, 4]

    max_count = 0
    mode = None

    for i in nums:
        if nums.count(i) > max_count:
            max_count = nums.count(i)
            mode = i

   
    # Min and max
    max=Lists[0]
    min=Lists[0]
    for i in range(length):
        if Lists[i]<min:
            min=Lists[i]
        
        if Lists[i]>max:
            max=Lists[i]

    

    result={"min":min,"max":max,"mean":mean,"medain":median,"mode":mode}
    return result


day1_stats_cli()