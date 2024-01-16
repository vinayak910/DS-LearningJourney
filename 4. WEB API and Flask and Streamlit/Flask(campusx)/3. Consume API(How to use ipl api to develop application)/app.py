from flask import Flask,render_template,request
import requests
app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('http://127.0.0.1:5000/api/teams')

    #print(response)# --> will tell status code
    #print(response.json())
    teams = response.json()['teams']

    return render_template('index.html' , teams = sorted(teams))

@app.route('/teamvteam')
def team_vs_team():
    response1 = requests.get('http://127.0.0.1:5000/api/teams')

    # print(response)# --> will tell status code
    # print(response.json())
    teams = response1.json()['teams']
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    response = requests.get('http://127.0.0.1:5000/api/teamvsteam?team1={}&team2={}'.format(team1 , team2))
    response = response.json()
    return render_template('index.html',result = response, teams = sorted(teams))

app.run(debug=True , port = 8000)