"""Quick script to build and manage the database"""

import csv
import sqlite3
from os import getcwd

# 3 source files for different scoring parameters
o_csv = getcwd() + "/data/offense.csv"
d_csv = getcwd() + "/data/defense_revised.csv"
k_csv = getcwd() + "/data/kickers.csv"

matchup = {o_csv: "Offense", d_csv: "Defense", k_csv: "Kickers"}

# list of sql commands to use
offense_table_construction_query = '''CREATE TABLE Offense
(Season YEAR, Position TEXT, FirstName TEXT, LastName TEXT, Team TEXT, Opp TEXT, Passing_Yds INT, Passing_TD INT, Passing_Int INT, Rushing_Yds INT, Rushing_TD INT, Receiving_Yds INT, Receiving_TD INT, Misc_FumTD INT, Misc_2PT INT, Fum_Lost INT, Fantasy_Points FLOAT(8, 4))'''
defense_table_construction_query = '''CREATE TABLE Defense
(Season YEAR, Position TEXT, TeamCity TEXT, TeamName TEXT, Opp TEXT, Tackles_Sack INT, Turnover_Int INT, Turnover_Fum_Rec INT, Score_Saf INT, Score_TD INT, Score_Def_2pt_Ret INT, Ret_TD INT, Points_Pts_Allow INT, Fantasy_Points FLOAT(8, 4))'''
kickers_table_construction_query = '''CREATE TABLE Kickers
(Season YEAR,Position TEXT, FirstName TEXT, LastName TEXT, Team TEXT, Opp TEXT, PAT_Made INT, FG_Made_0to19 INT, FG_Made_20to29 INT, FG_Made_30to39 INT, FG_Made_40to49 INT, FG_Made_50plus INT, Fantasy_Points FLOAT(8, 4))'''


def readfile(path):
    # just checking file format
    with open(path, newline='') as doc:
        data = csv.reader(doc, quotechar='|')
        print(data.__next__())
        print(data.__next__())
        print("Iteration beginning. Does it start again from the top?\n\n")
        for row in data:
            print(row)


def create_table(query):
    # make sure to pass in correct query from top of page to get headers
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()

def add_data(filepath):
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    with open(filepath, newline='') as csv_file:
        data = csv.reader(csv_file, delimiter=',', quotechar='|')
        header = data.__next__()
        for row in data:
            if matchup[filepath] == "Offense":
                c.execute("INSERT INTO Offense VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row)
            elif matchup[filepath] == "Defense":
                #print(row)
                c.execute("INSERT INTO Defense VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", row)
            elif matchup[filepath] == "Kickers":
                c.execute("INSERT INTO Kickers VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", row)
            else:
                print("Problem matching values")

    # Save (commit) the changes
    conn.commit()
    conn.close()


def read_db(filepath):
    conn = sqlite3.connect('football.db')
    c = conn.cursor()
    for row in c.execute('SELECT * FROM ' + matchup[filepath]):
        print(row)
    conn.close()




if __name__ == '__main__':
    #readfile(d_csv)
    create_table(defense_table_construction_query)
    add_data(d_csv)
    read_db(d_csv)
