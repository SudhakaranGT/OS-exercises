from queue import Queue 

def pageFaults(pages, n, capacity): 

    s = set() 

    indexes = Queue() 

    page_faults = 0
    page_hits = 0
    for i in range(n): 
        if (len(s) < capacity): 
            if (pages[i] not in s): 
                s.add(pages[i]) 
                page_faults += 1
                indexes.put(pages[i]) 
            else:
                page_hits += 1
        else: 
            if (pages[i] not in s): 
                val = indexes.queue[0] 
                indexes.get() 
                s.remove(val) 
                s.add(pages[i]) 
                indexes.put(pages[i]) 
                page_faults += 1
            else:
                page_hits += 1
    
    return [page_faults , page_hits]

if __name__ == '__main__': 
    pages= []
    no_of_page = int(input('ENTER THE NUMBER OF PAGES : '))
    for i in range(no_of_page):
        a = int(input('ENTRT THE REFERENCE STRING OF A PAGE : '))
        pages.append(a)
    print("REFRENCE STRING : ",pages)
    n = len(pages)
    capacity = int(input('ENTER THE NUMBER OF FRAMES : '))
    a = pageFaults(pages, n, capacity)
    print("PAGE HITS : ", a[1])
    print("PAGE FAULT : ", a[0]) 
    print(f"THE RATIO OF PAGE HIT TO THE PAGE FAULT IS {a[1]}:{a[0]} : ", a[1]/a[0])
    print("THE PAGE HIT PECENTAGE IS : ", a[0] * 100 / n)
    print("THE PAGE FAULT PERCENTAGE IS : ", a[1] * 100 / n)

