class ListKeeper:
 
    
    def show():
        #return all list names
        return(listdict.keys())

    def add(name, list):
        #adds a new list in the new dict
        listdict[name] = list

    def delete(name):
        # deletes list
        listdict.pop(name)

    def sort(name):
        #returns the sorted list name
        listdict[name].sort()
        return(listdict[name])

    def append(name,list):
        #appends new items to name
        listdict[name].extend(list)


listdict = {}
listdict["example"] = [1,2,3,4,5]