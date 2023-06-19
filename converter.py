import tkinter as tk

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None

arr = ["._", "_...", "_._.", "_..", ".", ".._.", "__.", "....", "..", ".___", "_._", "._..",
                    "__", "_.", "___", ".__.", "__._", "._.", "...", "_", ".._", "..._", ".__", 
                    "_.._", "_.__", "__..", "_____", ".____", "..___", "...__", "...._", ".....", "_....", "__...", "___..", "____.", ""]

class abctomorse:
    def __init__(self):
        self.root = Node("A")
        self.arr = arr

    def create(self):
        node = self.root
        for i in range(66, 91):
            x = chr(i)
            node.next = Node(x)
            node.down = Node(self.arr[i - 66])
            node = node.next
        for i in range(48,59):
            x = chr(i)
            node.next = Node(x)
            node.down = Node(self.arr[i - 23])
            node = node.next

    def convert(self, text):
        node = self.root
        converted = ""
        for i in text:
            node = self.root
            while node is not None:
                if node.val == i.upper():
                    converted += node.down.val + "  "
                node = node.next
        return converted

class morsetoabc:
    def __init__(self):
        self.root = Node("._")
        self.arr = arr

    def create(self):
        node = self.root
        for i in range(66, 92):
            x = chr(i - 1)
            node.next = Node(self.arr[i - 65])
            node.down = Node(x)
            node = node.next
            
        for i in range(49,59):
            x = chr(i-1)
            node.next = Node(self.arr[i - 22])
            node.down = Node(x)
            node = node.next

    def convert(self, morse):
        node = self.root
        converted = ""
        for i in morse:
            node = self.root
            while node is not None:
                if node.val == i:
                    converted += node.down.val
                node = node.next
        return converted


class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Morse Code Converter")

        self.input_label = tk.Label(self.window, text="Input:")
        self.input_label.pack()

        self.input_text = tk.Text(self.window, height=4, width=50)
        self.input_text.pack()

        self.output_label = tk.Label(self.window, text="Output:")
        self.output_label.pack()

        self.output_text = tk.Text(self.window, height=4, width=50)
        self.output_text.pack()

        self.option_var = tk.IntVar()

        self.morse_to_abc = tk.Radiobutton(self.window, text="Morse to English", value=1, variable=self.option_var)
        self.morse_to_abc.pack()

        self.abc_to_morse = tk.Radiobutton(self.window, text="English to Morse", value=2, variable=self.option_var)
        self.abc_to_morse.pack()

        self.convert_button = tk.Button(self.window, text="Convert", command=self.convert)
        self.convert_button.pack()

    def convert(self):
        option = self.option_var.get()
        
        if option == 1:
            morse_converter = morsetoabc()
            morse_converter.create()
            morse_text = self.input_text.get("1.0", tk.END).strip().split()
            converted_text = morse_converter.convert(morse_text)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, converted_text)
        elif option == 2:
            abc_converter = abctomorse()
            abc_converter.create()
            abc_text = self.input_text.get("1.0", tk.END).strip()
            converted_text = abc_converter.convert(abc_text)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, converted_text)

    def run(self):
        self.window.mainloop()

gui = GUI()
gui.run()
