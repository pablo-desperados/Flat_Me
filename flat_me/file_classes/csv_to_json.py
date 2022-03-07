"""Creates class to handle conversion from csv to json"""

from .csv_utils import CsvUtils
import pandas

pandas.DataFrame.to_json()
class CsvToJson(CsvUtils):
    def __init__(self,path,header,delim,dest_extension):
        CsvUtils.__init__(self,path,header,delim,dest_extension)

    def return_file(self,df):
        """Creating a JSON file out of a structured csv file"""
        print("Creating csv in the specified path...")

        try:
            json_path = self.path.replace('.csv','.json')
            df.to_json(json_path,orient="columns")
        except ValueError as value_error:
            raise ValueError("Something went terribly wrong when returning the txt file!") from value_error


