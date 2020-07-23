# Lab: 17 - Web Scraping

## Authors:

_**Leo Kukharau**_

## Feature Tasks and Requirements

- Scrape a Wikipedia page and record which passages need citations.
  - E.g. History of Mexico has 7 “citation needed” cases, as of this writing.
- Your web scraper should report the number of citations needed.
- Your web scraper should identify those cases AND include the relevant passage.
  - E.g. Citation needed for “lorem spam and impsum eggs”
  - Consider the “relevant passage” to be the parent element that contains the passage, often a paragraph element.

## Dependencies

- python = "^3.8"
- bs4 = "^0.0.1"
- requests = "^2.24.0"

### Dev dependencies

- pytest = "^5.2"
- autopep8 = "^1.5.3"
- pylint = "^2.5.3"

[Link to code](./web_scraper/scraper.py)

[Link to PR]()
