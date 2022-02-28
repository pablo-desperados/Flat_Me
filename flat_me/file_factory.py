from .file_classes.csv_to_txt import CsvToTxt
from .file_classes.txt_to_csv import TxtToCsv

class FileFactory():
    @staticmethod
    def create_file(type, answer, path):
        if type =='TXT to CSV':
            return TxtToCsv(path,answer['header_conf'],answer['delimeter'])
        if type =='CSV to TXT':
            return  CsvToTxt(path,answer['header_conf'],answer['delimeter'])

