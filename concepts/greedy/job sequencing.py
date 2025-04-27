def print_job_schedule(jobs, t):
    # Sort jobs based on profit in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)


    result = ['-1'] * t
    slot = [False] * t

    total_profit = 0

    # Iterate through each job
    for job in jobs:
        # Find a suitable slot for this job
        for j in range(min(t - 1, job[1] - 1), -1, -1):
            if slot[j] is False:
                slot[j] = True
                result[j] = job[0]
                total_profit += job[2]
                break

    # Print the sequence and total profit
    print("Maximum profit sequence of jobs is:", result)
    print("Total profit:", total_profit)
    return total_profit  # Return total profit if needed

# Example usage
if __name__ == "__main__":
    # List of jobs with format (job_id, deadline, profit)
    jobs = [
        ['a', 7, 202],
        ['b', 5, 29],
        ['c', 6, 84],
        ['d', 1, 75],
        ['e', 2, 43]
    ]

    # Number of slots (t)
    t = 3

    # Print maximum profit sequence of jobs
    max_profit = print_job_schedule(jobs, t)
