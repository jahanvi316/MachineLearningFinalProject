# opening files as arrays
#training data files
with open("TrainData1.txt") as TrainData1:
        TrainData1Array = [line.split() for line in TrainData1]
with open("TrainData2.txt") as TrainData2:
        TrainData2Array = [line.split() for line in TrainData2]
with open("TrainData3.txt") as TrainData3:
        TrainData3Array = [line.split() for line in TrainData3]
with open("TrainData4.txt") as TrainData4:
        TrainData4Array = [line.split() for line in TrainData4]
with open("TrainData5.txt") as TrainData5:
        TrainData5Array = [line.split() for line in TrainData5]
with open("TrainData6.txt") as TrainData6:
        TrainData6Array = [line.split() for line in TrainData6]
        
#training label files
with open("TrainLabel1.txt") as TrainLabel1:
        TrainLabel1Array = [line.split() for line in TrainLabel1]
with open("TrainLabel2.txt") as TrainLabel2:
        TrainLabel2Array = [line.split() for line in TrainLabel2]
with open("TrainLabel3.txt") as TrainLabel3:
        TrainLabel3Array = [line.split() for line in TrainLabel3]
with open("TrainLabel4.txt") as TrainLabel4:
        TrainLabel4Array = [line.split() for line in TrainLabel4]
with open("TrainLabel5.txt") as TrainLabel5:
        TrainLabel5Array = [line.split() for line in TrainLabel5]
with open("TrainLabel6.txt") as TrainLabel6:
        TrainLabel6Array = [line.split() for line in TrainLabel6]
        
#test data files
with open("TestData1.txt") as TestData1:
        TestData1Array = [line.split() for line in TestData1]
with open("TestData2.txt") as TestData2:
        TestData2Array = [line.split() for line in TestData2]
with open("TestData3.txt") as TestData3:
        TestData3Array = [line.split() for line in TestData3]
with open("TestData4.txt") as TestData4:
        TestData4Array = [line.split() for line in TestData4]
with open("TestData5.txt") as TestData5:
        TestData5Array = [line.split() for line in TestData5]
with open("TestData6.txt") as TestData6:
        TestData6Array = [line.split() for line in TestData6]
        
 
with open("testing.txt") as testing:
        testing = [line.split() for line in testing]

        
#find missing values (1.00000000000000e+99) and replacing it
def missingValues(array): 
    #print("missingValues called")
    for r in range(len(array)): #loop through array - row
        for c in range(len(array[r])): #loop through array -column
            #print("for loop: ")
            #print(r, c)
            floatVal = (float)(array[r][c])
            if floatVal==1.00000000000000e+99:  #find 1.00000000000000e+99 (missing entry)
                #print("if statement in missingValues successful")
                findSimilarRow(array, r) 
    #print("missingValues end")
    return array;
    
#find patterns for the row of missing value    
def findSimilarRow(array, currentRow):
   # print("findSimilarRow called")
    for r in range(len(array)):
        if r != currentRow:
            #print("if statement in findSimilarRow successful")
            colToFill = isRowTheSame(array[currentRow], array[r]) #check if rows are the same
            if len(colToFill) != 0: #if length is 0, then assume rows not equal, otherwise fill missing columns
                fillMissingColumns(array, currentRow, r, colToFill)#fill all missing columns here
                return array;

#method to find if the rows are the same for missing value rows; returns array of indexes of columns of missing values if same                
def isRowTheSame(missingValRow, comparedRow):
    #print("isRowTheSame called")
    colToFillArray = []
    #print("comparedRow is")
    #print(comparedRow)
    for i in range(len(comparedRow)):
        #print("for loop in isRowTheSame called for ")
        #print(i)
        floatVal = (float)(missingValRow[i])
        if floatVal != 1.00000000000000e99: #if number is not 1.00000000000000e+99
            #print("missingValRow isn't number")
            if missingValRow[i] != comparedRow[i]: #if the rows are not the same
                #print("missingValRow isn't same as comparedRow")
                return [] #return empty array if not the same
            #else:
                #print("missingValRow same as comparedRow")
        else:
            #print("missingValRow is number")
            colToFillArray.append(i) #if it is the missing value (1.00000000000000e+99), add index to array colToFill
    #print("isRowTheSame Ended")
   # print("colToFillArray :")
   # print(colToFillArray)
    return colToFillArray
    

#method to fill in the missing columns found by isRowTheSame
def fillMissingColumns(array, currentRow, row, colToFill):
    for i in range(len(colToFill)):
        currentCol = colToFill[i]
        array[currentRow][currentCol] = array[row][currentCol]
    return array;
    
#method to convert all numbers to floats
def convertToFloat(array):
    for r in range(len(array)): #loop through array - row
        for c in range(len(array[r])): #loop through array -column
            floatVal = (float)(array[r][c])
            array[r][c] = floatVal
    return array;
    
#method to convert all numbers to int
def convertToInt(array):
    for r in range(len(array)): #loop through array - row
        for c in range(len(array[r])): #loop through array -column
            intVal = (int)(array[r][c])
            array[r][c] = intVal
    return array;
  
#method to classify
def classify():
    #insert method here
    return;

#main function to run the file : convert file to readable values, run algorithm, convert it back to integers, and print out
def run(file, num):    
    convertToFloat(file)
    missingValues(file)
    convertToInt(file)
    #print(file)
    arrayToFile(file, num)

#function to format array to file
def arrayToFile(fileIn, fileNum):
    #fileNum = fileIn[10:11]
    fileName = "PatelClassfication" + str(fileNum) + ".txt"
    f = open(fileName, "a")
    #print("arrayToFile called")
    for i in range(len(fileIn)):
        line=""
        for j in range(len(fileIn[i])):
            line += str(fileIn[i][j])+" " 
        f.write(line)
        f.write("\n")
    return f
    
#run(testing, 0) #uncomment line to run on test file
run(TrainData1Array, 1)   #uncomment lin6e to run on TrainData1 file
run(TrainData2Array, 2)   #uncomment line to run on TrainData2 file
run(TrainData3Array, 3)   #uncomment line to run on TrainData3 file
run(TrainData4Array, 4)   #uncomment line to run on TrainData4 file
run(TrainData5Array, 5)   #uncomment line to run on TrainData5 file
run(TrainData6Array, 6)   #uncomment line to run on TrainData6 file