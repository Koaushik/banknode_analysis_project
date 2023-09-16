#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# user_nodes.py

import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# Function to read the CSV file into a DataFrame
def read_csv():
    # Read the user_nodes.csv file using the pandas library and return it
    df = pd.read_csv('user_nodes.csv')
    return df

# Function to check for null (missing) values in the DataFrame
def check_null_values():
    # Do not edit the predefined function name
    df = read_csv()
    # Check for null values using the isnull() method and sum them for each column
    null_values = df.isnull().sum()
    return null_values

# Function to check for duplicate rows in the DataFrame
def check_duplicates():
    # Do not edit the predefined function name
    df = read_csv()
    # Calculate the number of duplicate rows using the duplicated() method and sum them
    duplicates = df.duplicated().sum()
    return duplicates

# Function to drop duplicate rows from the DataFrame
def drop_duplicates():
    # Do not edit the predefined function name
    df = read_csv()
    # Drop duplicate rows using the drop_duplicates() method with inplace=True
    df.drop_duplicates(inplace=True)
    return df

def data_cleaning():
    """
    Data Cleaning Function:
    Cleans the DataFrame by dropping specified columns and renaming others.

    Returns:
    DataFrame: The cleaned DataFrame after dropping and renaming columns.
    """
    # Step 1: Get the DataFrame with duplicate rows removed and rows with null values dropped
    df = drop_duplicates()

    # Step 2: Columns to remove from the DataFrame
    # Columns that need to be removed: "has_loan" and "is_act" 
    # Drop specified columns from the DataFrame
    df.drop(['has_loan', 'is_act'], axis=1, inplace=True)

    # Step 3: Rename columns using the new column names
    # Rename columns id_, area_id_, node_id_, act_date, deact_date to consumer_id, region_id, node_id, start_date, end_date
    df.rename(columns={'id_': 'consumer_id', 'area_id_': 'region_id', 
                       'node_id_': 'node_id', 'act_date': 'start_date','deact_date' : 'end_date'}, inplace=True)

    # Step 4: Save to a new file name
    df.to_csv('user_nodes_cleaned.csv', index=False)
    
    return df

# user_transaction.py

import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# Function to read the CSV file into a DataFrame
def read_csv():
    # Read the user_transactions.csv file using the pandas library and return it
    df = pd.read_csv('user_transactions.csv')
    return df

# Function to check for null (missing) values in the DataFrame
def check_null_values():
    # Do not edit the predefined function name
    df = read_csv()
    # Check for null values using the isnull() method and sum them for each column
    null_values = df.isnull().sum()
    return null_values

# Function to check for duplicate rows in the DataFrame
def check_duplicates():
    # Do not edit the predefined function name
    df = read_csv()
    # Calculate the number of duplicate rows using the duplicated() method and sum them
    duplicates = df.duplicated().sum()
    return duplicates

# Function to drop duplicate rows from the DataFrame
def drop_duplicates():
    # Do not edit the predefined function name
    df = read_csv()
    # Drop duplicate rows using the drop_duplicates() method with inplace=True
    df.drop_duplicates(inplace=True)
    return df

def data_cleaning():
    """
    Data Cleaning Function:
    Cleans the DataFrame by dropping specified columns and renaming others.

    Returns:
    DataFrame: The cleaned DataFrame after dropping and renaming columns.
    """
    # Step 1: Get the DataFrame with duplicate rows removed and rows with null values dropped
    df = drop_duplicates()

    # Step 2: Columns to remove from the DataFrame
    # Columns that need to be removed: "has_credit_card" and "account_type"
    df.drop(['has_credit_card', 'account_type'], axis=1, inplace=True)

    # Step 3: Rename columns using the new column names
    # Rename columns id_, t_date, t_type, t_amt to consumer_id, transaction_date, transaction_type, transaction_amount
    df.rename(columns={'id_': 'consumer_id', 't_date': 'transaction_date', 
                       't_type': 'transaction_type', 't_amt': 'transaction_amount'}, inplace=True)

    # Step 4: Save to a new file name
    df.to_csv('user_transaction_cleaned.csv', index=False)
    
    return df

