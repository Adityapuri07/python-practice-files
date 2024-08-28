import random
import os

fruit_dict={
    1:"apple",
    2:"banana",
    3:"orange",
    4:"mango",
    5:'Pineapple',
    6:'Strawberry',
    7:'Watermelon',
    8:'Grape',
    9:'Kiwi',
    10:'Peach'
}

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_terminal()    

def game(level):
    total_point=0
    while True:
      print("remember the fruit name with corresponding number")
      selected_fruit={}
      key_for_selection=random.sample(list(fruit_dict.keys())),level
      print(key_for_selection)
      for keys in key_for_selection:
        
         


