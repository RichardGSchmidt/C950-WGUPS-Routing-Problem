A.  Develop a hash table, without using any additional libraries or classes, that has an insertion function that takes the package ID as input and inserts each of the following data components into the hash table:

•   delivery address

•   delivery deadline

•   delivery city

•   delivery zip code

•   package weight

•   delivery status (i.e., at the hub, en route, or delivered), including the delivery time

    This is achieved by using packages.py in conjunction with hashchain.py, which is implemented in the package load 
    function inside fileops.py (lines: 45-66) insertion function is located in hashchain.py (lines: 25-36).  
    packages.py includes all required data components.

B.  Develop a look-up function that takes the package ID as input and returns each of the following corresponding data components:

•   delivery address

•   delivery deadline

•   delivery city

•   delivery zip code

•   package weight

•   delivery status (i.e., at the hub, en route, or delivered), including the delivery time

    This is achieved by using the package class in conjuction with the hashchain.get() method located in 
    hashchain.py (lines 51-61).  The package being returned includes all required data components.

C.  Write an original program that will deliver all packages and meet all requirements using the attached supporting documents “Salt Lake City Downtown Map,” “WGUPS Distance Table,” and “WGUPS Package File.”

1.  Create an identifying comment within the first line of a file named “main.py” that includes your student ID.

2.  Include comments in your code to explain both the process and the flow of the program.

>Completed

D.  Provide an intuitive interface for the user to view the delivery status (including the delivery time) of any package at any time and the total mileage traveled by all trucks. (The delivery status should report the package as at the hub, en route, or delivered. Delivery status must include the time.)

1.  Provide screenshots to show the status of all packages loaded onto each truck at a time between 8:35 a.m. and 9:25 a.m.

2.  Provide screenshots to show the status of all packages loaded onto each truck at a time between 9:35 a.m. and 10:25 a.m.

3.  Provide screenshots to show the status of all packages loaded onto each truck at a time between 12:03 p.m. and 1:12 p.m.

>Completed.  See task_d_1.png, task_d_2.png, and task_d_3.png in the screenshots directory.

E.  Provide screenshots showing successful completion of the code that includes the total mileage traveled by all trucks.

>Completed. See task_e.png in the screenshots directory.

F.  Justify the package delivery algorithm used in the solution as written in the original program by doing the following:

1.  Describe two or more strengths of the algorithm used in the solution.


>1. Flexibility:  Adding constraints is relatively easy, as it is frequently easier to simulate constraints than it is 
    to determine how to logically deal with them in other algorithms.
>2. Explores Large solution spaces well:  Genetic algorithms are very good at exploring a large varity of solutions that 
    would not usually be explored with a single approach.
>3. Algorithm Load can be throttled flexibly:  Since the bulk of the overall run time complexity of 
    O(Generations * Populations * Packages) are constants Generations and Populations, these 
    constants can be throttled up or down based on whether optimation or speed of processing is a priority.

2.  Verify that the algorithm used in the solution meets all requirements in the scenario.
>All requirements are met: All packages are delivered on time, packages that must be together are together, packages 
 restricted to a truck are on the specified truck, no package is picked up before it is available for pickup.  
 One vehicle returned to hub so that a driver is available before the third vehicle is deployed.  
 The day ends once all packages are delivered (notably this is not when all trucks return to the hub). The package with the wrong
 address now has the wrong address until 10:20:00.

3.  Identify two other named algorithms that are different from the algorithm implemented in the solution and would meet all requirements in the scenario.

    a.  Describe how both algorithms identified in part F3 are different from the algorithm used in the solution.

>1. Dijkstra's Shortest Path Algorithm -  This is an algorithm that chooses the shortest path to each vertex from the home vertex.  
    Unlike my algorithm this algorithm requires heavy modification to also analyze for package delivery constraints such as required delivery times.
>2. Greedy Algorithm -  This is an algorithm that chooses what is considered most optimal when given an option between choices. 
    Determining what is "optimal" can become very challenging as constraints increase, the Genetic Algorithm in the solution instead lets the algorithm determine what is optimal through the processes of natural selection, mutation, and crossover (breeding).

G.  Describe what you would do differently, other than the two algorithms identified in part F3, if you did this project again, including details of the modifications that would be made.

>1. Include dynamic programmed route distances - store computed route distances to a data structure so that a given route's fitness 
    information only needs to be calculated once, save route distances to a CSV file to be reloaded everytime the package is run.
>2. Utilize multithreading - Populations can be generated in parallel in order to speed up computation drastically.

H.  Verify that the data structure used in the solution meets all requirements in the scenario.

>The self adjusting chaining hash table in hashchain.py in conjunction with the package class meets all requirements in the scenario.  
 It has all required components through utilizing the package class, required functions, and self adjusts as size demands increase or decrease.

1.  Identify two other data structures that could meet the same requirements in the scenario.

a.  Describe how each data structure identified in H1 is different from the data structure used in the solution.

>1. Linear probing Open Addressing Hash table:  This differs from the hashchain class used by storing values in buckets next to occupied 
    buckets.  Chaining hash tables instead append values to a list at the bucket index.
>2. Double Hashing Open Addressing Hash table:  This differs from the hashchain class by using two keys in the formula 
    (h1(key)+i*h2(key))mod (tablesize), whereas chaining hash tables only use one key.

I.  Acknowledge sources, using in-text citations and references, for content that is quoted, paraphrased, or summarized.

J.  Demonstrate professional communication in the content and presentation of your submission.
