'''
Haru Smart Home Application
'''
import tkinter as tk
import roslibpy as ros
import requests as req
from dotenv import load_dotenv
import os

class HaruSmartHome(tk.Tk):
    '''
    Haru Smart Home Application
    '''
    def __init__(self):
        super().__init__()
        
        self.dotenv = load_dotenv()

        self.title('Haru Smart Home Application')
        self.geometry('500x200')
        self.hass_url = "http://localhost:8123/api/services/scene/turn_on"
        self.hass_headers = {"Authorization": os.environ.get('hass_auth')}

        try:
            self.haru = ros.Ros(host='harumanager.local', port=9090)
            self.haru.run()
            print('Connected to haru?', self.haru.is_connected)
        except Exception:
            print('could not connect to haru')

        # Main tkinter container
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)

        # Routine number input field
        routine_number = tk.IntVar()
        routine_field = tk.Entry(container, textvariable=routine_number)
        routine_field.pack()

        # Execution button
        execute_routine_button = tk.Button(
            container,
            text='Execute Haru Routine',
            command=lambda: self.execute_routine(int(routine_number.get())))
        execute_routine_button.pack()

        # Start learning environment
        execute_scene_button = tk.Button(
            container,
            text='Start Learning',
            command=self.start_learning
        )
        execute_scene_button.pack()
        
        # Stop learning environment
        execute_scene_button = tk.Button(
            container,
            text='Stop Learning',
            command=self.stop_learning
        )
        execute_scene_button.pack()


    def execute_routine(self, number):
        '''
        Executes a routine with the given number
        '''
        execute_routine_service = ros.Service(
            ros=self.haru,
            name='/idmind_tabletop/execute_routine',
            service_type='idmind_tabletop_msg/Routine')
        execute_routine_request = ros.ServiceRequest({'routine': number})
        execute_routine_service.call(execute_routine_request)

    def start_learning(self):
        '''
        Start learning environment
        '''
        res = req.post(self.hass_url, headers=self.hass_headers, json={"entity_id": "scene.haru"} )
        if(res.status_code != 200):
            print('Error: ', res.status_code)
        else:
            print('starting learning environment')

    def stop_learning(self):
        '''
        Stop learning environment
        '''
        res = req.post(self.hass_url, headers=self.hass_headers, json={"entity_id": "scene.haru_off"} )
        if(res.status_code != 200):
            print('Error: ', res.status_code)
        else:
            print('stoping learning environment')


if __name__ == '__main__':
    haru_smart_home = HaruSmartHome()
    haru_smart_home.mainloop()
