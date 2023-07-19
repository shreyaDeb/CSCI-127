import numpy as np
import matplotlib.pyplot as plt

def read_file(file_name):
    file = open(file_name, 'r')
    
    nums = []
    courses = []
    
    for entry in file:  #Adds the numbers to one list and the college to the other
        lists = entry.strip().split(',')
        num = lists[0]
        course = lists[1]
        nums.append(num)
        courses.append(course)
        
    
    nums = nums[1:]     #Gets rid of the first entry in the csv (The titles)
    courses = courses[1:]
    
    nums_int = []
    
    for entry in nums:  #Turns each number string into an integer
        nums_int.append(int(entry))
        
    enrollment = tuple(np.array(nums_int))  #Creates tuples of numpy arrays of the two lists
    college = tuple(np.array(courses))
    
    return (college, enrollment)

# -------------------------------------------------

def main(file_name):
    
    college_names, college_enrollments = read_file(file_name)
  
    colors = ['gold','blue',]   #Sets colors for graph
    plt.bar(college_names, college_enrollments, color = colors) #Sets axis of graph
    plt.title('MSU Enrollments\nFall 2020')      #Titles graph
    plt.ylabel('Enrollment')    #Titles y axis
    plt.xlabel('College')       #Titles x axis
    plt.ylim(0, 5000, 1000)     #Sets scale for y axis
    plt.show()                  #Displays graph
    
# -------------------------------------------------

main("fall-2020.csv")

