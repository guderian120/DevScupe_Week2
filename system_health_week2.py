import os, psutil, subprocess, time, requests, json


def get_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

def get_memory_usage():
    mem_info = psutil.virtual_memory().percent
    return mem_info

def get_disk_usage():
    disk_usage = psutil.disk_usage("/")
    return disk_usage

def send_to_api():
    url = "http://127.0.0.1:8000/api/metrics/"
    cpu_ = get_cpu()
    memory_ = get_memory_usage()
    disk_ = get_disk_usage()
    data = {
            "CPU": cpu_,
            "MEMORY":memory_,
            "DISK": disk_,

            }
    response = requests.post(url, data=data)
    return alert(response)
def alert(data):
    response_content = data.content  # This gives the content as bytes
    response_json = json.loads(response_content.decode('utf-8'))
    # print(response_json)
    for c in response_json:
        cpu = c['cpu_usage']
        memory = c['memory_usage']
        storage = c['disk_usage']
        
        if c['cpu_usage'] > 0:
            print('alert')
send_to_api()

