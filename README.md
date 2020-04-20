# Database-Toolbox
This is a project that utilises a pipeline for scraping websites and connecting/executing queries to a remote MySQL database:

~/scraping_scripts/ --> contains the individual scraping scripts for unique websites.
~/scraping_scripts/utils --> contains the database utility scripts:

~/html_bank --> storage for scraped HTML's.

~/test_schema --> stoage for the MySQL schema.

The whole pipeline is called from ~/scraping_scripts/executor.py and constitutes of:
      --> 1. Getting the raw HTML from the given list of urls and storing them in the HTML bank.
      --> 2. Calling a specific data extractor function on the stored HTML's.
      --> 3. Connecting to the remote MySQL database and executing the write query function to commit the extracted data to DB

*As this is a demo version, the configuration of the DB has been masked out, and needs to be specified in ~/scraping_scripts/utils/config.py. Furthermore, the path to chromedriver needs to be updated/specified in the ~/scraping_scripts/utils/raw_html_getter.py

Package requirements in: requirements.txt
