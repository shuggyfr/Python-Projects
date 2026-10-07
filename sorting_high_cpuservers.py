def high_cpu_servers(servers):
    high_cpu = {}
    
    for server in servers:
        
        if servers[server] > 80:
            high_cpu[server] = servers[server]
    

    ranked = sorted(high_cpu, key=high_cpu.get, reverse=True) # sorted(high_cpu sorts the names of the servers in ascending order, key=high_cpu.get looks up each CPU Value % , reverse=True (biggest number first)

    for name in ranked:
        print(f"{name}:{high_cpu[name]}%")

high_cpu_servers({
    "web-01": 45,
    "web-02": 92,
    "db-01": 81,
    "cache-01": 99,
    "api-01": 67,
})
