class ClockTime: #constructor
    def __init__(self,hours,minutes,seconds):
        self.hour=hours
        self.minute=minutes
        self.second=seconds

    def setHours(self,hours): #function to only set hours
        self.hour=hours #set value of hours

    def setMinutes(self,minutes): #function to only set minutes
        self.minute=minutes #set value of minutes

    def setSeconds(self,seconds): #function to only set time
        self.second=seconds #set value of seconds

    def setTime(self,hours,minutes,seconds): #function to set hour,minutes and values at once
        self.hour=hours #set value of hours
        self.minute=minutes #set value of minutes
        self.second=seconds #set value of seconds

    def showTime(self):
        print("Time set is "+self.hour+":"+self.minute+":"+self.second) #output format for time

print("Welcome to your clock, please enter input based on 24h clock")
#user input
hour=input("Enter hours:")
minute=input("Enter minutes:")
second=input("Enter seconds:")
clock=ClockTime(hour,minute,second) #instantiate object based on user input
clock.showTime() #call function to showtime