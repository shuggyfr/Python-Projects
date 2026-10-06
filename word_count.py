def word_count(sentence):
    counts = {}
    words = sentence.lower().split()
    for word in words:
        
        if word in counts:
            counts[word]+=1
        else:
            counts[word]= 1
    return counts
result = word_count("wowW woww what is is you")
print(result)