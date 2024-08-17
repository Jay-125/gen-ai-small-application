from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the SQLAlchemy ORM base
Base = declarative_base()

# Define the Company table structure
class Company(Base):
    __tablename__ = 'companies'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    founding_year = Column(Integer, nullable=True)
    description = Column(Text, nullable=True)
    technology_company = Column(Text, nullable=True)

    # Function to save the company data to the SQL database
    def save_company_to_sql(self, company_name, founding_year, company_description, tech_company_or_not, db_url='sqlite:///company_data.db'):
        # Create an SQLAlchemy engine (replace the SQLite URL with your actual SQL server URL)
        engine = create_engine(db_url)
        
        # Create the companies table if it doesn't exist
        Base.metadata.create_all(engine)
        
        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()
        
        try:
            # Create a new company record
            company = Company(
                name=company_name,
                founding_year=founding_year,
                description=company_description,
                technology_company=tech_company_or_not
            )
            
            # Add the record to the session and commit the transaction
            session.add(company)
            session.commit()
            print(f"Company '{company.name}' saved successfully.")
        
        except Exception as e:
            session.rollback()  # Rollback the transaction in case of error
            print(f"An error occurred: {e}")
        
        finally:
            # Close the session
            session.close()
