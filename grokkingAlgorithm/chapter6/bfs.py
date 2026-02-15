# breadth first search
# just an example // means: it does not run, but the idea is there

def search(name):
    search_queue = deque()
    search_queue += graph[name]

    searched = []

    while search_queue :
        person = search_queue.popleft();
        if not person in searched :
            if person_is_seller(person):
                print("He is a seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False



graph = {}

graph["you"] = ["Kabin", "Ghale" , "Neo"]
graph["age"] = [20,21,22]

search("you")
search("age")
