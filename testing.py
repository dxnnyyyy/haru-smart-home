import roslibpy as ros
import tkinter as tk

window = tk.Tk()
window.title('Haru Smart Home Manager')
window.geometry('500x200')

frame = tk.Frame(master=window)
frame.pack()

entry = tk.Entry(master=window, textvariable=tk.IntVar())
entry.pack()

haru = ros.Ros(host='harumanager.local', port=9090)
haru.run()

def execute_routine():
    serivce = ros.Service(ros=haru, name='/idmind_tabletop/execute_routine', service_type='idmind_tabletop_msgs/RoutineRequest')
    request = ros.ServiceRequest({'routine': int(entry.get())})
    result = serivce.call(request=request)

button = tk.Button(master=frame, text='Execute Haru Routine', command=execute_routine)
button.pack()

window.mainloop()