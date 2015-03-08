from django.db import models
import datetime

class Article(models.Model):
	title = models.CharField(max_length = 200, default = "")
	author = models.CharField(max_length = 200, default = "")
	pub_date = models.DateField()
	MAJOR_CHOICES = (
		("ANT", "Anthropology"),
		("ARC", "Architecture School"),
		("ART", "Art and Archaeology"),
		("AST", "Astrophysical Sciences"),
		("CBE", "Chemical and Biological Engineering"),
		("CHM", "Chemistry"),
		("CEE", "Civil and Environmental Engineering"),
		("CLA", "Classics"),
		("COM", "Comparative Literature"),
		("COS", "Computer Science"),
		("CWR", "Creative Writing Program"),
		("EAS", "East Asian Studies"),
		("EEB", "Ecology and Evolutionary Biology"),
		("ECO", "Economics"),
		("ELE", "Electrical Engineering"),
		("ENG", "English"),
		("FRE", "French"),
		("ITA", "Italian"),
		("GEO", "Geosciences"),
		("GER", "German"),
		("HIS", "History"),
		("IND", "Independent Concentration"),
		("MAT", "Mathematics"),
		("MAE", "Mechanical and Aerospace Engineering"),
		("MOL", "Molecular Biology"),
		("MUS", "Music"),
		("NES", "Near Eastern Studies"),
		("ORF", "Operations Research and Financial Engineering"),
		("PHI", "Philosophy"),
		("PHY", "Physics"),
		("POL", "Politics"),
		("PSY", "Psychology"),
		("REL", "Religion"),
		("SLA", "Slavic Languages and Literature"),
		("SOC", "Sociology"),
		("SPA", "Spanish"),
		("POR", "Portugese"),
		("THR", "Theater"),
		("WWS", "Woodrow Wilson School"),
		("N/A", "None")
	)
	department = models.CharField(max_length = 3, choices = MAJOR_CHOICES, default="N/A")
	abstract = models.TextField(default="")
	article_link = models.URLField(default="")
	views = models.IntegerField(default=0)
	def __str__(self):
		return (self.title + '\n' + self.author + '\n' + str(self.pub_date) + '\n' + self.department)