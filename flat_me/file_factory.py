"""Creates a file object depending on answer to second CLI prompt"""
from .file_classes import CsvToTxt
from .file_classes import TxtToCsv
from .file_classes import CsvToJson

class FileFactory():
    @staticmethod
    def create_file(format_chosen, answer, path):
        if format_chosen =='TXT to CSV':
            return TxtToCsv(path,answer['header_conf'],answer['delimeter'])
        if format_chosen =='CSV to TXT':
            return  CsvToTxt(path,answer['header_conf'],answer['delimeter'],".txt")
        if format_chosen=='CSV to JSON':
            return  CsvToJson(path,answer['header_conf'],answer['delimeter'],".json")
