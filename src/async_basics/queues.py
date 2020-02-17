import multiprocessing as mp

def washer(dishes, out):
    for dish in dishes:
        print('Washing ', dish, ' dish')
        out.put(dish)
def dryer(input):
    while True:
        dish = input.get()
        print('Drying ', dish, ' dish')
        input.task_done()
dish_queue = mp.JoinableQueue()
dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
dryer_proc.daemon = True
dryer_proc.start()
dishes = ['salad', 'bread', 'entree', 'dessert']
washer(dishes, dish_queue)
dish_queue.join()