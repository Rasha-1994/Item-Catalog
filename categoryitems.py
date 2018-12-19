from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///itemcatalog.db?check_same_thread=False')

# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
user1 = User(name="Robo Barista", email="tinnyTim@udacity.com")

session.add(user1)
session.commit()

# Items for Saudi Arabia
category1 = Category(name="Saudi Arabia", user_id=1)

session.add(category1)
session.commit()
item1 = CategoryItem(name="Riyadh", user_id=1, description='''Capital of the Kingdom of Saudi Arabia, Riyadh city is the seat of
government; ministries, embassies, diplomatic missions, as well as It contains
educational, financial, agricultural, cultural, technical, commercial and
social organizations.''', category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Jeddah", user_id=1,  description='''Jeddah is the second largest city after Riyadh, it is the main port of
the Kingdom on the Red Sea and main gate through which most of the pilgrims
arrive by air and sea to perform Umrah, Haj or to visit the two holy mosques.
Area inhabited is more than 1,500 km, and population is more than one and
half million.''', category=category1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Makkah", user_id=1, description='''Mecca, also called Makkah, is a city in Saudi Arabia. It is the holiest city
in Islam and is considered to be very sacred to Muslims. Muslims believe
that it is very important to visit Mecca at least once in their
lives.''', category=category1)

session.add(item3)
session.commit()

# Items for United Arab Emirates
category2 = Category(name="United Arab Emirates", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(name="Abu Dhabi", user_id=1, description='''Abu Dhabi, the capital of the United Arab Emirates has now emerged as one of
the country's finest tourist destinations because of its excellent
infrastructure, growing economy and interesting attractions. Also it's
a lot easier to get a visit visa to Abu Dhabi.''', category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Dubai", user_id=1,  description='''The Emirate of Dubai is the second largest of the seven United Arab Emirates
but has the biggest population at over 2.1 million inhabitants.
Size has been synonymous with Dubai as it continues to build the
first, largest and the biggest constructions in the
world.''', category=category2)

session.add(item2)
session.commit()


# Items for United Kingdom
category3 = Category(name="United Kingdom", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(name="London", user_id=1, description='''London, city, capital of the
United Kingdom. ''', category=category3)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Manchester", user_id=1, description='''Manchester, city and metropolitan borough in
the metropolitan county of Greater Manchester urban county,
northwestern England. Most of the city, including the historic
core, is in the historic county of Lancashire, but it includes
an area south of the River Mersey in the historic county of
Cheshire.''', category=category3)

session.add(item2)
session.commit()


# Items for United States of America
category4 = Category(name="United States of America", user_id=1)

session.add(category4)
session.commit()

item1 = CategoryItem(name="New York", user_id=1, description='''New York City was the first capital of the
United States after the Constitution was ratified in 1788.
On April 30, 1789, George Washington was inaugurated as the
nation first president at Federal Hall, located on Wall
Street.''', category=category4)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Washington", user_id=1, description='''Washington, constituent state of the United
States of America. Lying at the northwestern corner of
the 48 conterminous states, it is bounded by the Canadian
province of British Columbia to the north, the U.S.
states of Idaho to the east and Oregon to the south, and
the Pacific Ocean to the west.''', category=category4)

session.add(item2)
session.commit()

# Items for Turkey
category5 = Category(name="Turkey", user_id=1)

session.add(category5)
session.commit()

print ("added catalog Items")
