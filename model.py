class ButtonModel:
    def __init__(self):
        self.colors = ['red', 'blue']
        self.value = 'click'
        self.current_index = 0

    def chang_color(self):
        self.current_index = (self.current_index + 1)% len(self.colors)
        return self.colors[self.current_index]
    
        
