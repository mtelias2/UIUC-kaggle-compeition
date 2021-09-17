#THis is written by moutaz elias
#This is a simple data loader and pre processor.
import numpy as np
import os 
import pandas as pd
class DataLoader:
    def __init__(self,path) -> None:
        self.test_path=path+"test.csv"
        self.train_path=path+"train.csv"
