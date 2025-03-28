
# movie class in oop lesson on python
class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('Movie object was created!')

    def __str__(self):
        return f'{self.title} by {self.director}' 

    def __len__(self):
        return self.duration
        
m = Movie('Interstellar', 'Nolan', 192)

print(m)
print(len(m))
