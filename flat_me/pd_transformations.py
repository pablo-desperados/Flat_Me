import pandas as pd

def ingest_options(package):
    if package['confirm_transformations'] is False:
        return
