import copy
import datetime

rules = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

class Time(object):
    '''
    Represents the time of day
    Attributes: hour, minute, second
    '''
    def __init__(self, hour = 0, minute = 0, second = 0):
        '''
        This method is called when we create an object
        '''
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def __str__(self):
        '''
        This method is called when we print an object
        '''
        return 'Today is %.2d:%.2d:%.2d' %(self.hour, self.minute, self.second)

    def __add__(self, other):
        '''
        Overloading the + operator
        '''
        #: This is called type-based dispatch
        if isinstance(other, Time):
            return self.add_time(other)
        else: return self.increment(other)

    def __radd__(self, other):
        '''
        This method is invoked when a Time object appears on the right side of the + operator.
        '''
        return self.__add__(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def print_time(self):
        print('%.2d:%.2d:%.2d'%(self.hour, self.minute, self.second))

    def time_to_int(self):
        '''
        This method parses the time to integer
        '''
        return self.hour * 3600 + self.minute * 60 + self.second

    def increment(self, seconds):
        '''
        Increase the current time to 'seconds' times
        '''
        a = self.second + seconds
        b = self.minute + a/60
        self.second = a % 60
        self.minute = b % 60
        self.hour += b / 60

    def is_after(self, t2):
        '''
        Check whether time > t2
        '''
        a = self.hour * 3600 + self.minute * 60 + self.second
        b = t2.hour * 3600 + t2.minute * 60 + t2.second
        return a > b

def add_time(t1, t2):
    '''
    t1 + t2
    '''
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
    if sum.hour >= 24: sum.hour -= 24
    return sum


def pure_version(time, second):
    result = copy.copy(time)
    result.increment(second)
    return result


def int_to_time(seconds):
    time = Time()
    time.hour = seconds / 3600
    tmp = seconds % 3600
    time.minute = tmp / 60
    time.second = tmp % 60
    return time

def mul_time(time, n):
    seconds = time.time_to_int()
    result = int_to_time(int(round(seconds * n)))
    return result

def get_date_now():
    '''
    This function gets the current date and prints the day of the week
    '''
    datetime_object_today = datetime.datetime.today()
    day_of_week = datetime.datetime.weekday(datetime_object_today)
    print(datetime_object_today)
    print('1) Today is %s' %rules[day_of_week])

def birthday_stats(birthday):
    today = datetime.datetime.now()
    age = today.year - birthday.year
    if (birthday.month == today.month) and (birthday.day <= today.day):
        pass
    elif birthday.month < today.month:
        pass
    else:
        age -= 1
    birthday_ = datetime.datetime(today.year, birthday.month, birthday.day)
    till_birthday = str(birthday_ - today).split()
    print(till_birthday)

    if len(till_birthday) > 1:
        days = int(till_birthday[0])
        time = till_birthday[2].split(":")
    else:
        days = 365
        time = till_birthday[0].split(":")

    hours = time[0]
    mins = time[1]
    secs = time[2][:2]

    if (days < 0) and (days != 365):
        days = 365 + days
    elif (days == 365):
        days = 0
    else:
        days = abs(days)

    print(("2) You are %s years old; %sd:%sh:%sm:%ss until your next birthday."
    % (age, days, hours, mins, secs)))

time = Time()
time.hour = 9
time.minute = 2
time.second = 30
# time.print_time()
get_date_now()
my_birth_day = datetime.datetime(1998, 10, 13)
birthday_stats(my_birth_day)
