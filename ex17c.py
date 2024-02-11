def exists_in_frame(key, frame):
    for i in range(len(frame)):
        if frame[i] == key:
            return True
    return False

def find_least_recently_used(pg, frame, pn, index):
    result = -1
    farthest = index
    for i in range(len(frame)):
        j = 0
        for j in range(index, pn):
            if frame[i] == pg[j]:
                if j > farthest:
                    farthest = j
                    result = i
                break
        if j == pn - 1:
            return i
    return 0 if result == -1 else result

def optimal_page(pg, pn, frame_count):
    frames = []
    hits = 0
    for i in range(pn):
        if exists_in_frame(pg[i], frames):
            hits += 1
            continue
        if len(frames) < frame_count:
            frames.append(pg[i])
        else:
            j = find_least_recently_used(pg, frames, pn, i + 1)
            frames[j] = pg[i]
    misses = pn - hits
    hit_ratio = (hits / pn) * 100
    miss_ratio = (misses / pn) * 100
    print("No. of hits =", hits)
    print("No. of misses =", misses)
    print("Hit Ratio =", "{:.2f}%".format(hit_ratio))
    print("Miss Ratio =", "{:.2f}%".format(miss_ratio))

# Driver Code
page_references = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3]
page_count = len(page_references)
frame_number = 4
optimal_page(page_references, page_count, frame_number)
