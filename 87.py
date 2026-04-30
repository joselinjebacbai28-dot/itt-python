
import operator

def person_lister(f):
    def inner(people):
     
        people.sort(key=lambda x: int(x[2]))
        
        return [f(person) for person in people]
    return inner



