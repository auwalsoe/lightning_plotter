import requests
from gmplot import gmplot
import numpy as np
class lightning_app ():
	def __init__(self):
		self.r = requests.get('https://api.met.no/weatherapi/lightning/1.0/')
		self.text = self.r.text
		self.text_tokenized = self.text.split()
		self.report_length = 25
		self.list_of_reports = None
		self.num_reports = len(self.text_tokenized)/self.report_length
		self.coordinate_pairs = []
		self.latitudes = []
		self.longitudes = []
	def text2vector(self):
		text_tokenized = self.text.split()
		self.list_of_reports =self.splitList()
	
	def splitList(self):
	    avg = len(self.text_tokenized) / float(self.num_reports)
	    out = []
	    last = 0.0

	    while last < len(self.text_tokenized):
	        out.append(self.text_tokenized[int(last):int(last + avg)])
	        last += avg

	    return out
	def extract_coordinates(self):
		for report in self.list_of_reports:
			self.coordinate_pairs.append((report[8], report[9]))
			self.latitudes.append(float(report[8]))
			self.longitudes.append(float(report[9]))
	def plot_coordinates_on_map(self, file_name = "my_map.html"):
		center_lat = np.average(self.latitudes)
		center_lng = np.average(self.longitudes)
		gmap = gmplot.GoogleMapPlotter(center_lat = center_lat, center_lng = center_lng, zoom = 5)
		gmap.scatter(self.latitudes, self.longitudes, '#3B0B39', size=10000, marker=False)
		gmap.draw(file_name)
	def printCoordinates(self):
		print(self.coordinate_pairs)
	def printAllReports(self):
		print(self.list_of_reports)
				

if __name__ =="__main__":
	test = lightning_app()
	test.text2vector()
	test.extract_coordinates()
	test.plot_coordinates_on_map(file_name = "test.html")


