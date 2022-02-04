from __future__ import print_function, unicode_literals
import argparse
from PyInquirer import prompt
from pyfiglet import Figlet
from .txt_to_csv import TxtToCsv


def file_factory(choice,path):
    if choice=='TXT to CSV':
        temp_prompt=[{
            'type':'input',
            'name':'delimeter',
            'message': 'What is the delimeter/separator used in your text file?'\
                       ' For tab separated files type: "TAB" (Default is ",")'
        },
            {
                'type':'confirm',
                'name':'header_conf',
                'message':'Does your file contain any headers? (Default is yes)',
                'default':True
            }
        ]
        answer= prompt(questions=temp_prompt)
        return TxtToCsv(path,answer['header_conf'],answer['delimeter'])



def greet_user():
    font= Figlet(font='standard',justify='center')
    print(font.renderText("Welcome to Flat_Me !"))
    name_prompt= {
        'type':'input',
        'name':'user_name',
        'message':'Before we begin, let\'s start with something easy: What is your name?'
    }
    answer = prompt(questions=name_prompt)

    if len(answer['user_name']) == 0:
        answer['user_name'] = "John Doe"

    return answer['user_name']


def choose_file_option(name):

    #TODO: limit choices depending on file chosen

    file_prompt={
        'type':'list',
        'name':'convertion_type',
        'message': f'Hi {name}, how do want to use Flat_Me today?',
        'choices':['CSV to TXT', 'TXT to CSV']
    }
    answer = prompt(questions=file_prompt)
    return answer['convertion_type']

def choose_transformations(name):
    transformations_prompt=[
        {
            'type':'confirm',
            'message':'Would you like to apply some transformations to the file? (Default is no)',
            'name':'confirm_transformations',
            'default':False
        },

        {
        'type':'checkbox',
        'message':f'Ok {name}, let\'s select some transformation before we convert your file:',
        'name':'transformations',
        'choices':[
            {'name':'Change Column Names'},
            {'name':'Change File Name'}
        ],
        'when': lambda answers: answers['confirm_transformations']
    }
    ]

    answers = prompt(questions=transformations_prompt)
    print(answers)
    return answers

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p','--path',help=
                        'Specifies location of the file',required=True)
    args = parser.parse_args()
    user_name=greet_user()
    choice= choose_file_option(user_name)
    file_class = file_factory(choice,args.path)
    initial_pd=file_class.retur_pd()
    transformations = choose_transformations(user_name)
    file_class.return_csv(initial_pd)
