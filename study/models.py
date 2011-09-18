from django.db import models
import datetime

# Create your models here.
class User(models.Model):
	"""A user."""
	user = models.CharField(max_length=32)		# username
	email = models.EmailField()					# user's email
	name = models.CharField(max_length=64)		# user's real name
	PRIV = {("user","User"), 					# Content creator and consumer
		("admin","Administrator"),				# Content administrator: blocks, bans, suspends, warns, etc.
		("super","Super-admin")}				# Can appoint admins, plus admin powers
	auth = models.CharField(max_length=5,choices = PRIV) # user privilege level
	def __unicode__(self):
		return self.user

class Study(models.Model):
	"""A scientific study"""
	title = models.CharField(max_length=128) 	# Title
	date = models.DateTimeField()				# Date of study's creation
	def __unicode__(self):
		return self.title
	def age(self):
		return str(datetime.datetime.now() - self.date)
	
class Author(models.Model):
	"""Connects users with studies they've authored, and allows several users to author a study"""
	study = models.ForeignKey(Study)	# Study being authored
	user = models.ForeignKey(User)		# User authoring study
	def __unicode__(self):
		return self.user
	
class Section(models.Model):
	"""An individual section of the study, such as hypothesis, findings, conclusion, or bibliography."""
	study = models.ForeignKey(Study)
	date = models.DateTimeField()				# Date of section's creation
	title = models.CharField(max_length=32)		# Section title
	text = models.CharField(max_length=4096)	# Section text
	# things to think about: images, graphs, formulas, etc
	def __unicode__(self):
		return self.title
	
class Comment(models.Model):
	"""Comments talk about one section of a scientific study, rather than the whole thing. Comments are public."""
	section = models.ForeignKey(Section)		# Section being commented
	user = models.ForeignKey(User)				# Comment author
	date = models.DateTimeField()				# Comment post date/time
	text = models.CharField(max_length=1024)	# Comment text
	# Things to think about: refining what the comment refers to specifically
	
class Review(models.Model):
	"""Reviews comment on a whole study, rather than any one part. Additionally, only the author can see them."""
	study = models.ForeignKey(Study)			# Study being reviewed
	user = models.ForeignKey(User)				# Review author
	title = models.CharField(max_length=64)		# Review title
	date = models.DateTimeField()				# Review post date/time
	text = models.CharField(max_length=4096)	# Review text
	save = models.BooleanField()				# False if the review has been published, true if unpublished
	# use "save" to save reviews before publishing, since their longer form means
	# we should probably give users more time to craft them than may be available
	# in a single sitting.
	def __unicode__(self):
		return self.title
	
class Tag(models.Model):
	"""Tags to help organize studies by topic"""
	study = models.ForeignKey(Study)			# Study being tagged
	text = models.CharField(max_length=32)		# The tag itself
	# Think about upvote downvote tagging, so the community can generate tags
	def __unicode__(self):
		return self.text
	
class Citation(models.Model):
	"""When one study cites another"""
	study = models.ForeignKey(Study,related_name="Citer")	# Study citing the other
	cite = models.ForeignKey(Study,related_name="Cited")	# Study being cited
	def __unicode__(self):
		return str(self.study) + " cited " + str(self.cite)
	
class Vote(models.Model):
	"""A user's vote, 1-5, on studies"""
	study = models.ForeignKey(Study)					# Study being voted on
	user = models.ForeignKey(User)						# User casting vote
	VALUES = {(1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5")}	# Possible values for vote
	vote = models.IntegerField(choices = VALUES)		# Vote
	def __unicode__(self):
		return str(self.vote) + " by " + str(self.user) + " on " + str(self.study)
	
class ReportStudy(models.Model):
	"""Reports a study for abuse."""
	study = models.ForeignKey(Study)		# Study being reported
	user = models.ForeignKey(User)			# User reporting the study
	text = models.CharField(max_length=512)	# Text explaining reason for report
	
class ReportSection(models.Model):
	"""Reports a section for abuse."""
	section = models.ForeignKey(Section)	# Section being reported
	user = models.ForeignKey(User)			# User reporting the section
	text = models.CharField(max_length=512)	# Text explaining reason for report
	
class ReportReview(models.Model):
	"""Reports a review for abuse."""
	review = models.ForeignKey(Review)		# Review being reported
	user = models.ForeignKey(User)			# User reporting the review
	text = models.CharField(max_length=512)	# Text explaining reason for report
	
class ReportComment(models.Model):
	"""Reports a comment for abuse."""
	comment = models.ForeignKey(Comment)	# Comment being reported
	user = models.ForeignKey(User)			# User reporting the comment
	text = models.CharField(max_length=512)	# Text explaining reason for report
	# Consider upvote downvote system for comments instead
