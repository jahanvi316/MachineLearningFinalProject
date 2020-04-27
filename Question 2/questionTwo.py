# opening files as arrays
#Missing data files
with open("MissingData1.txt") as MissingData1:
        MissingData1Array = [line.split() for line in MissingData1]
with open("MissingData2.txt") as MissingData2:
        MissingData2Array = [line.split() for line in MissingData2]
with open("MissingData3.txt") as MissingData3:
        MissingData3Array = [line.split() for line in MissingData3]


        
#find missing values (1.00000000000000e+99) and replacing it
def missingValues(array): 
    #print("missingValues called")
    for r in range(len(array)): #loop through array - row
        for c in range(len(array[r])): #loop through array -column
            #print("for loop: ")
            #print(r, c)
            #floatVal = (float)(array[r][c])
            if array[r][c]==1.00000000000000e+99:  #find 1.00000000000000e+99 (missing entry)
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
        #floatVal = (float)(missingValRow[i])
        if missingValRow[i] != 1.00000000000000e99: #if number is not 1.00000000000000e+99
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
    
  
#method to classify
def classify():
    #insert method here
    return;

#main function to run the file : convert file to readable values, run algorithm, convert it back to integers, and print out
def run(file, num):    
    #convertToFloat(file)
    missingValues(file)
    #print(file)
    arrayToFile(file, num)

#function to format array to file
def arrayToFile(fileIn, fileNum):
    #fileNum = fileIn[10:11]
    fileName = "PatelMissingResult" + str(fileNum) + ".txt"
    f = open(fileName, "a")
    #print("arrayToFile called")
    for i in range(len(fileIn)):
        line=""
        for j in range(len(fileIn[i])):
            line += str(fileIn[i][j])+" " 
        f.write(line)
        f.write("\n")
    return f
    
run(MissingData1Array, 1)   
run(MissingData2Array, 2)  
run(MissingData3Array, 3)  
