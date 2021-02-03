import random
from CPU.CPUCore import CPUCore
from DataStructures.TaskState import Priority, State
from Resourses.Resource import Resource
from Schedulers.HRRN import HRRN
from Schedulers.RR import RR
from Schedulers.SJF import SJF
from Task import Task
from Schedulers.FCFS import FCFS

resourse_A = Resource("A", 0)
resourse_B = Resource("B", 0)
resourse_C = Resource("C", 0)

core1 = CPUCore('core 1')
core2 = CPUCore('core 2')
core3 = CPUCore('core 3')
core4 = CPUCore('core 4')


def get_prio(strr):
    if strr == 'X':
        return Priority.low, [resourse_A, resourse_B]
    elif strr == 'Y':
        return Priority.med, [resourse_B, resourse_C]
    elif strr == 'Z':
        return Priority.high, [resourse_A, resourse_C]


def get_resourses():
    a, b, c = input('enter a, b, c count: ').split()
    resourse_A.set_count(int(a))
    resourse_B.set_count(int(b))
    resourse_C.set_count(int(c))


def get_tasks():
    print('SJF : 1')
    print('FCFS : 2')
    print('RR : 3')
    print('HRRN: 4')
    algorithm_type = input('input algorithm type number: ')
    count = input('enter number of task: ')

    algorithm = None

    while algorithm is None:
        if algorithm_type == '1':
            algorithm = SJF(core1, core2, core3, core4)
            for i in range(int(count)):
                type, time = input('enter type, time: ').split()
                priority, resourses = get_prio(type)
                task = Task(i, 'task_' + str(i), priority, State.waiting, float(time), resourses, 0)
                algorithm.waiting_queue.append(task)

        elif algorithm_type == '2':
            algorithm = FCFS(core1, core2, core3, core4)
            for i in range(int(count)):
                type, time = input('enter type, time: ').split()
                priority, resourses = get_prio(type)
                task = Task(i, 'task_' + str(i), priority, State.waiting, float(time), resourses, 0)
                algorithm.waiting_queue.append(task)

        elif algorithm_type == '3':
            algorithm = RR(core1, core2, core3, core4)
            for i in range(int(count)):
                type, time = input('enter type, time: ').split()
                priority, resourses = get_prio(type)
                task = Task(i, 'task_' + str(i), priority, State.waiting, float(time), resourses, 0)
                algorithm.waiting_queue.append(task)

        elif algorithm_type == '4':
            algorithm = HRRN(core1, core2, core3, core4)
            for i in range(int(count)):
                type, time, arrival = input('enter  type, time, arrival time : ').split()
                priority, resourses = get_prio(type)
                task = Task(i, 'task_' + str(i), priority, State.waiting, float(time), resourses, arrival)
                algorithm.waiting_queue.append(task)
        else:
            print('choose valid type')

    print('\n'.join([task.__str__() for task in algorithm.waiting_queue]))
    algorithm.start()

    # sjf = RR(core1, core2, core3, core4)
    # # count = input('enter number of task: ')
    # l = list(range(2, 10))
    # random.shuffle(l)
    #
    # ar = [0, 1, 3, 4, 6]
    # for i in range(5):
    #     name, type, time = input('enter name, type, time: ').split()
    #     prio, res = get_prio('X')
    #     num = l.pop()
    #     task = Task(i, 'task_' + str(i), prio, State.ready, float(num), res, ar[i])
    #     print('task_' + str(i), ' ', 'X', ' ', num , ' arrival time:  ' + str(ar[i]))
    #     sjf.waiting_queue.append(task)
    # sjf.start()


if __name__ == '__main__':
    get_resourses()
    get_tasks()
