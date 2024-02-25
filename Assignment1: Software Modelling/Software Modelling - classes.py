from enum import Enum
from datetime import date


class SeatPreference(Enum): #defines an enumeration for SeatPreference with two options
    WindowSeat = "Window Seat"
    AisleSeat = "Aisle Seat"


class AirlinePreference(Enum): #defines an enumeration for AirlinePreference with four options
    Emirates = "Emirates Airline"
    National = "National Airline"
    Turkish = "Turkish Airline"
    American = "American Airline"


class ClassPreference(Enum): #defines an enumeration for ClassPreference with three options
    Economy = "Economy"
    Business = "Business"
    FirstClass = "First Class"


class AuthenticationStatus(Enum): #defines an enumeration for AuthenticationStatus with 2 options
    AuthenticationSuccess = "Authenticated"
    AuthenticationFailed = "Not Authenticated"


class BookingStatus(Enum): #defines an enumeration for BookingStatus with two options
    Confirmed = "Confirmed"
    Cancelled = "Cancelled"


class Person:  # create a parent class that the child class (passenger) would inherit attributes and functions from.
    def __init__(self, firstName, lastName, birthDate, id, nationality, email, phoneNumber): #define a constructor method to initialize the attributes of the Person class.

        self.__firstName = firstName
        self.__lastName = lastName
        self.__birthDate = birthDate
        self.__id = id
        self.__nationality = nationality
        self.__email = email
        self.__phoneNumber = phoneNumber

    def setFirstName(self, firstName): #setter method for updating the attribute of firstName
        self.__firstName = firstName

    def setLastName(self, lastName): #setter method for updating the attribute of lastName
        self.__lastName = lastName

    def setBirthDate(self, birthDate): #setter method for updating the attribute of birthDate
        self.__birthDate = birthDate

    def setID(self, id): #setter method for updating the attribute of id
        self.__id = id

    def setNationality(self, nationality): #setter method for updating the attribute of nationality
        self.__nationality = nationality

    def setEmail(self, email): #setter method for updating the attribute of email
        self.__email = email

    def setPhoneNumber(self, phoneNumber): #setter method for updating the attribute of phoneNumber
        self.__phoneNumber = phoneNumber

    def getFirstName(self): #getter method for receiving the first name attribute.

        return self.__firstName

    def getLastName(self): #getter method for receiving the last name attribute.
        return self.__lastName

    def getBirthDate(self): #getter method for receiving the birth date attribute.
        return self.__birthDate

    def getID(self): #getter method for receiving the id attribute.
        return self.__id

    def getNationality(self): #getter method for receiving the nationality attribute.
        return self.__nationality

    def getEmail(self): #getter method for receiving the email attribute.
        return self.__email

    def getPhoneNumber(self): #getter method for receiving the phone number attribute.
        return self.__phoneNumber

    def displayPersonInfo(self): #define a function to display information about the person.
        return f"Name: {self.__firstName} {self.__lastName}, Birth Date: {self.__birthDate}, ID: {self.__id}, Nationality: {self.__nationality}, Email: {self.__email}, PhoneNumber: {self.__phoneNumber}"


class Passenger(Person):  #create a child class that inherits attributes from the parent class (person).
    def __init__(self, firstName, lastName, birthDate, id, nationality, email, phoneNumber, bookingRefNum,
                 seatPreference, airlinePreference, classPreference): #define a constructor method to initialize the attributes of the Passenger class, including the attributes of the parent class..
        Person.__init__(self, firstName, lastName, birthDate, id, nationality, email, phoneNumber) #calls the constructor of the parent class (Person) to initialize common attributes.
        self.__bookingRefNum = bookingRefNum
        self.__seatPreference = seatPreference
        self.__airlinePreference = airlinePreference
        self.__classPreference = classPreference

    def setBookingRefNum(self, bookingRefNum): #setter method for updating the attribute of bookingRefNum
        self.__bookingRefNum = bookingRefNum

    def setSeatPreference(self, seatPreference): #setter method for updating the attribute of seatPreference
        self.__seatPreference = seatPreference

    def setAirlinePreference(self, airlinePreference): #setter method for updating the attribute of airlinePreference
        self.__airlinePreference = airlinePreference

    def setClassPreference(self, classPreference): #setter method for updating the attribute of classPreference
        self.__classPreference = classPreference

    def getBookingRefNum(self): #getter method for receiving the bookingRefNum attribute.
        return self.__bookingRefNum

    def getSeatPreference(self): #getter method for receiving the seatPreference attribute.
        return self.__seatPreference

    def getAirlinePreference(self): #getter method for receiving the airlinePreference attribute.
        return self.__airlinePreference

    def getClassPreference(self): #getter method for receiving the classPreference attribute.
        return self.__classPreference

    def displayPassenger(self): #define a function to display information about the passenger.
        return super().displayPersonInfo() + f", BookingRefNum: {self.__bookingRefNum}, SeatPreference: {self.__seatPreference.value}, AirlinePreference: {self.__airlinePreference.value}, ClassPreference: {self.__classPreference.value}"

