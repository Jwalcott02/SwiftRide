from abc import ABC, abstractmethod

class RideType(ABC):
    @abstractmethod
    def Fare_Calculation(self,distance:float) -> float:
        pass


#Different Ride Types
class EconomyRide(RideType):
    def Fare_Calculation(self,distance: float) -> float:
        return distance * 5



class LuxuryRide(RideType):
    def Fare_Calculation(self,distance: float) -> float:
        return distance * 10

class PoolRide(RideType):
     def Fare_Calculation(self,distance: float) -> float:
         return distance * 3


#Driver Class
class Driver:
    def __init__(self,name):
        self.name = name
        self.available = True

    def assign_driver(self):
        self.available = False

    def completed_ride(self):
        self.available = True

#Customer Class
class Customer:
    def __init__(self,name):
        self.name = name

    def Ride_Request(self,booking_system,ride_type: RideType, distance: float):
        driver = booking_system.find_available_driver()
        if driver:
            fare = ride_type.Fare_Calculation(distance)
            driver.assign_driver()
            print(f"Ride Fare: ${fare}, Driver: {driver.name}")
        else:
            print("No drivers available.")



#Ride Share Booking System
class RideShareBookingSystem:
    def __init__(self):
        self.drivers = []

    def add_driver(self,driver: Driver):
        self.drivers.append(driver)

    def find_available_driver(self):
        for driver in self.drivers:
            if driver.available:
                return driver
        return None


if __name__ == "__main__":
    booking_system = RideShareBookingSystem()
    Driver1 = Driver("Alice")
    Driver2 = Driver("Bob")
    booking_system.add_driver(Driver1)
    booking_system.add_driver(Driver2)

    Customer1 = Customer("John")
    Customer2 = Customer("Rebecca")
    Customer3 = Customer("Mike")

    Economy_Ride = EconomyRide()
    Luxury_Ride = LuxuryRide()
    Ride_Pool = PoolRide()
    Customer1.Ride_Request(booking_system, Economy_Ride, 15)
    Customer2.Ride_Request(booking_system, Luxury_Ride,10)
    Customer3.Ride_Request(booking_system, Ride_Pool,5)
