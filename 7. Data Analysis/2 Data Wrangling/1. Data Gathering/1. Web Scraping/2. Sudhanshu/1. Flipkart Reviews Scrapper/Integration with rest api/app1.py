from flask import Flask , render_template , request , jsonify
import requests
from bs4 import BeautifulSoup
import logging
import pandas as pd
app1 = Flask(__name__)
logging.basicConfig(filename = "scrapper.log",level = logging.INFO)

@app1.route("/" , methods = ['POST' , 'GET'])
def homepage():
    return render_template("index.html")

@app1.route("/review" , methods = ['POST'])
def scrape():
    if request.method == "POST":
        try:
            search = request.form['content'].replace(" ","")
            flipkart_url = "https://www.flipkart.com/search?q={}".format(search)
            webpage = requests.get(flipkart_url).text
            soup=BeautifulSoup(webpage,'lxml')
            prod_link = 'https://www.flipkart.com' + soup.find_all('div' , class_="_2kHMtA")[0].find('a' , class_="_1fQZEK")['href']
            subpage = requests.get(prod_link).text
            subsoup = BeautifulSoup(subpage , 'lxml')
            all_reviews = requests.get('https://www.flipkart.com' + subsoup.find_all('div',class_="col JOpGWq")[0].find('a')['href']).text
            reviews_html = BeautifulSoup(all_reviews , 'lxml')
            final_page = "https://www.flipkart.com" + reviews_html.find_all('div',class_="_33iqLu")[0].find_all('a')[0]['href']
            reviews = []
            for i in range(1 , 10):
                final_page = final_page + "&page={}".format(i)
                final_html= requests.get(final_page).text
                final = BeautifulSoup(final_html,'lxml')
                reviews_page = final.find_all('div',class_="col _2wzgFH K0kLPL")
                
                for div in reviews_page :
                    try:
                        buyer = div.find_all('p',class_="_2sc7ZR _2V5EHH")[0].text
                    except:
                        logging.info("name")
                    try:
                        ratings = (div.find_all('div',class_="_3LWZlK _1BLPMq")[0].text)

                    except:
                        logging.info("rating")


                    try:
                        desc = (div.find_all('div',class_="t-ZTKy")[0].text.split("READ MORE")[0])
                    except:
                        logging.info("Description")
                    try:
                        review_head = (div.find_all('p',class_="_2-N8zT")[0].text)
                    except:
                        logging.info("Review head")
        
                    d = {'Buyer':buyer,'Ratings':ratings,'Reviews':review_head,'Description':desc}
                    reviews.append(d)
                df = pd.DataFrame(reviews)
                df.to_csv(search + ".csv" , index = False)
            logging.info("The final result {}".format(d))
            return render_template('result.html', reviews=reviews[0:(len(reviews)-1)])
            
        except Exception as e:
            logging.info(e)
            return "Something Went Wrong"
    else:
        render_template('index.html')
if __name__=="__main__":
    app1.run(host="0.0.0.0")

        
                    



