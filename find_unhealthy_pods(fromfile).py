import json

def find_unhealthy_pods(filename):
    # find pods that are not running or have more than 5 restarts
    
    names = []
    with open(filename, 'r') as f:
        pods = json.load(f)
    for pod in pods:
        if pod['status'] != "Running" or pod['restarts'] > 5:
            names.append(pod['name'])

    return names
print(find_unhealthy_pods('pods.json'))


        

