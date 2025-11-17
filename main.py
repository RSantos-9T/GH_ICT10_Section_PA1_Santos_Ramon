# Working with Sets
from pyscript import display, document


glee = {'Sang', 'Jalainie', 'Carl', 'Joaquin', 'Alijah', }
dance= {'Jennifer', 'Carl', 'Euan', 'Sean', 'Jalainie', 'calvin'}

display(glee | dance, target='one') 
display(glee & dance, target='both') 
display(glee - dance, target='first') 
display(dance - glee, target='second')
display(glee ^  dance, target='onlyone') 
