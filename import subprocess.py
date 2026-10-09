import subprocess
import json


def pod_status_summary():
    num_of_pods = {}

    result = subprocess.run(['kubectl' , 'get', 'pods', '-o', 'json'], capture_output=True, text=True)

    if result.returncode != 0:
        print("kubectl failed:", result.stderr)
        return {}

    output =  json.loads(result.stdout)

    pods = output['items']

    for pod in pods:
        phase = pod["status"]["phase"]
        if phase in num_of_pods:
            num_of_pods[phase] +=1

        else:
            num_of_pods[phase]=1


    return num_of_pods

print(pod_status_summary())

        



            



  

pod_status_summary()
