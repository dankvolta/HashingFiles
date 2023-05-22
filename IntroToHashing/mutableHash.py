class Emp:
    def __init__(self, num, id):
        self.num = num
        self.id = id

# return 1 if two objects are the same, 0 otherwise
    def __eq__(self, other):
        #equality comparison between two objects
        return self.num == other.num and self.id == other.id
    
    def __hash__(self):
        return hash((self.num, self.id))
    


john = Emp('john' , 45)
print('the hash of john is: ' + str(hash(john)))

