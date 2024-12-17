from typing import List
from pandas import DataFrame
from pymongo import MongoClient
from certifi import where
from os import getenv
from dotenv import load_dotenv
from MonsterLab import Monster
import plotly.express as px




class Database:
    """
    A class for interacting with my MongoDB database(Bander).
    Overview:
    It provides the ability to seed/populate the database with a bunch-O random documents,
    resets it by deleting all documents,
    count documents,
    and retrieve documents as a Pandas DataFrame or an HTML table.
    """
    load_dotenv()  # Load environment variables from .env file
    db = MongoClient(getenv("db_url"), tlsCAFile=where())['Database']

    def __init__(self, collection: str):
        """
        Initializes the database connection and selects the specified collection.

        Bander: Name of the MongoDB collection to interact with.
        """

        self.collection = self.db[collection]

    def seed(self, amount=1008):
        """
        Adds a specific number of random monster documents into the collection.

        amount: Number of documents to seed/insert.
        Remember, the amount is random, so we need to import the random library
        """

        monsters = [Monster().to_dict() for _ in range(amount)]
        return {'seed successful': f'{self.collection.insert_many(monsters).acknowledged}'}

    def reset(self):
        """
        Deletes all documents from the dict/collection.
        """

        return {'collection reset successful':f'{self.collection.delete_many(filter={}).acknowledged}'}

    def count(self) -> int:
        """
        Get the number of documents in the collection.

        returns number of documents in the collection.
        """
        return self.collection.count_documents(filter={})

    def dataframe(self) -> DataFrame:
        """
        Retrieve all documents in the collection as a Pandas DataFrame.

        returns a dataFrame containing all the documents.
        """
        documents = self.collection.find({}, {"_id": False})  # '_id' not needed from the MongoDB '_id' field
        return DataFrame(documents)

    def html_table(self) -> str:
        """
        Retrieve all documents as an HTML table.

        :returns the HTML table as a string, or None if the collection is empty.
        """
        df = self.dataframe()
        return df.to_html(index=False) if not df.empty else None

    def visualize_monsters(self):
        """
        Visualize the monster data using Plotly.
        """
        df_monstars = self.dataframe()  # Call the dataframe method
        if df_monstars.empty:
            print("No data available to visualize.")
            return
        # Make sure the columns used 'Type', 'Damage', and 'Type' exist in the DataFrame
        if 'Type' not in df_monstars.columns or 'Damage' not in df_monstars.columns:
            print("Required columns ('Type' and 'Damage') are missing in the data.")
            return

        # Create a bar chart using the correct column names
        fig = px.bar(df_monstars, x='Type', y='Damage', color='Type', title='Monster Damage by Type')
        fig.show()

    def export_dataset(self, filename='monsters.csv'):
        self.to_csv(filename, index=False)
        print(f'Dataset saved as {filename}')


if __name__ == "__main__": # constructor class

    Data_base = Database('Collection')
    action = input('Do you want to reset the database? (yes/no): ').strip().lower()
    if action == 'yes':
        print(Data_base.reset())
        seed_amount = int(input('How many documents would you like to add? * dont be greedy now! :)'))
        print(Data_base.seed(seed_amount))
    else:
        print('No action performed.')
    data_F = Data_base.dataframe()

    if not data_F.empty:
        # Call the visualize_monsters method of the Database instance
        Data_base.visualize_monsters()
    else:
        print('No data to visualize.')
