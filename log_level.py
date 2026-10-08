def count_log_levels(filename):


    counts = {}

    with open (filename) as f:
      


        for line in f:


            words = line.split()
            
            if len(words)  < 3:
                 continue
            
            level = words[2]

            if level in counts:
                counts[level] +=1
            
            else:
                counts[level] = 1

            
    return counts



print(count_log_levels("app.log"))

