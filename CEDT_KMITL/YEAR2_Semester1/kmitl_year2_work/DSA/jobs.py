class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, job):
        self.queue.append(job)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue) 

class Job:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Company:
    def __init__(self):
        self.queues = [Queue() for _ in range(10)]

    def addJob(self, id, jobName):
        job = Job(id, jobName)
        self.queues[int(id) // 100].enqueue(job)
        print("Job submitted.")

    def getNextJob(self):
        for queue in self.queues:
            if queue.size() > 0:
                job = queue.dequeue()
                print(f"ID : {job.id} Job : {job.name} starts running.")
                break

    def cancelJob(self, id, jobName):
        for job in self.queues[int(id) // 100].queue:
            if job.name == jobName:
                self.queues[int(id) // 100].queue.remove(job)
                print(f"ID : {id} Job: {jobName} has been cancelled.")
                break

    def urgentJob(self, id, jobName):
        for job in self.queues[int(id) // 100].queue:
            if job.name == jobName:
                self.queues[int(id) // 100].queue.remove(job)
                self.queues[0].enqueue(job)
                print(f"ID : {id} Job: {jobName} has first priority.")
                break
    def listJobs(self):
            for i, queue in enumerate(self.queues):
                if queue.size() > 0:
                    print(f"Jobs in queue {i}:")
                    for job in queue.queue:
                        print(f"ID: {job.id}, Job Name: {job.name}")
                        

queue = Company()
while True:
    command = input("Enter Command: ")
    if command == "A":
        ID, jobName = input("Enter ID and Job Name: ").split()
        queue.addJob(ID, jobName)
    elif command == "L":
        queue.listJobs()
    elif command == "R":
        queue.runJob()
    elif command == "C":
        ID, jobName = input("Enter ID and Job Name: ").split()
        queue.cancelJob(ID, jobName)
    elif command == "U":
        ID, jobName = input("Enter ID and Job Name: ").split()
        queue.urgentJob(ID, jobName)
