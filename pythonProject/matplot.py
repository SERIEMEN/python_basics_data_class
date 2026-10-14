import numpy as np
import matplotlib.pyplot as plt

# the matplotlib module is used to visualize data that has been collected through other means.
# It can help to visualize data as graphs, charts, etc. and you can use it with minimal code.

# remove the docstrings or comments around the blocks of code individually and run them




base = [1,2,3,4,5]
squares = [1,4,9,16,25]
cubes = [1,8,27,64,75]
days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
sales = [23,46,32,19,39,64,22]
#plt.style.use('seaborn')

# you can optionally add styles to your visual presentations to change how they look. Try removing this line and see the output
# You can look up the other styles you can use



fig, ax=plt.subplots() # the subplots module can be used to generate one or more plots in the same figure
ax.plot(squares) # the plot method will try to show the data it's given in a meaningful way



#plt.plot(base,squares,label='Line 1',color='purple') # a 2 line graph
#plt.plot(base,cubes,label='Line 2',color='red')# You can plot multiple lines on a graph and label and color them
# you could also concatenate it as plt.plot(base,squares,label='Line 1',color = 'purple',base,cubes,label='Line 2',color='red')


#plt.scatter(squares,cubes,s=10)# a scatter plot graph


'''
plt.bar(days,sales,color='red')#bar chart
plt.title('Bar Chart')#plt.title('Cubes vs Squares')# label your visual
plt.xlabel("Day")#plt.xlabel('X-axis')
plt.ylabel("Sales")#plt.ylabel('Y-axis')
'''


plt.pie(sales, labels=days)
plt.title("Pie Chart")

# there are other ways you can visualize data as well as customize them, you can look up some different ways to do so


#plt.legend()# extra guiding information, try removing it and see the difference

plt.show()# this will attempt to display the data you pass to it