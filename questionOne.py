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
    print("missingValues called")
    for r in range(len(array)): #loop through array - columns
        for c in range(len(array[r])): #loop through array -rows
            print("for loop: ")
            print(r, c)
            if array[r][c] == ("1.00000000000000e+99"):  #find 1.00000000000000e+99 (missing entry)
                print("if statement in missingValues successful")
                findSimilarRow(array, r) 
    print("missingValues end")
    return array;
    
#find patterns for the row of missing value    
def findSimilarRow(array, currentRow):
    print("findSimilarRow called")
    for r in range(len(array)):
        if r != currentRow:
            print("if statement in findSimilarRow successful")
            colToFill = isRowTheSame(array[currentRow], array[r]) #check if rows are the same
            if len(colToFill) != 0: #if length is 0, then assume rows not equal, otherwise fill missing columns
                fillMissingColumns(array, currentRow, r, colToFill)#fill all missing columns here

#method to find if the rows are the same for missing value rows; returns array of indexes of columns of missing values if same                
def isRowTheSame(missingValRow, comparedRow):
    print("isRowTheSame called")
    colToFillArray = []
    for i in range(len(comparedRow)):
        if missingValRow[i] != 1.00000000000000e+99: #if number is not 1.00000000000000e+99
            if missingValRow[i] != comparedRow[i]: #if the rows are not the same
                return [] #return empty array if not the same
        else:
            colToFillArray.append(i) #if it is the missing value (1.00000000000000e+99), add index to array colToFill
    print("isRowTheSame Ended")
    return colToFillArray
    

#method to fill in the missing columns found by isRowTheSame
def fillMissingColumns(array, currentRow, row, colToFill):
    for i in len(colToFill):
        currentCol = colToFill[i]
        array[currentRow][currentCol] = array[row][currentCol]
        return array;
  
#method to classify
def classify():
    #insert method here
    return;
    

missingValues(testing)
print(testing)