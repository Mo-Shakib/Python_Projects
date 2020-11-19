# Author: Mohammad Shakib
#Documentation: https://pypi.org/project/tabulate/
from tabulate import tabulate # importing tabulate

#data table
data = [['Name', 'ID', 'Age'],['Mr. A', '101', '16'],['Mr. Y', '102', '12'],['Mr. Z', '103', '16'],['Mr. S', '105', '21'],['Mr. K', '108', '19']]

print(tabulate(data,headers='firstrow',tablefmt='grid'))

