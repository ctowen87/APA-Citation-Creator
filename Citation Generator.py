import sqlite3
import time
import datetime
import random

                                                #Logo
def logo():
    print('############################################################################################')
    print(' ██████╗ ██████╗      ██████╗██████╗ ███████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗███████╗')
    print('██╔════╝██╔═══██╗    ██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝')
    print('██║     ██║   ██║    ██║     ██████╔╝█████╗  ███████║   ██║   ██║██║   ██║██╔██╗ ██║███████╗')
    print('██║     ██║   ██║    ██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║╚════██║')
    print('╚██████╗╚██████╔╝    ╚██████╗██║  ██║███████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║███████║')
    print(' ╚═════╝ ╚═════╝      ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝')
    print('############################################################################################')
    print('                                               Adjust Screen to Fit                           ')

#----------------------------------------------------------------------------------------------------------
                                                #Blank Line
def blank_line():
    print('                                                                                              ')    

#----------------------------------------------------------------------------------------------------------
                                                #APA Style


def apa_journal_citation():
    print('How Many Authors?')
    author_number = int(input('Number: '))
    authors = []
    for _ in range(author_number):
        last_name = input('Last Name: ')
        first_initial = input('First Initial: ')
        authors.append(last_name + ", " + first_initial)
    year = input('Year: ')
    title = input('Title: ')
    journal = input('Journal: ')
    volume = input('Volume #: ')
    url = input('URL: ')
    citation = (", ".join(authors) + "(" + year + ")." + title + ". " + journal + ", " + volume + ". Retrieved from " + url)
    keywords = input('Keywords: ')
    abstract = input('Paste Abstract: ')
    blank_line()
    blank_line()
    print(citation)
    blank_line()
    blank_line()

    conn = sqlite3.connect('Articles.db')
    c = conn.cursor()

    def data_entry():
        c.execute("INSERT INTO Journals VALUES(Title, Year, Journal, Keywords, URL, Citation)")
        
        conn.commit()
        c.close()
        conn.close()

    def dynamic_data_entry():

        c.execute("INSERT INTO Journals(title,year,journal,keywords,url,citation, abstract) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (title,year,journal,keywords,url,citation,abstract))

        conn.commit()

    for i in range(1):
        dynamic_data_entry()

    c.close
    conn.close()
#----------------------------------------------------------------------------------------------------------
                                            #Program Start
logo()
blank_line()
blank_line()
print('APA Citation Creator')
print('Created By: Christopher Owen')
print('Citation Structure Source: https://owl.purdue.edu')
print('Copyright: 2019')
blank_line()
blank_line()
while True:
    apa_journal_citation()
    another_citation = input('Another Citation? Y/N: ')
    if another_citation == 'Yes':
        continue
    if another_citation == 'yes':
        continue
    if another_citation == 'Y':
        continue
    if another_citation == 'y':
        continue
    if another_citation == 'No':
        break
    if another_citation == 'no':
        break
    if another_citation == 'N':
        break
    if another_citation == 'n':
        break