class BoardingPass: #create a class for the boarding pass.
    def __init__(self, gateNum, therminal, electronicTicketNum): #define a constructor method to initialize the attributes of the Passenger class.
        self.__gateNum = gateNum
        self.__therminal = therminal
        self.__electronicTicketNum = electronicTicketNum

    def setGateNum(self, gateNum):  #setter method for updating the attribute of gateNum
        self.__gateNum = gateNum

    def setTherminal(self, therminal):  #setter method for updating the attribute of therminal
        self.__therminal = therminal

    def setElectronicTicketNum(self, electronicTicketNum):  #setter method for updating the attribute of electronicticketNum
        self.__electronicTicketNum = electronicTicketNum

    def getGateNum(self): #getter method for receiving the gateNum attribute
        return self.__gateNum

    def getTherminal(self): #getter method for receiving the therminal attribute
        return self.__therminal

    def getElectronicTicketNum(self): #getter method for receiving the electronicticketNum attribute
        return self.__electronicTicketNum

    def displayBoardingPass(self):  #defines a function to generate or display the boarding pass info
        return f"Gate Number: {self.__gateNum}, Therminal: {self.__therminal}, Electronic Ticket Number: {self.__electronicTicketNum}"


class CheckIn: #create a class for the check in
    def __init__(self, passengerID, passengerName, baggageWeight, authenticationStatus): #define a constructor method to initialize the attributes of the CheckIn class.
        self.__passengerID = passengerID
        self.__passengerName = passengerName
        self.__baggageWeight = baggageWeight
        self.__authenticationStatus = authenticationStatus

    def setPassengerID(self, passengerID): #setter method for updating the attribute of passengerID
        self.__passengerID = passengerID

    def setPassengerName(self, passengerName): #setter method for updating the attribute of passengerName
        self.__passengerName = passengerName

    def setBaggageWeight(self, baggageWeight): #setter method for updating the attribute of baggageWeight
        self.__baggageWeight = baggageWeight

    def setAuthenticationStatus(self, authenticationStatus): #setter method for updating the attribute of authenticationStatus
        self.__authenticationStatus = authenticationStatus

    def getPassengerID(self): #getter method for receiving the passengerID attribute
        return self.__passengerID

    def getPassengerName(self): #getter method for receiving the passengerName attribute
        return self.__passengerName

    def getBaggeWeight(self): #getter method for receiving the baggageWeight attribute
        return self.baggageWeight

    def getAuthenticationStatus(self): #getter method for receiving the authenticationStatus attribute
        return self.__authenticationStatus

    def checkBaggageWeight(self, baggageWeight): #define a function to check the weight of the baggage that the passenger provides at check-in
        if baggageWeight > 35: #checks if the baggage weight is greater than 35
            print(f"Warning: Baggage weight exceeds 35 kg. Additional charges is required.") #prints a message if baggage weight is greater than 35

    def checkAuthentication(self): #define a function to check whether a passenger is authenticated
        if self.__authenticationStatus == AuthenticationStatus.AuthenticationSuccess: #checks if authentication status is success
            print(f"Passenger authenticated, therefore, boarding pass can be generated.") #prints a message that a boarding pass can be generated if authentication status is success

        else:
            print(f"Passenger not authenticated, therefore, boarding pass cannot be generated.") #prints a message that a boarding pass cannot be generated if authentication status failed

    def verifyPassport(self): #aims to define a function that checks if the passenger's passport is verified to continue with generating boarding pass process
        pass

    def displayCheckInInfo(self): #define a function to display the check in info
        print(
            f"PassengerID: {self.__passengerID}, PassengerName: {self.__passengerName}, BaggageWeight: {self.__baggageWeight}, Authentication Status: {self.__authenticationStatus.value}")


