import requests
import argparse
import sys

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

def is_down(result):
    return result["error"] is not None or result["status"] >= 500


            
if __name__ == "__main__":
  
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--timeout",type=int, default=5)

    args = parser.parse_args()

    results = check_urls(args.file, args.timeout)


    up = 0
    down = 0

    for r in results:
        if r["error"]:
            print(f"{r['url']}   ERROR  {r['error']}")
        else:
            print(f"{r['url']}   {r['status']}   {r['time']}s")   


        if is_down(r):
            down+=1

        else: 
            up +=1

    print(f"\n{up} up, {down} down")


    if down > 0:
        sys.exit(1)
    sys.exit(0)







        