from tkinter import * 
  
 root = Tk() 
 root.title("Calculator") 
 label = Label(root, text = "Calculator", font = ("Arial", 20)) 
  
 e = Entry(root, width=30, borderwidth=4) 
 e.grid(row=0, column=0, columnspan=3, padx=10, pady=30) 
  
  
  
 def btt_onclick(number): 
     now = e.get() 
     e.delete(0, END) 
     e.insert(0, str(now) + str(number)) 
  
  
 def btt_clearing(): 
     e.delete(0, END) 
  
  
 def btt_equal(): 
     sec_num = e.get() 
     e.delete(0, END) 
     if math == "addition": 
         e.insert(0, f_num + str(sec_num)) 
     if math == "subtraction": 
         e.insert(0, f_num - str(sec_num)) 
     if math == "multiplication": 
         e.insert(0, f_num * str(sec_num)) 
     if math == "division": 
         e.insert(0, f_num / str(sec_num)) 
  
  
 def btt_add(): 
     first_num = e.get() 
     global f_num 
     global math 
     math = "addition" 
     f_num = int(first_num) 
     e.delete(0, END) 
  
  
 def btt_subtract(): 
     first_num = e.get() 
     global f_num 
     global math 
     math = "subtraction" 
     f_num = int(first_num) 
     e.delete(0, END) 
  
  
 def btt_multiplying(): 
     first_num = e.get() 
     global f_num 
     global math 
     math = "multiplication" 
     f_num = int(first_num) 
     e.delete(0, END) 
  
  
 def btt_divding(): 
     first_num = e.get() 
     global f_num 
     global math 
     math = "division" 
     f_num = int(first_num) 
     e.delete(0, END) 
  
  
  
 btt_1 = Button(root, text="1", command=lambda: btt_onclick(1), fg="#000000", bg="#dddd99", padx=30, pady=30, borderwidth=2) 
 btt_2 = Button(root, text="2", command=lambda: btt_onclick(2), fg="#000000", bg="#dddd99", padx=30, pady=30, borderwidth=2) 
 btt_3 = Button(root, text="3", command=lambda: btt_onclick(3), fg="#000000", bg="#dddd99", padx=30, pady=30, borderwidth=2) 
 btt_4 = Button(root, text="4", command=lambda: btt_onclick(4), fg="#000000", bg="#dddd99", padx=30, pady=30, borderwidth=2) 
 btt_5 = Button(root, text="5", command=lambda: btt_onclick(5), fg="#000000", bg="#dddd99", padx=30, pady=30, borderwidth=2) 
 btt_6 = Button(root, text="6", command=lambda: btt_onclick(6), fg="#000000", bg="#dddd99", padx=30, pady=30, borderwidth=2) 
 btt_7 = Button(root, text="7", command=lambda: btt_onclick(7), fg="#000000", bg="#dddd99", padx=30, pady=30, borderwidth=2) 
 btt_8 = Button(root, text="8", command=lambda: btt_onclick(8), fg="#000000", bg="#dddd99", padx=30, pady=30, borderwidth=2) 
 btt_9 = Button(root, text="9", command=lambda: btt_onclick(9), fg="#000000", bg="#dddd99", padx=30, pady=30, borderwidth=2) 
 btt_0 = Button(root, text="0", command=lambda: btt_onclick(0), fg="#000000", bg="#dddd99", padx=30, pady=30, borderwidth=2) 
  
 #btt_dot = Button(root, text=".", command=lambda: btt_onclick("."), fg="#000000", bg="#dddd99", padx=31, pady=30, borderwidth=2) 
 btt_clear = Button(root, text="Clear", command=btt_clearing, fg="#000000", bg="#dddd99", padx=20, pady=10, borderwidth=2) 
  
 btt_plus = Button(root, text="+", command=btt_add, fg="#000000", bg="#dddd99", padx=29, pady=30, borderwidth=2) 
 btt_minus = Button(root, text="-", command=btt_subtract, fg="#000000", bg="#dddd99", padx=30, pady=30, borderwidth=2) 
 btt_multiply = Button(root, text="*", command=btt_multiplying, fg="#000000", bg="#dddd99", padx=30, pady=30, borderwidth=2) 
 btt_divide = Button(root, text="/", command=btt_divding, fg="#000000", bg="#dddd99", padx=30, pady=30, borderwidth=2) 
 btt_equall = Button(root, text="=", command=btt_equal, fg="#000000", bg="#dddd99", padx=29, pady=30, borderwidth=2) 
  
 btt_9.grid(row=1, column=2, columnspan=1) 
 btt_8.grid(row=1, column=1, columnspan=1) 
 btt_7.grid(row=1, column=0, columnspan=1) 
  
 btt_6.grid(row=2, column=2, columnspan=1) 
 btt_5.grid(row=2, column=1, columnspan=1) 
 btt_4.grid(row=2, column=0, columnspan=1) 
  
 btt_3.grid(row=3, column=2, columnspan=1) 
 btt_2.grid(row=3, column=1, columnspan=1) 
 btt_1.grid(row=3, column=0, columnspan=1) 
 btt_0.grid(row=4, column=0, columnspan=1) 
  
 #btt_dot.grid(row=4, column=1, columnspan=1) 
 btt_clear.grid(row=0, column=3, columnspan=1) 
 btt_equall.grid(row=4, column=2, columnspan=1) 
  
 btt_plus.grid(row=1, column=3, columnspan=1) 
 btt_minus.grid(row=2, column=3, columnspan=1) 
 btt_multiply.grid(row=3, column=3, columnspan=1) 
 btt_divide.grid(row=4, column=3, columnspan=1) 
  
  
 root.mainloop()