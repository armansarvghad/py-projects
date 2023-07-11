class Device:
    def __init__(self, name):
        self.name = name
        self.is_turned_on = False
    
    def turn_on(self):
        self.is_turned_on = True
        print(f"{self.name} is turned on.")
    
    def turn_off(self):
        self.is_turned_on = False
        print(f"{self.name} is turned off.")

class Light(Device):
    def __init__(self, name):
        super().__init__(name)
        self.brightness = 0
    
    def set_brightness(self, brightness):
        self.brightness = brightness
        print(f"{self.name} brightness is set to {brightness}.")

class Thermostat(Device):
    def __init__(self, name):
        super().__init__(name)
        self.temperature = 72
    
    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"{self.name} temperature is set to {temperature}.")

class HomeAutomationSystem:
    def __init__(self):
        self.devices = []
    
    def add_device(self, device):
        self.devices.append(device)
        print(f"{device.name} is added to the system.")
    
    def turn_off_all_devices(self):
        for device in self.devices:
            device.turn_off()

home_automation_system = HomeAutomationSystem()

light = Light("Living Room Light")
home_automation_system.add_device(light)

thermostat = Thermostat("Living Room Thermostat")
home_automation_system.add_device(thermostat)

light.turn_on()
light.set_brightness(50)

thermostat.turn_on()
thermostat.set_temperature(75)

home_automation_system.turn_off_all
