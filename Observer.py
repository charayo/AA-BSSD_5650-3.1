# code taken from: https://en.wikibooks.org/wiki/Computer_Science_Design_Patterns/Observer
# Date Accessed: 02/04/2023
# License:  Open License - https://foundation.wikimedia.org/wiki/Terms_of_Use/en
# CHANGELOG:
#   -   Refactored code to Python 3
#   -   Updated AbstractSubject to Python 3 ABC
#
#
#
#


from abc import ABC, abstractmethod


class AbstractSubject(ABC):
    @abstractmethod
    def register(self, listener):
        pass

    @abstractmethod
    def unregister(self, listener):
        pass

    @abstractmethod
    def notify_listeners(self, event):
        pass


class IListener(ABC):
    @abstractmethod
    def notify(self, event):
        pass


class Listener(IListener):
    def __init__(self, name, subject):
        self.name = name
        subject.register(self)

    def notify(self, event):
        print(self.name, "received event", event)


class Subject(AbstractSubject):
    def __init__(self):
        self.listeners = []
        self.data = None

    def getUserAction(self):
        self.data = input('Enter something to do:')
        return self.data

    # Implement abstract Class AbstractSubject

    def register(self, listener):
        self.listeners.append(listener)

    def unregister(self, listener):
        self.listeners.remove(listener)

    def notify_listeners(self, event):
        for listener in self.listeners:
            listener.notify(event)


if __name__ == "__main__":
    # make a subject object to spy on
    subject = Subject()

    # register two listeners to monitor it.
    listenerA = Listener("<listener A>", subject)
    listenerB = Listener("<listener B>", subject)

    # simulated event
    subject.notify_listeners("<event 1>")
    # outputs:
    #     <listener A> received event <event 1>
    #     <listener B> received event <event 1>

    action = subject.getUserAction()
    subject.notify_listeners(action)
    # Enter something to do:hello
    # outputs:
    #     <listener A> received event hello
    #     <listener B> received event hello
