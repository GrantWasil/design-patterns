class Subject: 
    def registerObserver(self, observer):
        raise NotImplementedError

    def removeObserver(self, observer):
        raise NotImplementedError

    def notifyObservers(self):
        raise NotImplementedError

class Observer:
    def update(self, temp, humidity, pressure):
        return NotImplementedError

class DisplayElement:
    def display(self):
        return NotImplementedError

class WeatherData(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def registerObserver(self, observer):
        self.observers.append(observer)
    
    def removeObserver(self, observer):
        self.observers.remove(observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)
    
    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()

class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weatherData):
        self.temperature = 0
        self.humidity = 0
        self.weatherData = weatherData
        weatherData.registerObserver(self)
    
    def CurrentConditionsDisplay(self, weatherData):
        self.weatherData = weatherData
        weatherData.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()
    
    def display(self):
        print(f"Current conidtions: " + str(self.temperature) + "F degrees and " + str(self.humidity) + "% humidity" )


weatherData = WeatherData()

currentDisplay = CurrentConditionsDisplay(weatherData)

weatherData.setMeasurements(80, 65, 30.4)
weatherData.setMeasurements(82, 70, 29.2)
weatherData.setMeasurements(78, 90, 29.2)