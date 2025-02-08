## Web Scraping all the colleges in gujarat from IndianStudyChannel website
## Libraries used
- scrapy
- ipython
- virtualenv
## Project Structure
```bash
univscraper/
│── venv/
│── univscraper/               # Project module
│   ├── spiders/                # Spider definitions
│   │   ├── __init__.py
│   │   ├── univspider.py        # Custom spider
│   ├── __init__.py
│   ├── items.py                # Define scraped data structure
│   ├── middlewares.py          # Custom middlewares
│   ├── pipelines.py            # Data processing pipelines
│   ├── settings.py             # Scrapy settings
│── scrapy.cfg                  # Scrapy configuration file
│── requirements.txt            # Dependencies
│── README.md                   # Project documentation
```
## Commands used
```bash
## to create virtual env
python -m venv venv
python venv\Scripts\activate
## to create project
scrapy startproject univscraper
## go the spider folder
scrapy genspider univspider '##paste webpage url'
## to activate scrapy shell
scrapy shell
```
- Successfully able to scrape all the university in gujarat
