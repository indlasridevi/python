import queue
q1 = queue.Queue()
q1.put(11)
q1.put(5)
q1.put(4)
q1.put(21)
q1.put(3)
def reverseQueue (q1scr, q2dest) :
    buffer = q1scr.get()
    if (q1scr.empty() == False):
        reverseQueue(q1scr, qdest)       #using recursion
    qdest.put(buffer)
    return q2dest
qdest = queue.Queue()
qReversed = reverseQueue(q1,qdest)
while (qReversed.empty() == False):
    print(qReversed.queue[0], end = " ")
    qReversed.get()