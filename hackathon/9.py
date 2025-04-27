def print_job_schedule(jobs, t):
    jobs.sort(key=lambda x: x[2], reverse=True)
    result = ['-1'] * t
    slot = [False] * t
    total_profit = 0
    for job in jobs:
        for j in range(min(t - 1, job[1] - 1), -1, -1):
            if slot[j] is False:
                slot[j] = True
                result[j] = job[0]
                total_profit += job[2]
                break
    print("Maximum profit sequence of jobs is:", result)
    print("Total profit:", total_profit)
    return total_profit
if __name__ == "__main__":
    jobs = [
        ['J1', 1, 50],
        ['J2', 2, 10],
        ['J3', 3, 40],
        ['J4', 3, 70],
    ]
    t = 2
    max_profit = print_job_schedule(jobs, t)
