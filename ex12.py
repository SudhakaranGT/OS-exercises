import threading
import time

class DiningP:
    def __init__(self):
        self.chopsticks = [threading.Semaphore(1) for _ in range(5)]
        self.states = ['thinking' for _ in range(5)]
        self.lock = threading.Lock()
    
    def eat(self, i):
        left = self.chopsticks[i]
        right = self.chopsticks[(i + 1) % 5]
        
        left.acquire()
        right.acquire()
        
        with self.lock:
            print('p', i, 'is eating', self.states)
            self.states[i] = 'eating'
        
        time.sleep(3)
        
        left.release()
        right.release()
        
    
    def think(self, i):
        print('p', i, 'is thinking',self.states)
        self.states[i] = 'thinking'

def phil(p, i):
    while True:
        p.think(i)
        p.eat(i)

p = DiningP()
threads = []

for i in range(5):
    threads.append(threading.Thread(target=phil, args=(p, i)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
