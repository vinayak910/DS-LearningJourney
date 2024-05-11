# Flipkart Reviews Scraper

This project is a web scraper that extracts product reviews from Flipkart using Beautiful Soup. Additionally, it provides a user-friendly web interface using Flask, HTML, and CSS to view and interact with the scraped data.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/vinayak910/Flipkart-Reviews-Scrapper.git
   cd flipkart-reviews-scraper
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:

   ```bash
   python app1.py
   ```

   This will start the Flask development server.

2. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the web interface.

3. Enter the Flipkart product  Name.

4. The scraper will extract reviews from the provided URL and display them on the web page and even stored locally in the csv format.

## Project Structure

- `app.py`: The main Flask application.
- `templates/`: Contains HTML templates.
- `static/`: Contains CSS stylesheets.

## Libraries Used

- **Beautiful Soup:** Used for web scraping to extract data from HTML.
- **Flask:** Used to create the web application.
- **HTML and CSS:** Used for creating the user interface.

## Acknowledgments

Special thanks to the developers of Beautiful Soup and Flask for creating such powerful and user-friendly tools.

