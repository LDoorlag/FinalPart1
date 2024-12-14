from tkinter import *
from logic import Logic
def main():
    '''
    Main function to run the application. initializes the window and the logic class
    param: None
    return: None
    '''
    window: Tk = Tk()
    window.title("Voting Application")
    Logic(window)
    window.geometry("400x600")
    window.resizable(False, False)
    window.mainloop()
if __name__ == '__main__':
    main()
