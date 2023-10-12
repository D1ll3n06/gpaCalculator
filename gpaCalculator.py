# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:39:57 2023

@author: dille
"""

"""
NAME:
    collectionGrades

DESCRIPTION:
    This function accepts keyboard input of course codes and associated letter
    grades. The output is stored in a DICTIONARY with KEY = Course code and 
    VALUE = Course letter grade
    
INPUT
    None

OUTPUT: 
    Dictionary containing entries:
        KEY = Course code
        VALUE = Course letter grade 
        
FUNCTIONAL:
        1. For each class attempted, collect course code and letter grade
        2. For each class inputed, it will display what the user had recorded
        3. Ask the user if they would like to add more courses
        4. Save their input into a dictionary 

NONFUNCTIONAL:
    * There will be no consideration of credits earned during highschool
    * There will be no consideration of drops/withdraws
    * There will be no consideration of transfer courses
    * There will be no consideration of CN/NR courses
    * Limit user input as much as is functional 
    * Design the application using function to make it more flexible and 
      to allow for reuse of code


VALIDATION
    * Will make sure that course identifier is 6-7 characters and ends with a
      number at the end to identify hours
    * Will make sure that input of letter grade is correct. Compares input with
      a list of correct letter grade choices
    * Does not consider inputs that do not match a course at UTSA (EX: BABSD1)
    * Does not consider a limit on course hours (EX:IS3009)
    
      
    
LIMITATION
    * Does not allow the user to redo an entry if it was inputted wrong
        *a loop hole to this however is if the user adds another entry and 
         rewrites the entry with the same course identifier it will overwrite 
         the incorrect one this is due to the fact that dictionaries do not 
         allow for duplicates
         
     
      
"""

### FILE DEDICATION BEGINS HERE ###




### FUNCTIONS BEGIN HERE ###

def collectGrades( ) -> dict:
    
    gradeCollection = dict( )
    
    #Ask student User for INPUT...
    print ( "We will collect your grades to begin calculations." )
    print ( "Please provide course number as a 6 - 7 character course identifier," )
    print ( "  in the form of IS3003 or ACC3413" )
    print ( ) #for readability
    
    print ( "Please enter grades as letter grades of one or two characters. " )
    print ( "          (A+, B-, F)" )
    print ( ) #for readability
    
    #set a loop control 
    another = 'yes'
    
    # This while iteration will ask the user to input the course code and the 
    # letter grade associated with it. It will then display those inputs. Finally
    # it will ask the user if they want to continue entering courses. If the 
    # user says no it will end the iteration
    
    while ( another == 'yes' ):
        
        #Accept input of course code
        course = input( "Please enter the course identifier: " ).strip( )
        
       # This gets the last element of course. This will be used to determine 
       # if it's a digit. We want a digit since this represents the amount of 
       # hours a student has earned in the course
        lastElement = course[-1] 
        courseCheck = True # used to determine the status of the course check 
                   
        
        # This iteration will check to see if the user course code matches the 
        # form specified in the instructions (6-7 characters and ends in a number)
        # If the user does not do it correctly it will ask the user to re-enter
        # a course until it matches the form specified (see above function to 
        # view limitations) 
        
        while courseCheck :
                       
        
            # This if statement is looking for 2 things: that the user input is
            # 6-7 characters and that the last element is a number 
            
            if  lastElement.isdigit() and (len(course) == 6 or len(course) == 7):
                   courseCheck = False
            else:
                # Displays the user that their input was incorrect
                print() #for readability
                print("YOUR INPUT DID NOT MATCH THE CRITERIA ABOVE")
                print("It should be a 6-7 character course and")
                print("   in the form of IS3003 or ACC3413")
                print() #for readability
                       
                # ask the user to re-enter another letter grade
                course = input( "Please re-enter the course identifier: " ).strip( ) 
                
            # This gets the last element of course. This will be used to 
            # determine if it's a digit. We want a digit since this represents 
            # the amount of hours a student has earned in the course
                lastElement = course[-1]
                
            # This if statement is looking for 2 things: that the user input is
            # 6-7 characters and that the last element is a number               
                if lastElement.isdigit() and (len(course) == 6 or len(course) == 7):
                    courseCheck = False
                               
                #end of selection
            #end of selection
        #end of iteration
            
            
            
        #this list will be used to compare the letter grade the user inputs        
        letterGrade = ["A+" ,"A" ,"A-",
                   "B+" ,"B" ,"B-",
                   "C+" ,"C" ,"C-",
                   "D+" ,"D" ,"D-",
                   "F",
                     ]

        #Accept input of letter grade 
        grade = input( "Please enter the course letter grade: " ).strip( ).upper( )
        gradeCheck = True # used to determine the status of the grade check 

        # this iteration will check to see if the users letter grade matches the
        # form specified in the beginning instruction. If not it will ask the user
        # to input another letter grade until it matches. This will use the list 
        # to make sure the users input matches one of the letter grades.
    
    
        while gradeCheck:  
            
            if grade in letterGrade:
                gradeCheck = False
            else:
                # Displays the user that their input was incorrect 
                print() #for readability
                print("YOUR INPUT DID NOT MATCH THE CRITERIA ABOVE")
                print("Your letter grade should be in the form of ")
                print("              A+,B,F,C-")
                print() #for readability
                 
                # ask the user to re-enter another letter grade
                grade = input( "Please re-enter the course letter grade: " ).strip( ).upper( )
               
                # if letter grade matches one of the letter grades in the list 
                # the program will end 
                if grade in letterGrade:
                    gradeCheck = False   
                    # ends the iteration. this means that the users input matches 
                    # the form in the begining instructions
                
                #end of selection
           #end of selection
        #end of iteration
        
        
    
        #MIRROR the input back to the user
        print( "You received a grade of %s in course %s." %
                  (grade, course) )
        
        #Add the input to our DICTIONARY 
        gradeCollection[ course ] = grade
        
        #Ask if the student USER wishes to continue...
        another = input( "Enter Yes to add another course. " ).lower( ).strip( )
        
        #end iteration//course and grade input.
        
    # Will return the the users inputs into the form of a dictionary
    return gradeCollection # (course code : letter grade)

#end FUNCTION collectGrades







# start of function calculateQualityPts
"""
NAME:
    calculateQualityPts

