# Rihards Nolmanis 221RDB431 16.grupa
def parallel_processing(n, m, data):
    output = [] 
    to_do = [] 
    for i in range(n):
        to_do.append((0, i))
    for t_time in data:
        min_thread = to_do[0]
        for thread in to_do: 
            if thread[0] < min_thread[0]:
                min_thread = thread
        output.append((min_thread[1], min_thread[0])) 
        to_do.remove(min_thread)
        to_do.append((min_thread[0] + t_time, min_thread[1]))  
    return output

def main(): 
    first_line = input() 
    n, m = map(int, first_line.split())
    sec_line = input() 
    data = list(map(int, sec_line.split())) 
    assert len(data) == m

    result = parallel_processing(n, m, data) 

    for i, j in result:
        print(i, j)

if __name__ == "__main__":
    main()