class Flight: #creates a class for the flight
    def __init__(self, passengerName, bookingStatus, boardingPass, locationTo, locationFrom, flightNum, seat,
                 departureTime, arrivalTime, departureDate): #define a constructor method to initialize the attributes of the Flight class.
        self.__passengerName = passengerName
        self.__bookingStatus = bookingStatus
        self.__boardingPass = boardingPass
        self.__locationTo = locationTo
        self.__locationFrom = locationFrom
        self.__flightNum = flightNum
        self.__seat = seat
        self.__departureTime = departureTime
        self.__arrivalTime = arrivalTime
        self.__departureDate = date.today()

    def setPassengerName(self, passengerName): #setter method for updating the attribute
        self.__passengerName = passengerName

    def setbookingStatus(self, bookingStatus): #setter method for updating the attribute
        self.__bookingStatus = bookingStatus

    def setBoardingPass(self, boardingPass): #setter method for updating the attribute
        self.__boardingPass = boardingPass

    def setLocationTo(self, locationTo): #setter method for updating the attribute
        self.__locationTo = locationTo

    def setLocationFrom(self, locationFrom): #setter method for updating the attribute
        self.__locationFrom = locationFrom

    def setFlightNum(self, flightNum): #setter method for updating the attribute
        self.__flightNum = flightNum

    def setSeat(self, seat): #setter method for updating the attribute
        self.__seat = seat

    def setDepartureTime(self, departureTime): #setter method for updating the attribute
        self.__departureTime = departureTime

    def setArrivalTime(self, arrivalTime): #setter method for updating the attribute
        self.__arrivalTime = arrivalTime

    def setDepartureDate(self, departureDate): #setter method for updating the attribute
        self.__departureDate = departureDate

    def getPassengerName(self): #getter method for receiving the attribute
        return self.__passengerName

    def getBookingStatus(self): #getter method for receiving the attribute
        return self.__bookingStatus

    def getBoardingPass(self): #getter method for receiving the attribute
        return self.__boardingPass

    def getLocationTo(self): #getter method for receiving the attribute
        return self.__locationTo

    def getLocationFrom(self): #getter method for receiving the attribute
        return self.__locationFrom

    def getFlightNum(self): #getter method for receiving the attribute
        return self.__flightNum

    def getSeat(self): #getter method for receiving the attribute
        return self.__seat

    def getDepartureTime(self): #getter method for receiving the attribute
        return self.__departureTime

    def getArrivalTime(self): #getter method for receiving the attribute
        return self.__arrivalTime

    def getDepartureDate(self): #getter method for receiving the attribute
        return self.__departureDate

    def verifyBoardingPass(self): #define a function that prints a message for verifying that the boarding pass is valid and passenger can proceed into the plane.
        # Implement the boarding pass verification logic here
        print("Passenger present their boarding pass to flight attendees and verifies them to get into the plane")

    def displayFlightInfo(self): #define a function that display flight information
        print(f"Passenger Name: {self.__passengerName}, Booking Status: {self.__bookingStatus.value}, Boarding Pass: {self.__boardingPass.displayBoardingPass()}, Location To: {self.__locationTo}, Location From: {self.__locationFrom}, Flight Number: {self.__flightNum}, Seat: {self.__seat}, Departure Time: {self.__departureTime}, Arrival Time: {self.__arrivalTime}, Departure Date: {self.__departureDate}")


# creating objects

passenger1 = Passenger("Wafaa", "Alfalahi", (1982, 6, 24), 5445628, "UAE", "wafaa.alfalahi@gmail.com", 9715551041,"A56789", SeatPreference.WindowSeat, AirlinePreference.Emirates, ClassPreference.Business) #Creates an instance of the Passenger class named passenger1 with specific attribute values.
check_in1 = CheckIn(5445628, "Wafaa Alfalahi", 38.2, AuthenticationStatus.AuthenticationSuccess) #Creates an instance of the CheckIn class named check_in1 with specific attribute values.
boarding_pass1 = BoardingPass(3, 2, 3389) #Creates an instance of the BoardingPass class named boarding_pass1 with specific attribute values.
flight1 = Flight("Wafaa Alfalahi", BookingStatus.Confirmed, boarding_pass1, "Austria", "Abu Dhabi", "GG233", "A1", 1.30, 9.00, date.today()) #Creates an instance of the Flight class named flight1 with specific attribute values, including the previously created boarding_pass1.

print("Passenger documentation:")
print(passenger1.displayPassenger()) #Displays information about the passenger using the displayPassenger method.

passenger1.setClassPreference(ClassPreference.FirstClass) #updating passenger's class prefernece from business to first class using the setClassPreference method.
passenger1.setSeatPreference(SeatPreference.AisleSeat) #updating passenger's seat preference from window seat to aisle seat using the setSeatPreference method.
passenger1.setAirlinePreference(AirlinePreference.Turkish) #updating passenger's airline preference from emirates to turkish using the setAirlinePreference method
print(passenger1.displayPassenger()) #re-display passenger information with updated version

print("\nCheck-in:")
check_in1.checkBaggageWeight(38.2) #Displays whether the baggage weight is greater than 35 using the checkBaggageWeight method by specifying a weight for it.
check_in1.checkAuthentication() #Displays whether the passenger is authenticated using the checkAuthentication method
check_in1.displayCheckInInfo() #Displays information about the check in using the displayCheckInfo method.

print("\nBoarding Pass:")
print(boarding_pass1.displayBoardingPass()) #Displays information about the boarding pass using the displayBoardingPass method.

print("\nFlight:")
flight1.verifyBoardingPass() #Displays the print statement that a passenger has to present their boarding pass in this step for verification.
flight1.displayFlightInfo() #Dispays information about the flight using the displayFlightInfo method.

flight1.setSeat("A3") #updating seat info since passengers may want to change it during check-in process
flight1.setDepartureTime(3.00) #updating departure time since passengers may want to change it during check-in process
flight1.setArrivalTime(11.00) #updating arrival time since it will be changed when passengers chooses to update their departure time
flight1.displayFlightInfo() #re-display flight information updated version
