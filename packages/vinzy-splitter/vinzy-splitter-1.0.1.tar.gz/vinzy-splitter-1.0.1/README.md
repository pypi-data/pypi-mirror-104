## A package will help you to split your data frame into training, validation and testing subsets

## Working:
Splits arrays or matrices into random train, validation and test subsets
"train_val_test_split" function accepts independent features(X), dependent
feature (y), validation size (default size = 0.15),test size (default size = 0.15) and shuffle (default = True) as input parameters and returns X_train,X_val,X_test,y_train,y_val,y_test

Note: If shuffle parameter is True, after shuffling index of all records will be reset in ascending order

## How to use it:

from vinzy_splitter import train_val_test_split

X_train,X_val,X_test,y_train,y_val,y_test = train_val_test_split(X,y,val_size=0.15,test_size=0.15,shuffle=True)

after executing the function your data frame will be splitted into training,validation and testting subsets based on validation and testing size you have provided, deafult value will be 15% for both and suffling will be True.