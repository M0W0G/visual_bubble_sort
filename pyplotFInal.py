import random as ran
from matplotlib import pyplot as plt
#this is key to allowing plots to update easily
from matplotlib import animation


#easy swapper function
def swap(A, x, y):
    save = A[x]
    A[x] = A[y]
    A[y] = save



def bubble_sort(data):
	swapped = True
	
	for x in range(len(data) - 1):
		if not swapped:
			return
		swapped = False
		
		for y in range(len(data) - 1 - x):
			if data[y] > data[y + 1]:
				swap(data, y, y + 1)
				swapped = True
			yield data

#defines the screen and runs updates
    
def visualize():
    #number of itterations
	it_num = 40
	data = list(range(1, it_num + 1))
	ran.shuffle(data)
	
	# uses yield to create consecutive "list" of graph states
	generator = bubble_sort(data)
	
	figure, axis = plt.subplots()
	axis.set_title("bubble sort")
	bar_sub = axis.bar(range(len(data)), data, align="center")
	
	# sets limit to how far x axis can go
	axis.set_xlim(0, it_num)
	text = axis.text(0.03, 0.96, "", transform=axis.transAxes)
	iteration = [0]
	
	def updateScreen(data, rects, iteration):
		for rect, value in zip(rects, data):
			rect.set_height(value)
		iteration[0] += 1
		text.set_text(f"# of steps: {iteration[0]}")

	# creating animation object for rendering the iteration
	slides = animation.FuncAnimation(
		figure,
		func=updateScreen,
		fargs=(bar_sub, iteration),
		frames=generator,
		repeat=True,
		blit=False,
        #speed of each step going through generator in MS
		interval=25,
        #how many screens (steps) it will save
		save_count=90000,
	)
	
	# must open it and then close it or it will open too many graphs and crash / lag
	plt.show()
	plt.close()


if True:
	visualize()


