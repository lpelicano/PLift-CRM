# import numpy as np
#import matplotlib.pyplot as plt
# import mpld3

# def plot():

# 		fig, axes = plt.subplots(figsize=(6,4))
# 		models = [i.name for i in connect.session.query(Models).all()]
# 		quantity = [i.current_quantity for i in connect.session.query(Models).all()]
# 		x = np.arange(len(models))

# 		axes.bar(x,quantity, align='center', alpha=0.5, color='lightblue')
# 		plt.xticks(x,models)
# 		plt.ylabel('Stock')
# 		plt.title('Inventory')
# 		axes.margins(0.05)
# 		axes.set_ylim(bottom=0)
# 		fig.set_size_inches(3,4,forward=True)
# 		#plt.draw()

class Main(): 

	def plotgraph(): 
		import numpy as np
		import matplotlib.pyplot as plt,mpld3

		S2B = np.linspace(0.9,3.0,0.1)

		fig , ax = plt.subplots()

		BP = np.array([16,20,20,22,22,24,26,26,28,28])
		SQT = np.array([8,8,10,10,12,12,12,14,14,14,16,16,16,18,18,18,20,20,20])
		DL = np.array([6,6,6,6,8,8,8,10,10,10,10,12,12,12,14,14,14,16,16,18,18,18,20,20,20])

		line_BP = ax.plot(np.arange(len(BP)),BP)
		line_SQT = ax.plot(np.arange(len(SQT)),SQT)
		line_DL = ax.plot(np.arange(len(DL)),DL)


		plt.title('Correlation between correct fatigue and strength level')
		plt.xlabel('Strength/BodyWeight')
		plt.ylabel('Total Fatigue % per week')
		plt.grid(True)

		return plt,fig, ax

if __name__ == '__main__':
	Main()

