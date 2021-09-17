#this will perform the loading and training and comparing of models
# I will use pycaret that automates basically the whole thing
#data loader is in a seperate file just for cleanliness
#written by Moutaz elias

#importing main libraries
import os
from data_loader import DataLoader

def main():

    #load data
    DL=DataLoader(os.getcwd())
    
    train_data=DL.get_data("Train")

    print(train_data)

# This is to avoid the function being called while imported
# This is not neccessary just a safety lock
if __name__ == "__main__":
    main()