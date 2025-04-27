def job_sequencing(jobs):
    # Sort jobs by deadline and profit in descending order
    for i in range(len(jobs)):
        for j in range(i + 1, len(jobs)):
            if jobs[i][1] < jobs[j][1] or (jobs[i][1] == jobs[j][1] and jobs[i][2] < jobs[j][2]):
                jobs[i], jobs[j] = jobs[j], jobs[i]

    # Initialize result and deadline arrays
    result = [False] * len(jobs)
    deadline = [False] * (max(job[1] for job in jobs) + 1)

    # Iterate through jobs and schedule them
    for i, job in enumerate(jobs):
        for j in range(job[1], 0, -1):
            if not deadline[j]:
                deadline[j] = True
                result[i] = True
                break

    # Print the scheduled jobs
    print("Following jobs are scheduled:")
    for i, job in enumerate(jobs):
        if result[i]:
            print(f"Job {job[0]} with profit {job[2]} and deadline {job[1]}")

# Example usage:
jobs = [
    ("A", 2, 100),
    ("B", 1, 19),
    ("C", 2, 27),
    ("D", 1, 25),
    ("E", 3, 15)
]

job_sequencing(jobs)