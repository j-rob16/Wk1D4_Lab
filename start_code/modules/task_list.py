# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    incomplete_tasks = False
    return get_tasks_by_status(list, incomplete_tasks)


## Get a list of completed tasks
def get_completed_tasks(list):
    complete_tasks = True
    return get_tasks_by_status(list, complete_tasks)


## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    long_task = []
    for task in list:
        if task["time_taken"] >= time:
            long_task.append(task)

    return long_task
    # pass


## Find a task with a given description
def get_task_with_description(list, description):
    described_task = []
    for task in list:
        if task["description"] == description:
            described_task.append(task)

    return described_task


# Extention (Function):

## Get a list of tasks by status
def get_tasks_by_status(list, status):
    tasks = []
    for task in list:
        if task["completed"] == status:
            tasks.append(task)
    return tasks


def mark_task_complete(task):
    task[0]["completed"] = True


def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task


def add_to_list(list, task):
    list.append(task)
