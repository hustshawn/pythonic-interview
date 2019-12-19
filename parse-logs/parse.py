def top_x_ip(file, n):
    with open(file, 'r') as f:
        logs = f.read().strip('\n').split('\n')
    result = {}
    for r in logs:
        ip = r.split(',')[3]
        if ip not in result:
            result[ip] = 1
        else:
            result[ip] += 1
    sorted_result = sorted(result.items(), key=lambda d: d[1], reverse=True)
    if n > len(sorted_result):
        return sorted_result
    return sorted_records[:n]

top_x_ip('access.log', 10)

# cat access.log | awk -F ',' '{print $4}'| sort | uniq -c | sort -nr | head  -5