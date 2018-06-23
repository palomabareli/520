#!/usr/bin/python3

linguage = input('What is yours linguage of program favorite?: ')

linguage = linguage.lower().strip()

if linguage == 'python':
    print('It is right. Very Good!')
elif linguage == 'goland':
    print('It is right. Good!')    
else:
    print('It is wrong. Come on!')