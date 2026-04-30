
cube = lambda x: x**3

def fibonacci(n):
    storage = [0, 1]
    if n == 0:
        return []
    if n == 1:
        return [0]
    
   
    for i in range(2, n):
        storage.append(storage[-1] + storage[-2])
        
    return storage



