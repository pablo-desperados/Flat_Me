from os.path import exists
import pandas as pd
import numpy as np

class CsvToTxt:
    '''Creates an object for pd tranformations and file exporting'''
    def __init__(self,path,header,delim):
        self.path = path
        if len(delim)==0:
            self.delim=","
        elif delim.lower() =='tab':
            self.delim='\t'
        else:
            self.delim = delim
        self.header= header

    def validate_file(self):
        if exists(self.path) and self.path.endswith('.csv'):
            return True
        raise FileNotFoundError("You have either entered the wrong path to the file or the file is not a .csv file")


    def retur_pd(self):
        """Return pandas DF for txt files"""
        final_header = None
        if self.header is True:
            final_header = 0

        if self.validate_file():
            df = pd.read_csv(self.path, sep=self.delim, header=final_header,engine='python')
            return df

