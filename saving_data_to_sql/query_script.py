from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from saving_company_data import Base, Company  # Import your ORM base and Company model

# Replace 'your_script_filename' with the actual name of the Python file where the Base and Company are defined

# Create an SQLAlchemy engine (replace the SQLite URL with your actual SQL server URL)
engine = create_engine('sqlite:///company_data.db')

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Query the database to retrieve all companies
def view_all_companies():
    try:
        companies = session.query(Company).all()
        for company in companies:
            print(f"ID: {company.id}, Name: {company.name}, Founding Year: {company.founding_year}, Description: {company.description}")
    except Exception as e:
        print(f"An error occurred while querying the database: {e}")
    finally:
        session.close()

# Example usage
if __name__ == "__main__":
    view_all_companies()
