from os.path import exists
import pandas as pd

class TxtToCsv:
    """Create an object that handles txt to pandas convertion"""
    def __init__(self,path,header,delim,dest_extension='.csv',cur_extension='.txt'):
        self.path = path
        self.header= header
        self.dest_extension = dest_extension
        self.cur_extension = cur_extension

        if len(delim)==0:
            self.delim=","

        elif delim.lower() =='tab':
            self.delim='\t'

        else:
            self.delim = delim



    def validate_file(self):
        if exists(self.path) and self.path.endswith('.txt'):
            return True
        raise FileNotFoundError("You have either entered the wrong path to the file or the file is not a .txt file")



    def retur_pd(self):
        """Return pandas DF for txt files"""
        final_header = None
        if self.header is True:
            final_header = 0

        if self.validate_file():
            df = pd.read_csv(self.path, sep=self.delim, header=final_header,engine='python')
            return df


    def return_file(self,df):
        print(f"Creating csv in the specified path")
        try:
            csv_path = self.path.replace('.txt','.csv')
            df.to_csv(csv_path,encoding='utf-8',index=False)
            print("Process completed, enjoy your new file(s)!")

        except:
            raise ValueError("Something went terribly wrong when returning the csv!")



