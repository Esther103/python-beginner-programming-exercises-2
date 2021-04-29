import random

def get_color(color_number=4):
    # making sure is a number and not a string
    color_number = int(color_number)

    switcher={
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    return switcher.get(color_number,"Invalid Color Number")


def get_allStudentColors():

    example_color = 1
    students_array = []
    #your loop here
    for i in range(10):
        numero = random.randint(1, 4)
        print(get_color)



get_allStudentColors()


#     def standards_maker():
#     #your code here
#     for i in range(300):
         
#         print('will write questions if I am stuck')
        

# standards_maker()





print(get_allStudentColors())