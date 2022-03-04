#Code i got online :(
def b1e_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swapped = True

random_list_numbers = [5,123,12,34,2,12,123]

#bubble_sort(random_list_numbers)
#print(random_list_numbers)


# Attempt 1 (fail) :

def b2e_sort(nums):
    loop = True
    while loop:
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i],nums[i+1] = nums[i+1], nums[i]
            elif nums[i+1]:
                pass


# Attempt 2:
# This time I think I got it.

def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i],nums[i+1] = nums[i+1], nums[i]
                swapped = True
            

bubble_sort(random_list_numbers)
print(random_list_numbers)
            
 # ok but i still kinda was gonna write the same thing

 
                




        

        
