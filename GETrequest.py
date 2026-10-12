import requests

def check_urls(filename,timeout):
    results = [] 
    with open(filename) as f:

    
        for link in f:
            link = link.strip()
            if link == "":
                continue
            
            try:   
                response = requests.get(link, timeout=timeout)
                results.append({
                    "url": link,
                    "status": response.status_code,
                    "time": round(response.elapsed.total_seconds(), 2),
                    "error": None,
                })

                
                
                        
            except requests.exceptions.Timeout:
                results.append({"url": link, "status": None, "time": None, "error": "timeout"})
                
            except requests.exceptions.ConnectionError:
                 results.append({"url": link, "status": None, "time": None, "error": "connection error"})
                
      
    return results 
print(check_urls('urls.txt', 3))


for r in check_urls("urls.txt", 3):
    if r["error"]:
        print(f"{r['url']}   ERROR  {r['error']}")
    else:
        print(f"{r['url']}   {r['status']}   {r['time']}s")     
            
   




        