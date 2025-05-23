#Author: Richard Schmidt ID:010869529
# #C950 WGUPS Routing Program

#Initialization section
import vehicle
import datetime
from package import get_header, Package
from genetic_algorithm import genetic_algorithm, simulate_delivery
from fileops import load_data


matrices, addresses, packages, restrictions = load_data()

HUB = 0

#print(f'distances : {distance_matrix},\n addresses : {addresses},\npackages : {packages}')

def str_all_packages(package_hashmap):
    keys = package_hashmap.keys()

    return_string = f'\n{get_header()}\n'
    for ki in keys:
        return_string = return_string + f'{package_hashmap.get(ki)}\n'
    return return_string

def update_all_packages(query_time,package_hashmap):
    keys = package_hashmap.keys()
    for ki in keys:
        package_hashmap.get(ki).update(query_time)


wgups1 = vehicle.Vehicle(16,18,None,[1,13,14,15,16,19,20,21,27,29,30,34,35,37,39,40],0.0, HUB, datetime.timedelta(hours=8))
wgups2 = vehicle.Vehicle(16,18,None,[3,6,7,11,12,18,22,23,24,25,26,31,32,36,38],0.0, HUB, datetime.timedelta(hours=9, minutes= 5))
wgups3 = vehicle.Vehicle(16,18,None,[2,4,5,8,9,10,17,28,33],0.0, HUB, datetime.timedelta(hours=10, minutes= 20))


# Run the genetic algorithm
best_solution, best_distance = genetic_algorithm(
    [wgups1, wgups2, wgups3],
    packages,
    matrices,
    pop_size=5000,
    generations=250,
    crossover_rate=0.9,
    mutation_rate= 0.05
)

# Simulate delivery with the optimized solution
optimized_trucks, total_mileage, optimized_packages = simulate_delivery(best_solution, [wgups1,wgups2,wgups3], packages, matrices)

print(f"\nbest solution: {best_solution}")
print(f"best distance: {float(best_distance):.1f} miles")
go_time = datetime.timedelta(hours=20)
#update_all_packages(go_time,packages)
for key in optimized_packages.keys():
    tmp_pack = optimized_packages.get(key)
    tmp_pack.update(go_time)
print(f'optimized packages:{str_all_packages(optimized_packages)}')

print(f'total milage: {total_mileage:.1f}, wgups1 = {optimized_trucks[0].mileage:.1f}, wgups2 = {optimized_trucks[1].mileage:.1f}, wgups3 = {optimized_trucks[2].mileage:.1f}')


