from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, CatalogItem, User

engine = create_engine('sqlite:///catalogandusers.db')
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
User1 = User(name="Makeda Stuff", email="jenn@madeUpSite.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Catalog for Soccer
category1 = Category(user_id=1, categoryname="Soccer")

session.add(category1)
session.commit()

catalogItem1 = CatalogItem(user_id=1, name="Shin Guards", description="Two shin guards for full coverage", category=category1)

session.add(catalogItem1)
session.commit()

catalogItem2 = CatalogItem(user_id=1, name="Jersey", description="choose your team colors for this short sleeve jersey", category=category1)

session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Cleats", description="Cleats with interchangable bottoms", category=category1)

session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="Soccer Ball", description="regulation full sized soccer ball", category=category1)

session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="Uniform Shorts", description="Shorts to match your jersey", category=category1)

session.add(catalogItem5)
session.commit()

catalogItem6 = CatalogItem(user_id=1, name="Break Away Warm-up Pants", description="pants to cover your shorts", category=category1)

session.add(catalogItem6)
session.commit()


# Catalog for Basketball
category2 = Category(user_id=1, categoryname="Basketball")

session.add(category2)
session.commit()


catalogItem7 = CatalogItem(user_id=1, name="Regulation Basketball", description="Full size regulation basketball for games", category=category2)

session.add(catalogItem7)
session.commit()

catalogItem8 = CatalogItem(user_id=1, name="Basketball Jersey",
                     description="Choose your team colors for this great jersey", category=category2)

session.add(catalogItem8)
session.commit()

catalogItem9 = CatalogItem(user_id=1, name="High Tops", description="Run super fast with these awesome high tops", category=category2)

session.add(catalogItem9)
session.commit()

catalogItem10 = CatalogItem(user_id=1, name="Basketball Shorts", description="Light weight breathable shorts to keep you comfy", category=category2)

session.add(catalogItem10)
session.commit()

catalogItem11 = CatalogItem(user_id=1, name="Warm Up Pants", description="Ride the bench in style with these great pants", category=category2)

session.add(catalogItem11)
session.commit()


# Catalog for Baseball
category3 = Category(user_id=1, categoryname="Baseball")

session.add(category3)
session.commit()


catalogItem13 = CatalogItem(user_id=1, name="Regulation Baseball", description="Regulation game ball", category=category3)

session.add(catalogItem13)
session.commit()

catalogItem14 = CatalogItem(user_id=1, name="Baseball Jersey", description="Nice pin stripe jersey", category=category3)

session.add(catalogItem14)
session.commit()

catalogItem15 = CatalogItem(user_id=1, name="Baseball Glove", description="choose left or right handed glove", category=category3)

session.add(catalogItem15)
session.commit()

catalogItem16 = CatalogItem(user_id=1, name="Batting Gloves", description="Keep your hands from stinging while smacking a line drive", category=category3)

session.add(catalogItem16)
session.commit()

catalogItem17 = CatalogItem(user_id=1, name="Bat", description="32 inch 24 oz double walled bat", category=category3)

session.add(catalogItem17)
session.commit()


# Catalog for Disc Golf
category4 = Category(user_id=1, categoryname="Disc Golf")

session.add(category4)
session.commit()


catalogItem18 = CatalogItem(user_id=1, name="Space Dyed Disc", description="Spot this bright colored disc in any terrain", category=category4)

session.add(catalogItem18)
session.commit()

catalogItem19 = CatalogItem(user_id=1, name="LED Accent Light", description="Keep playing through dusk with these LED lights", 		category=category4)

session.add(catalogItem19)
session.commit()

catalogItem20 = CatalogItem(user_id=1, name="Disc Carrying Bag",
                     description="keep your discs organized", category=category4)

session.add(catalogItem20)
session.commit()

catalogItem21 = CatalogItem(user_id=1, name="Disc Golf Target", description="Set up this portable target and practice anywhere",
                     category=category4)

session.add(catalogItem21)
session.commit()




# Catalog for Snowboarding
category5 = Category(user_id=1, categoryname="Snowboarding")

session.add(category5)
session.commit()


catalogItem22 = CatalogItem(user_id=1, name="Snowboard", description="Spiffy new snowboard. Please use only on snow.", category=category5)

session.add(catalogItem22)
session.commit()

catalogItem23 = CatalogItem(user_id=1, name="Giant Boots", description="Lock into your board with these huge inflexible boots",
                     category=category5)

session.add(catalogItem23)
session.commit()

catalogItem24 = CatalogItem(user_id=1, name="Gloves", description="Gloves to keep your hands warm",
                     category=category5)

session.add(catalogItem24)
session.commit()

catalogItem25 = CatalogItem(user_id=1, name="Goggles",
                     description="Goggles keep your eyes from freezing", category=category1)

session.add(catalogItem25)
session.commit()

catalogItem26 = CatalogItem(user_id=1, name="Snow Pants", description="Be honest these are really what you plan to go down the mountain on",
                     category=category1)

session.add(catalogItem26)
session.commit()


# Catalog for Rock Climbing
category6 = Category(user_id=1, categoryname="Rock Climbing")

session.add(category6)
session.commit()


catalogItem27 = CatalogItem(user_id=1, name="Rope", description="Tie yourself to a big rock",
                     category=category6)

session.add(catalogItem27)
session.commit()

catalogItem28 = CatalogItem(user_id=1, name="Foot Gear", description="Sticky shoes to climb rocks",
                     category=category6)

session.add(catalogItem28)
session.commit()

catalogItem29 = CatalogItem(user_id=1, name="Harness", description="Attach to a big rope",
                     category=category6)

session.add(catalogItem29)
session.commit()

catalogItem30 = CatalogItem(user_id=1, name="Clippy Thing", description="clippy thing to use on a rope",
                     category=category6)

session.add(catalogItem30)
session.commit()



# Catalog for Football
category7 = Category(user_id=1, categoryname="Football")

session.add(category7)
session.commit()

catalogItem31 = CatalogItem(user_id=1, name="Shoulder Pads",
                     description="turn your shoulders into battering rams", category=category7)

session.add(catalogItem31)
session.commit()


catalogItem32 = CatalogItem(user_id=1, name="Awesome Football", description="An unsettlingly huge football",
                     category=category7)

session.add(catalogItem32)
session.commit()

catalogItem33 = CatalogItem(user_id=1, name="football pants", description="lower case football pants",
                     category=category7)

session.add(catalogItem33)
session.commit()

catalogItem34 = CatalogItem(user_id=1, name="football shirt",
                     description="covers those super awesome shoulder pads you just bought", category=category7)

session.add(catalogItem34)
session.commit()

catalogItem35 = CatalogItem(user_id=1, name="under eye paint", description="paint for under your eyes. because football",
                     category=category7)

session.add(catalogItem35)
session.commit()



# Catalog for Skating
category8 = Category(user_id=1, categoryname="Skating")

session.add(category8)
session.commit()


catalogItem36 = CatalogItem(user_id=1, name="Skates",
                     description="Low top skates with fat pink wheels", category=category8)

session.add(catalogItem36)
session.commit()

catalogItem37 = CatalogItem(user_id=1, name="leg warmers", description="keep your ankles warm with these neon green leg warmers",
                     category=category8)

session.add(catalogItem37)
session.commit()


catalogItem38 = CatalogItem(user_id=1, name="hair spray", description="keep those bangs tall ladies",
                     category=category8)

session.add(catalogItem38)
session.commit

catalogItem39 = CatalogItem(user_id=1, name="pad lock",
                     description="bring your own lock for your locker", category=category1)

session.add(catalogItem39)
session.commit()




print "added all the things!"
