from tkinter import*
window=Tk()
window.title("Event Handeler")
window.geometry("100x100")
def handle_keypress(event):
    print(event.char)
window.bind("<Key>",handle_keypress)
def handle_click(event):
    print("\nThe button was clcked!")
button=Button(text="Click me!")
button.pack()
button.bind("<Button-1>",handle_click)
window.mainloop()