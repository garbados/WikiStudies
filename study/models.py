from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here
class Tag(models.Model):
	"""Tags to help organize studies by topic"""
	text = models.CharField(max_length=32)		# The tag itself
	# Think about upvote downvote tagging, so the community can generate tags
	def __unicode__(self):
		return self.text

class Study(models.Model):
	"""A scientific study"""
	title = models.CharField(max_length=128) 	# Title
	tags = models.ManyToManyField(Tag)			# Tag set
	authors = models.ManyToManyField(User)      # Author set
	date = models.DateTimeField()				# Date of study's creation
	def __unicode__(self):
		return self.title
	def age(self):
		return str(datetime.datetime.now() - self.date)
	
class Section(models.Model):
	"""An individual section of the study, such as hypothesis, findings, conclusion, or bibliography."""
	study = models.ForeignKey(Study)            # Study to which the section belongs
	date = models.DateTimeField()				# Date of section's creation
	citations = models.ManyToManyField(Study, related_name='citations')   # Citation set
	title = models.CharField(max_length=64)		# Section title
	text = models.TextField()					# Section text
	# things to think about: images, graphs, formulas, etc
	def __unicode__(self):
		return self.title
	
class Comment(models.Model):
	"""Comments talk about one section of a scientific study, rather than the whole thing. Comments are public."""
	section = models.ForeignKey(Section)		# Section being commented
	user = models.ForeignKey(User)				# Comment author
	date = models.DateTimeField()				# Comment post date/time
	text = models.TextField()					# Comment text
	# Things to think about: refining what the comment refers to specifically
	
class Review(models.Model):
	"""Reviews comment on a whole study, rather than any one part. Additionally, only the author can see them."""
	study = models.ForeignKey(Study)			# Study being reviewed
	user = models.ForeignKey(User)				# Review author
	title = models.CharField(max_length=64)		# Review title
	date = models.DateTimeField()				# Review post date/time
	text = models.TextField()					# Review text
	save = models.BooleanField()				# False if the review has been published, true if unpublished
	# use "save" to save reviews before publishing, since their longer form means
	# we should probably give users more time to craft them than may be available
	# in a single sitting.
	def __unicode__(self):
		return self.title
	
#class Ext_citation(models.Model):
#	"""When one study cites another from outside of wikistudies"""
#	study = models.ForeignKey(Study,related_name="Citer")	# Study citing the other
#	cite = models.ForeignKey(Study,related_name="Cited")	# Study being cited
#	def __unicode__(self):
#		return str(self.study) + " cited " + str(self.cite)
	
class Vote(models.Model):
	"""A user's vote, 1-5, on studies"""
	study = models.ForeignKey(Study)					# Study being voted on
	user = models.ForeignKey(User)						# User casting vote
	VALUES = {(1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5")}	# Possible values for vote
	vote = models.IntegerField(choices = VALUES)		# Vote
	def __unicode__(self):
		return str(self.vote) + " by " + str(self.user) + " on " + str(self.study)
