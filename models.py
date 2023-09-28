from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Mentor(db.Model):
  __tablename__ = "mentors"
  fname = db.Column(db.String(255), nullable=False)
  lname = db.Column(db.String(255), nullable=False)
  username = db.Column(db.String(255), primary_key=True)
  password = db.Column(db.String(255), nullable=False)
  email = db.Column(db.String(255), nullable=False)
  profile_pic = db.Column(db.String(255), nullable=False, default="arabsoc.png")
  bio = db.Column(db.Text, nullable=False, default="Bio has not been edited by the user")
  job = db.Column(db.String(255), nullable=False)
  cv_help = db.Column(db.Boolean, nullable=False)
  meetStudents = db.Column(db.Boolean, nullable=False)
  mockInterview = db.Column(db.Boolean, nullable=False)
  workExp = db.Column(db.Boolean, nullable=False)


class Mentee(db.Model):
  __tablename__ = "mentees"
  fname = db.Column(db.String(255), nullable=False)
  lname = db.Column(db.String(255), nullable=False)
  prn_num = db.Column(db.String(255), nullable=False)
  username = db.Column(db.String(255), primary_key=True)
  password = db.Column(db.String(255), nullable=False)
  branch = db.Column(db.String(255), nullable=False)
  batch = db.Column(db.String(255), nullable=False)
  email = db.Column(db.String(255), nullable=False)
  linkedin_pro = db.Column(db.String(255), nullable=False)
  class_incharge = db.Column(db.String(255), nullable=False)
  aggregate_sgpa = db.Column(db.Float, nullable=False)
  achievements = db.Column(db.String(255), nullable=False)
  internships = db.Column(db.String(255), nullable=False)
  profile_pic = db.Column(db.String(255), nullable=False, default="arabsoc.png")
  bio = db.Column(db.Text, nullable=False, default="Bio has not been edited by the user")
  cv_help = db.Column(db.Boolean, nullable=False)
  meetAlumni = db.Column(db.Boolean, nullable=False)
  mockInterview = db.Column(db.Boolean, nullable=False)

class Resource(db.Model):
    __tablename__ = "resources"
    id = db.Column(db.Integer, primary_key=True) #this is the resource id
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    file = db.Column(db.String(255), nullable=False, default="c.pdf")
