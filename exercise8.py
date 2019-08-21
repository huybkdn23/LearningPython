import random
def is_sorted(lst):
    previous = lst[0]
    for element in lst:
        if element < previous: return False
        previous = element
    return True

def has_duplicates(lst):
    for element in lst:
        if lst.count(element) >= 2: return True
    return False

def remove_duplicates(lst):
    array = lst[:]
    array.sort()
    for i in range(len(array) - 1):
        if array[i] == array[i+1]: 
            del array[i]

    return array

def random_birthdays(n):
    birthdays = []
    for i in range(n):
        random_birth = random.randint(1,365)
        birthdays.append(random_birth)
    print(birthdays)
    return birthdays

def count_matches(students, samples):
    '''
    Returns the number of matches if there's at least one match in sample
    '''
    count = 0
    for i in range(samples):
        #: generate a random list birthday of students
        birthdays = random_birthdays(students)
        if has_duplicates(birthdays): count += 1
    return count

print(is_sorted(['a', 'a','b']))
print(has_duplicates(['a', 'b', 'c', 1, 1]))
print(remove_duplicates(['huy', 'huy', 'ekhgsdjh', 'ajhgrk4bskd', 'c']))
print(count_matches(5, 15))
