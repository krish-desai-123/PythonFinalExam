""" Python Exam """
from unittest import case

""" Smart Expense Tracker Application"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt


global expenses,df
expenses = []
df = pd.read_csv("expenses.csv")


class ExpenseTracker:
    def __init__(self):
        self.df = df
        self.expenses = expenses
        

    def add_expense(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description
        self.expenses.append([date, amount, category, description])
        write_to_csv()
    def get_summary(self):
        print(f"Total Spent: {self.df['amount'].sum()}")
        print(f"Avg Spent: {self.df['amount'].mean()}")
        print(f"Description of Dataset: {self.df.describe()}")

    def filter_expenses(self, condition):
        pass
        # if condition in self.expenses["Category"]:
        #     print(f"Spent on {condition}: { self.expenses.groupby(condition)['amount'].sum()}")

    def generate_report(self):
        pass
    def graph(self):
        sns.barplot(x=self.df['Category'], y=self.df['amount'])
        plt.xlabel("Category")
        plt.xticks(rotation=90)
        plt.ylabel("Amount")
        plt.show()

        sns.lineplot(x=self.df["date"].dt.month, y=self.df['amount'])
        plt.xlabel("Month")
        plt.ylabel("Amount")
        plt.show()

        plt.pie(df['amount'], labels=self.df['Category'])
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.show()

        sns.histplot(df['amount'], bins=5)
        plt.xlabel("Amount")
        plt.xlabel("Amount")
        plt.show()

def write_to_csv():
    with open ('expenses.csv', "a+") as csvfile:
        for i in expenses:
            print(i)
            for j in i:
                csvfile.write(str(j))
                csvfile.write(",")
            csvfile.write("\n")




while True:
    obj = ExpenseTracker()
    print("""
Choose:
1. Add new expenses
2. Get_summary
3. Filter expenses
4. Generate report
5. Graph
6. Exit
""")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:

            print("Add new expenses")
            date = input("Enter date (yyyy-mm-dd): ")
            try:
                date = dt.datetime.strptime(date, "%Y-%m-%d").date()
                date = dt.datetime.strftime(date, "%Y-%m-%d")
            except ValueError:
                print("Please enter a valid date")
            except Exception as e:
                print("Please enter a valid date")
                print("\nError: ", e)
            else:
                try:
                    amount = float(input("Enter amount: "))
                    if amount > 0:
                        pass
                    else:
                        raise ValueError("Please enter a  positive amount")
                except ValueError:
                    print("Please enter a valid amount")
                except Exception as e:
                    print("Please enter a valid amount")
                    print("\nError: ", e)
                else:
                    try:
                        category = input("Enter category: ")
                    except Exception as e:
                        print("Please enter a valid category")
                        print("\nError: ", e)
                    else:
                        try:
                            description = input("Enter description: ")
                        except Exception as e:
                            print("Please enter a valid description")
                            print("\nError: ", e)
                        else:
                            obj.add_expense(date,amount,category, description)
        case 2 :
            obj.get_summary()
        case 3:
            pass
        case 4:
            pass
        case 5:
            obj.graph()
        case 6:
            print("Exit")
            break
        case _:
            print("Invalid Option")

# df = pd.read_csv("expenses.csv")
# df.isna().sum()
#
#
#
#






