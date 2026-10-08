def human_size(num_bytes):

# input is taken
# conversion is done
# output is given 

    kb = 1024
    mb = 1024 * kb
    gb = 1024 * mb

    
    if num_bytes < kb :
        return (f"{num_bytes}B")
    elif num_bytes < mb:
        return f"{num_bytes / kb:.1f}KB" 

    elif num_bytes < gb:
        return f"{num_bytes / mb:.1f}MB"     
    else:
         return f"{num_bytes  / gb:.1f}GB"
    

    

print(human_size(11))