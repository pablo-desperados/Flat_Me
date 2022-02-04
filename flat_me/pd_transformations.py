import pandas as pd
from PyInquirer import prompt

def change_column_name_prompt(column_ix,name):
    question={
        'type':'input',
        'name':f"column_{column_ix}",
        'message':f' #{column_ix} Choose the new name for the column  - {name}: - (press enter to make no changes):',
        'default':f"{name}"
    }

    answer = prompt(question)
    return answer[f"column_{column_ix}"]

def change_column_name(df):
    list_of_columns=df.columns.tolist()
    print(list_of_columns)
    new_list=[]
    for ix,column in enumerate(list_of_columns):
        new_val = change_column_name_prompt(ix,column)
        new_list.append(new_val)
    print(new_list)


def ingest_transformations(package,df):
    if package['confirm_transformations'] is False:
        return df

    transformation_map={'Change Column Names':change_column_name}

    for action in package['transformations']:
        funct_to_call = transformation_map[action]
        funct_to_call(df)
