from modul_exercise12B import Queue
queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')
print(queue.queue)
queue.dequeue()
print(queue.queue)
queue.head()