import tkinter
import tkinter.messagebox

def main():
    flag = True
    #change label text
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'hello')\
            if flag else ('blue', 'goodbye')
        label.config(text=msg, fg=color)
    
    #confirm to quit
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('tips', 'cofirm to quit?'):
            top.quit()
    
    top = tkinter.Tk()
    top.geometry('240x160')
    top.title('game')
    label = tkinter.Label(top, text='hello,world', fg='red')
    label.pack(expand=1)
    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='change', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='exit', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    tkinter.mainloop()

if __name__ == '__main__':
    main()