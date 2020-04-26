# Machine Learning Final Project

## Instructions To Run Code
1. Download project .zip file and extract project 
1. Open Command Prompt
1. Navigate to location of Project folder
1. Open file and uncomment appropriate line to run TrainingData set with
     * Line 151 is TrainData1
     * Line 152 is TrainData2
     * Line 153 is TrainData3
     * Line 154 is TrainData4
     * Line 155 is TrainData5
     * Line 156 is TrainData6
1. Run File in command prompt.
    * Use the following command: `Python questionOne.py`

*File currently estimates the missing values. The return should be a completed data set.* 



## Project Description
1. Classification 

**Classification:** Classification is to identify which category a new observation belongs to, on the basis of a training dataset. There are five datasets. For each dataset, we provide the training dataset, training label, and test dataset. Please use the training dataset and training label to build your classifier and predict the test label. A class label is represented by an integer. For example, in the 1st dataset, there are 4 classes where 1 represents the 1st class, 2 represents the 2nd class, etc. Note that, there exist some missing values in some of the dataset (a missing entry is filled by 1.00000000000000e+99), please fill the missing values before perform your classification algorithm. 

TrainData 1 contains 3312 features with 150 samples. Testdata1 contains 3312 features with 53 samples. There are 5 classes in this dataset. 

TrainData 2 contains 9182 features with 100 samples. Testdata2 contains 9182 features with 74 samples. There are 11 classes in this dataset. 

TrainData 3 contains 13  features with 6300 samples. Testdata3 contains 13 features with 2693 samples. There are 9 classes in this dataset. 

TrainData 4 contains 112 features with 2547 samples. Testdata4 contains 112 features with 1092 samples. There are 9 classes in this dataset. 

TrainData 5 contains 11 features with 1119 samples. Testdata5 contains 11 features with 480 samples. There are 11 classes in this dataset. 

TrainData 6 contains 142 features with 612 samples. Testdata5 contains 142 features with 262 samples. This is not a classification problem. You are asked to predict the real value. (Graduate Students Only)

**Sample Data:**
Training data: 

1.1 2.1 2.1 5.2 
2.1 2.4 2.4 2.1 
3.1 1.5 2.6 1.5 

Training label 

1 
1 
2 

Test data 

3.1 2.2 1.5 2.5 
2.1 2.1 2.1 2.6 
