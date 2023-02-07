from Observer import Subject, IListener
from WeatherData import *

# class CapsListener(IListener):
#     def __init__(self, name, subject):
#         self.name = name
#         subject.register(self)
#
#     def notify(self, event):
#         print(self.name, "You typed: ", event.capitalize())


# class LowerListener(IListener):
#     def __init__(self, name, subject):
#         self.name = name
#         subject.register(self)
#
#     def notify(self, event):
#         print(self.name, "You typed: ", event.lower())
class WeatherTower(Subject):
    def getUserAction(self):
        prompt = "Enter Pressure, temperature, and Wind Direction separated by a comma."
        self.data = input(prompt)
        return self.data
# class WeatherTower(Subject):


class WeatherMan(Subject):
    def getUserAction(self):
        prompt = "Enter Weather man's name"
        self.data = input(prompt)
        return self.data
# class WeatherTower(Subject):


if __name__ == "__main__":
    # make a subject object to spy on
    subject = WeatherTower()
    # subject2 = WeatherMan()

    listenerT = TemperatureListener("T", subject)
    # listenerT = TemperatureListener("T", subject, subject2)
    # subject.register(listenerT)

    listenerP = PressureListener("P", subject)
    # subject.register(listenerP)

    listenerW = WindListener("W", subject)
    # subject.register(listenerW)

    action = subject.getUserAction()
    subject.notify_listeners(action)
    # To test the prev_info memory algorithm
    action = subject.getUserAction()
    subject.notify_listeners(action)

    # making Temperature observe WeatherMan
    # action = subject2.getUserAction()
    # subject2.notify_listeners(action)
