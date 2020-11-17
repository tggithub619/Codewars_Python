#https://www.codewars.com/kata/56d46b8fda159582e100001b/train/python

def travel(total_time, run_time, rest_time, speed):
    count = total_time // (run_time + rest_time)
    rest = total_time % (run_time + rest_time)
    dist = run_time * speed * count
    if rest >= run_time:
        dist += run_time * speed
    else:
        dist += rest * speed
    return dist