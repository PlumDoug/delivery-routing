Author: Douglas Faehndrich
Student ID: 012315568
Submission for WGU C950 - Data Structures and Algroithms II - Task 2

Instructions:
Create an app that utilizes a self adjusting algorithm and a custom hash table (no dict) to efficiently route 40 packages on 3 trucks with 2 drivers. Distances between delivery addresses, earliest start times, package deadlines, and special reuqests are provided. 

Explanation:
This app utilizes a nearest neighbor (greedy) algorithm and a custom hash table with simple chaining for collision resolution. It has methods for processing the data, inserting into the hash table searching the hash table, and checking the status of packages at specific times. It manually loads the trucks. It has a simple CLI to check the status of individual packages and to print the status of all packages at any given time. 
