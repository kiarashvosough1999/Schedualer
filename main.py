import random

from CPU.CPUCore import CPUCore
from DataStructures.TaskState import Priority, State
from Resourses.Resource import Resource
from Schedulers.SJF import SJF
from Task import Task
from Schedulers.FCFS import FCFS

# ready = []
#
# waiting = []


resourse_A = Resource("A", 0)
resourse_B = Resource("B", 0)
resourse_C = Resource("C", 0)


def get_prio(str):
    if str == 'X':
        return Priority.low, [resourse_A, resourse_B]
    elif str == 'Y':
        return Priority.med, [resourse_B, resourse_C]
    elif str == 'Z':
        return Priority.high, [resourse_A, resourse_C]


def get_resourses():
    a, b, c = input('enter a, b, c count: ').split()
    resourse_A.set_count(int(a))
    resourse_B.set_count(int(b))
    resourse_C.set_count(int(c))

def get_tasks():
    sjf = SJF()
    # count = input('enter number of task: ')
    l = list(range(2, 8))
    random.shuffle(l)

    for i in range(5):
        # name, type, time = input('enter name, type, time: ').split()
        prio, res = get_prio('X')
        num = l.pop()
        task = Task(i, 'task_' + str(i), prio, State.ready, float(num), res)
        print('task_' + str(i), ' ', 'X', ' ', num)
        sjf.ready_queue.append(task)
    sjf.start()


if __name__ == '__main__':
    get_resourses()
    get_tasks()
