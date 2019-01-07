from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DB import Theater, Base, MovieName, User

# connect with DB

engine = create_engine('sqlite:///theatreDB.db?check_same_thread=False')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create User
user1 = User(name="admin", email="topics.of.computer@gmail.com")
session.add(user1)
session.commit()
# create random theater number 1
theater1 = Theater(name="Test Theater", user_id="1")
session.add(theater1)
session.commit()

# Create movie names for funny theater
movieName1 = MovieName(
    name="Free State of Jones",
    description="A disillusioned Confederate army deserter returns to "
                " Mississippi and leads a militia of fellow deserters "
                " and women in an uprising "
                "against the corrupt local Confederate government.",
    price="10",
    theater=theater1,
    user_id="1")
session.add(movieName1)
session.commit()

movieName2 = MovieName(
    name="First Man",
    description="A look at the life of the astronaut, "
                " Neil Armstrong, and the legendary space mission "
                "that led him to become "
                "the first man to walk on the Moon on July 20, 1969.",
    price="15",
    theater=theater1,
    user_id="1")
session.add(movieName2)
session.commit()

# create random theater number 2

# create random theater
theater1 = Theater(name="Test Theater number 2", user_id="2")
session.add(theater1)
session.commit()

# Create movie names for funny theater
movieName1 = MovieName(
    name="Our Patriots ",
    description="After the French defeat of summer 1940,"
                "Addi Ba, a young Senegalese rifleman escapes "
                "and hides in the Vosges. Aided by some villagers,"
                "he gets false documents that allow him to live openly.",
    price="10",
    theater=theater1,
    user_id="2")
session.add(movieName1)
session.commit()

movieName2 = MovieName(
    name="The Imitation Game",
    description="During World War II,"
                "  the English mathematical genius Alan Turing "
                "tries to crack the German Enigma code "
                "with help from fellow mathematicians.",
    price="7",
    theater=theater1,
    user_id="2")
session.add(movieName2)
session.commit()

print "test movie names is added!"
