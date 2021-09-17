#THis is written by moutaz elias
#This is a simple data loader and pre processor.
import numpy as np
import os 
import pandas as pd

class DataLoader:
    def __init__(self,path) -> None:
        self.test_path=path+"/test.csv"
        self.train_path=path+"/train.csv"

    def get_data(self,test_train):
        """    
        Fetches training or teesting data
        input:
        "Test" or "Train"
        """
        if test_train=="Test":
            return self._get_test_data()
        elif test_train=="Train":
            return self._get_train_data()
        else:
            print("Option not available")

    def _get_train_data(self):
        return pd.read_csv(self.train_path)

    def _get_test_data(self):
        return pd.read_csv(self.test_path)

