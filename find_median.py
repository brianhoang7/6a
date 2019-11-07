# Author: Brian Hoang
# Date: 11/06/2019
# Description: function that takes list as parameter and finds the median of that list


#function takes list as parameter
def find_median(my_list):
    #sorts list from least to greatest
    my_list.sort()
    #distinguishes even number of items in list
    if len(my_list) % 2 == 0:
        #finding the smallest number of the second half of the list
        num1 = my_list[int(len(my_list)/2)]
        #finding the largest number of the first half of the list
        num2 = my_list[int(len(my_list)/2 - 1)]
        #adding the two numbers up and dividing by 2 to return the median
        sum1 = num1 + num2
        return sum1/2
    #finds the number in the center of the list to return as the median for lists with odd number of objects
    elif len(my_list) % 2 != 0:
        num1 = my_list[round(len(my_list)/2)]
        return num1


#my_list = [4,5,3,7,8,3,1,12,13]
#print(find_median(my_list))