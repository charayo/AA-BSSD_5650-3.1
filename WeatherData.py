from Observer import IListener


class PressureListener(IListener):
    prev_info = ""

    def __init__(self, name, subject):
        self.name = name
        subject.register(self)

    def notify(self, event):
        val = event.split(",")[0]
        if self.prev_info != val:
            self.prev_info = val
            print("Current Barometric Pressure is", val, "atms.")


# class PressureListener(IListener):


class TemperatureListener(IListener):
    prev_info = ""

    # def __init__(self, name, subject1, subject2):
    def __init__(self, name, subject1):
        self.name = name
        subject1.register(self)
        # subject2.register(self)

    def notify(self, event):
        val = event.split(",")[1]
        if self.prev_info != val:
            self.prev_info = val
            print("Current Temperature is", val, "degrees F.")


# class TemperatureListener(IListener)


class WindListener(IListener):
    prev_info = ""

    def __init__(self, name, subject):
        self.name = name
        subject.register(self)

    def notify(self, event):
        val = event.split(",")[2]
        if self.prev_info != val:
            self.prev_info = val
            print("Current Wind Direction is from the", val.capitalize())
#  class WindListener(IListener):
