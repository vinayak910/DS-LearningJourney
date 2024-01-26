**Automation with Selenium and Beautiful Soup for Smartphone Data Scraping**

*Objective: Automate the extraction of smartphone data from a dynamic website using Selenium, save the HTML content for later reference, and utilize Beautiful Soup for structured data extraction. The extracted information includes multiple columns such as mobile name, spec score, SIM, OS, and others, which can be used for data analysis and potential machine learning model development.*

**1. Selenium Automation:**

   a. **Setup:**
      - Employed Selenium for automated web interactions.
      - Developed a Python script using Selenium, specifying the WebDriver and required modules.

   b. **Dynamic Website Navigation:**
      - Navigated to a dynamic website containing smartphone data.
      - Utilized Selenium to interact with dynamic elements, such as scrolling or clicking on "Load more" buttons.

   c. **HTML Page Capture:**
      - Captured the resulting HTML page post dynamic interactions.
      - Saved the HTML content to a text file for later reference (`dynamic_page.html`).

   d. **Selenium Script:**
      - Refer to the provided Python script for the Selenium automation code.

**2. Beautiful Soup Data Scraping:**

   a. **Read HTML File:**
      - Utilized Beautiful Soup to parse the saved HTML file (`dynamic_page.html`).

   b. **Data Extraction:**
      - Extracted smartphone data, including mobile name, spec score, SIM, OS, and other relevant information, from the HTML content.

   c. **Beautiful Soup Script:**
      - Refer to the provided jupyter notebook for the Beautiful Soup data extraction code.

**3. Data Analysis and Machine Learning:**

   a. **Data Processing:**
      - Processed the extracted data for analysis.

   b. **Potential ML Application:**
      - Explored potential machine learning applications using the gathered smartphone data, such as predicting spec score based on features.