DESCRIPTION:
    This function accepts a dictionary named 'grades' as its parameter. It will 
    then use the KEY values to calculate the amount of hours a student has done.
    The VALUE portion of the dictionary will be used to determine points based
    off the letter grade. After it will then do a calculation which gives us
    the total points earned (assinged to varible 'points') per course. The function 
    will give, in the form of a tuple, the total hours and the total points earned.
    
  
    
    KEY = Course code and 
    VALUE = Course letter grade
    
INPUT
    Dictionary given the name grades:
        (grades: dict)

OUTPUT: 
    Tuples containing entries:
        (credits, points)
       
        
FUNCTIONAL:
        1. It will take a dictionary as its parameter 
        
        2. For each course code it will take the last element (indicator of 
           the hours per course) and add it up in the variable 'hours' which 
           the total will be stored in the variable 'credit'4
    
        3. Across all classes, it will determine the points by comparing the
          the letter grade and the corresponding points earned using the dictionary 
          'qualityPts'. It will store the total in 'quality'.
        
        4. Multiply 'quality' by 'hours' to get the quality points per course.
          Store in 'points'
        
        5. return 'credits' and 'points' in the form of a tuple.

NONFUNCTIONAL:    
    * Limit user input as much as is functional 
    * Design the application using function to make it more flexible and 
      to allow for reuse of code
      
"""



# right arrow = more notation than python code 
# provide documentation that we are returning a tuple

def calculateQualityPts( grades: dict ) -> tuple:
    
    # Begin by defining a "lookup" structure for assigning quality points
    qualityPts = {"A+" : 4.33,
                  "A"  : 4.00,
                  "A-" : 3.67,
                
                  "B+" : 3.33,
                  "B"  : 3.00,
                  "B-" : 2.67,
                
                  "C+" : 2.33,
                  "C"  : 2.00,
                  "C-" : 1.67,
                            
                  "D+" : 1.33,
                  "D"  : 1.00,
                  "D-" : 0.67,
                            
                
                   "F" : 0.00,

                }                   # end of DICTIONARY
    
    # Traverse the RECEIVED dictionary to accumulate credit hours &
    # quality points. 
    
    credits = 0 # total amount of hours taken
    points = 0.0 # total amount of points earned 
    
    
    # This for iteration will go through all the key:value pairs within the 
    # the users dictionary and determine total hours and points earned.  
    
    
    for course, grade in grades.items( ):
        
        # Retrieving CREDIT HOURS from course code by using the last element
        hours = int( course[-1] )
        
        # uses the amount in 'hours' and adds it up in 'credits' which represents 
        # the student total hours
        credits += hours
        
        # retrieve quality points for the grade 
        
        # gets the corresponding points in the dictionary 'qualityPts' by 
        # using 'grade' (the VALUE portion of the users dictionary ) 
        quality = qualityPts [grade] 
        
        # points represent the points earned per course and adds it into 'points'
        points += (quality * hours )
    # end iteration
        
    # Return the TUPLE containing summed credits and quality points
    return  credits, points

#end of function calculateQualityPts


# start of GPA Calculator

"""
This application is a simple GPA calculator 

FUNCTIONAL:
        1. For each class attempted, collect letter grade and course hours
        2. For each class, calculate "quality points"; sum the calculation result
        3. Across all classes, sum credit hours attempted
        4. Divide TOTAL quality points by TOTAL credit hours
        5. Display result to user

NONFUNCTIONAL:
    * There will be no consideration of drops/withdraws
    * There will be no consideration of transfer courses
    * There will be no consideration of CN/NR courses
    * Limit user input as much as is functional 
    * Design the application using function to make it more flexible and 
      to allow for reuse of code5
        
"""

# NOW, let's pull all of this together.....

# Call the collectGrades function
# if a function returns a value you need to give a name to that return value
myGrades = collectGrades ( ) 

# called the calculateQualityPts function while also using a dictionary as a 
# arguement to retrieve a tuple and store it in gpaInfo
gpaInfo = calculateQualityPts( myGrades )

# UNPACK to the returned TUPLE
creditHours, qualityPoints = gpaInfo

# Use the unpacked values to CALCULATE the overall GPA
gpa = qualityPoints / creditHours

# Present user's GPA
print()  #for readability
print ("My GPA is: %s" % "{:.2f}".format(gpa) )

