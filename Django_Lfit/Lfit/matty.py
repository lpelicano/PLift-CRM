import numpy as np
import matplotlib.pylot as plt 

def plot():

		fig, axes = plt.subplots(figsize=(6,4))
		models = [i.name for i in connect.session.query(Models).all()]
		quantity = [i.current_quantity for i in connect.session.query(Models).all()]
		x = np.arange(len(models))

		axes.bar(x,quantity, align='center', alpha=0.5, color='lightblue')
		plt.xticks(x,models)
		plt.ylabel('Stock')
		plt.title('Inventory')
		axes.margins(0.05)
		axes.set_ylim(bottom=0)
		fig.set_size_inches(3,4,forward=True)
		#plt.draw()