import csv
import datetime
from hashchain import HashChain
from package import Package

def load_distances():
    # Load distances
    with open("./data/distances.csv", 'r') as myFile:
        tmp = list(csv.reader(myFile))
        d_matrix = []
        for i, row in enumerate(tmp):
            row_values = []
            for j in range(len(row)):
                if row[j] == '':
                    row_values.append(float(tmp[j][i]))
                else:
                    row_values.append(float(row[j]))
            d_matrix.append(row_values)
    return d_matrix

#Pregenerate a time matrix so all this slow math only needs to be calculated once
def get_time_matrix(d_matrix, speed):
    time_matrix = [
        [datetime.timedelta(hours=val / speed) for val in row]
        for row in d_matrix
    ]
    return time_matrix

def get_matrices():
    d_matrix = load_distances()
    t_matrix = get_time_matrix(d_matrix, 18)
    return d_matrix, t_matrix

def load_addresses():
    # Load addresses
    with open("./data/addresses.csv", 'r') as myFile:
        addresses = list(csv.reader(myFile))
        return addresses

def load_packages():
    # Load packages
    packages = HashChain()
    with open("./data/packages.csv", 'r') as myFile:
        items = list(csv.reader(myFile))
        for item in items:
            # Create package object
            # def __init__(self, package_id, address,           city,         zipcode,  time_due,       weight,                                  status,                time_available=datetime.timedelta(hours=8),  truck_restriction=0):
            #                                0        1                   2              3          4    vs       5                                         6                                                7                       8
            #                        6,   3060 Lester St,   West Valley City,  84119,   10:30:00,     88 Kilos,     'Delayed on flight---will not arrive to depot until     9:05 am',              09:05, (a number here if restricted to a truck)

            pkg = Package(
                int(item[0]),  # package id
                item[1],  # address
                item[2],  # city
                item[3],  # zip
                item[4],  # time_due
                item[5],  # weight
                item[6],  # note
                item[7],  # TimeAvailable
                item[8])  # truck restrictions
            # item = Package(0,1,2,3,4,5,6,7,8)
            # Insert into hash chain
            packages.insert(int(item[0]), pkg)
        return packages

# Load data
def load_data():
    addresses = load_addresses()
    packages = load_packages()
    restrictions = get_restrictions()
    return get_matrices(), addresses, packages, restrictions

#returns a tuple of both constraints and package groups
def get_restrictions():
    #constraints means that package[value 0] must be on truck[value 1]
    constraints = [[3,2],[18,2],[36,2],[38,2]]
    #groups must be delivered together
    groups = [[13,14,15,16,19,20]]
    return constraints, groups