# APA-Citation-Creator
Python Script Text Input APA Citation Creator with output to SQLite Database

This script, when executed, will ask for input from the user. Information currently requested includes:
- Author Last Name
- Author First Name
- Year Published
- Title
- Publishing Journal
- Volume #
- Keywords
- Abstract
Once provided the script will then display the APA Citation for the respected work before asking if you want to 
continue to another citation.

In addition to creating the citation the script also connects to a SQLite database stored in the same file and inserts all of the entered information into a table for archival purposes.
