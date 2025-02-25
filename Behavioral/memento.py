'''
Definition:-The Memento Pattern is a behavioral design pattern that allows an object to save and 
restore its state without violating encapsulation.
It is useful when implementing undo/redo functionality in applications.
'''


# Memento: Stores the state
class Memento:
    def __init__(self, state):
        self.state = state

# Originator: The object whose state needs to be saved
class Editor:
    def __init__(self):
        self.text = ""

    def write(self, text):
        self.text = text

    def save(self):
        return Memento(self.text)  # Save current state

    def restore(self, memento):
        self.text = memento.state  # Restore saved state

# Caretaker: Manages saved states
history = []

# Example Usage
editor = Editor()
editor.write("Hello")
history.append(editor.save())  # Save state

editor.write("Hello, World!")
history.append(editor.save())  # Save state

editor.write("Hello, Design Patterns!")  # Modify again

print("Current:", editor.text)  # Output: Hello, Design Patterns!

# Undo once
editor.restore(history[-1])
print("After Undo:", editor.text)  # Output: Hello, World!

# Undo again
editor.restore(history[-2])
print("After Second Undo:", editor.text)  # Output: Hello
