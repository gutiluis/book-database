from models import (Base, session, 
                    Books, engine)




if __name__ == "__main__":
    Base.metadata.create_all(engine)