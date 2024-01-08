from flask import Flask,jsonify,request
import ipl0
import ipl
import json
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/api/teams')   #-->1st api
def teams():
    teams = ipl.teamsAPI()
    return jsonify(teams)
@app.route('/api/teamvsteam')
def teamvsteam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    result = ipl.team_vs_teamAPI(team1 , team2)
    return jsonify(result)
@app.route('/api/team-record')
def team_record():
    team = request.args.get('team')
    result = ipl0.teamAPI(team)
    return result

@app.route('/api/batting-record')
def batsman_record():
    batsman = request.args.get('batsman')
    result = ipl0.batsmanAPI(batsman)
    return result

@app.route('/api/bowling-record')
def batsman_record():
    bowler = request.args.get('bowler')
    result = ipl0.batsmanAPI(bowler)
    return result

app.run(debug=True)