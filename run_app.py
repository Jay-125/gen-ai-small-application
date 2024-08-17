from upload_csv_file.csv_input_tkinter import *
import requests
from saving_data_to_sql.saving_company_data import *
import traceback

class Main:

    def __init__(self):
        self.db = Company()

    def extract_company_desc_from_data(self, row):
        company_description = row['Description']
        return company_description

    def send_description_to_api(self, description):
        if description:
            url = "http://127.0.0.1:8000/api/check_description"  # Update this URL as needed
            try:
                response = requests.post(url, json={"description": description})
                if response.status_code != 200:
                    return None
                return response.json()
            except Exception as e:
                print("Error", f"An error occurred while sending the description to the API.\nError: {e}")
        return None

    def saving_data_to_sql(self, row, check_tech_company):
        company_name = row['Company name']
        company_description = row['Description']
        founding_year = row['Founding year']
        tech_company_or_not = check_tech_company['Technology based']
        self.db.save_company_to_sql(company_name, founding_year, company_description, tech_company_or_not)

    def add_or_update_column(self, df, column_name, value, row_index):
        df.at[row_index, column_name] = value
        return df


if __name__=="__main__":
    app = CSVParserApp()
    data = app.run()  # This will run the UI and return the data once it's done
    main = Main()
    try:
        for index, row in data.iterrows():
            company_description = main.extract_company_desc_from_data(row)
            print("Extracted company data from csv file.")
            send_desc_to_llm = main.send_description_to_api(company_description)
            if send_desc_to_llm != None:
                print("successfully analysed the company description through llm.")
                print("saving data to db.")
                save_data_to_db = main.saving_data_to_sql(row, send_desc_to_llm)
                # adding new column to csv file
                print("adding new column in csv file.")
                data = main.add_or_update_column(data, 'Technology based', send_desc_to_llm['Technology based'], index)
                output_csv_file = 'company_data.csv'
                data.to_csv(output_csv_file, index=False)
                print("Successfully added new column to csv file")
            else:
                raise Exception("Error in analyzing the company description through LLM.")
            break
    except Exception as e:
        print("Error Occured! Getting following error")
        traceback.print_exc()

