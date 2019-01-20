# Imports
from typing import List
import sqlite3

# ----------------------------------------------------------------------------------------------------------------------
# -Global Variable Sets

#   -Developer Info
program_title = 'APA Citation Generator'
copyright_year = '2019'
creator = 'Christopher Owen'
company = 'CO Creations'
citation_source = 'https://owl.purdue.edu'


# ----------------------------------------------------------------------------------------------------------------------
# Blank Line

def blank_line():
    print('                                                                                                           ')


# ----------------------------------------------------------------------------------------------------------------------
# APA Style

# Journal
def apa_journal_citation():
    year = ''
    title = ''
    journal = ''
    volume = ''
    url = ''
    keywords = ''
    abstract = ''
    print('Enter Author Data')
    blank_line()
    author_number = int(input('Number of Authors: '))
    authors: List[str] = []
    for _ in range(author_number):
        blank_line()
        last_name = input('Last Name: ')
        first_initial = input('First Initial: ')
        authors.append(last_name + ", " + first_initial + '.')
    blank_line()
    while year == '':
        year = input('Year: ')
    while title == '':
        title = input('Title: ')
    while journal == '':
        journal = input('Journal: ')
    while volume == '':
        volume = input('Volume #: ')
    while url == '':
        url = input('URL: ')
    blank_line()
    citation = (", ".join(authors) + "(" + year + "). " + title + ". " + journal + ", " + volume +
                ". Retrieved from " + url)
    while keywords == '':
        keywords = input('Keywords: ')
    abstract_yes_no = input('Add Abstract? Yes/No: ')
    if abstract_yes_no != 'No':
        while abstract == '':
            objective = ''
            method = ''
            results = ''
            conclusion = ''
            print('Abstract Insert')
            blank_line()
            while objective == '':
                objective = input('Inset Objective: ')
            while method == '':
                method = input('Inset Method: ')
            while results == '':
                results = input('Inset Results: ')
            while conclusion == '':
                conclusion = input('Inset Conclusions: ')
            abstract = (objective + method + results + conclusion)

    blank_line()
    blank_line()
    print(citation)
    blank_line()
    blank_line()

    conn = sqlite3.connect('Articles.db')
    c = conn.cursor()

    def dynamic_data_entry():

        c.execute('INSERT INTO Journals(title,year,journal,keywords,url,citation,abstract,objective,'
                  'method,results,conclusion) '
                  'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                  (title, year, journal, keywords, url, citation, abstract, objective, method, results, conclusion))
        conn.commit()

    for i in range(1):
        dynamic_data_entry()

    c.close()
    conn.close()


# ----------------------------------------------------------------------------------------------------------------------
# Program Start

blank_line()
blank_line()
print(program_title)  # Program Title Statment
print('Created By: ' + creator)  # Program Created By Statement
print('Citation Structure Source: ' + citation_source)  # Source For Citation Structure
print('Copyright: ' + copyright_year + " " + company)  # Copyright Info
blank_line()
blank_line()

# Enter Another Citation? Prompt.
while True:
    apa_journal_citation()
    another_citation = input('Another Citation? Y/N: ')
    if another_citation == 'Yes':
        blank_line()
        blank_line()
        continue
    if another_citation == 'yes':
        blank_line()
        blank_line()
        continue
    if another_citation == 'Y':
        blank_line()
        blank_line()
        continue
    if another_citation == 'y':
        blank_line()
        blank_line()
        continue
    if another_citation == 'No':
        blank_line()
        blank_line()
        break
    if another_citation == 'no':
        blank_line()
        blank_line()
        break
    if another_citation == 'N':
        blank_line()
        blank_line()
        break
    if another_citation == 'n':
        blank_line()
        blank_line()
        break
