#Chapter 6  - Breadth First Search



from collections import deque


def search(name):
    queue = deque()
    queue += graph[name]
    searched = set()
    while queue:
        person= queue.popleft()
        if person not in searched:
            if is_mango_seller(person):
                print(f'{person} is the mango seller!')
                return True
            else:
                queue += graph[person]
                searched.add(person)
    
    return False

def is_mango_seller(name):
    return name[-1] == 'm'


graph = {}
graph["you"]= ["alice", "bob", "claire"]
graph["bob"]= ["anuj", "peggy"]
graph["claire"]= ["jonny", "thom"]
graph["alice"]= ["peggy"]
graph["anuj"] = []
graph["peggy"] = []
graph["jonny"] = []
graph["thom"] = []

search("you")