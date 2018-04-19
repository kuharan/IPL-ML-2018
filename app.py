from flask import Flask ,render_template ,request ,redirect ,url_for
import unicodedata

app=Flask(__name__)

@app.route('/')
def first():
    return render_template('homepage.html')

@app.route('/second' ,methods = ['POST', 'GET'])
def second():

    if request.method=='POST' :

        #extracting cigratePerDay by using request.form and converting it into string because request.form returns unicode
        team_1= unicodedata.normalize('NFKD', request.form['team_1']).encode('ascii', 'ignore')
        team_2= unicodedata.normalize('NFKD', request.form['team_2']).encode('ascii', 'ignore')
        team_1_homeGround= unicodedata.normalize('NFKD', request.form['team_1_homeGround']).encode('ascii', 'ignore')
        team_1_toss= unicodedata.normalize('NFKD', request.form['team_1_toss']).encode('ascii', 'ignore')
        team_1_toss_decision= unicodedata.normalize('NFKD', request.form['team_1_toss_decision']).encode('ascii', 'ignore')

        #converting cigratePerDay it into int due to input format for logisticRegression
        # initial=[int(cigratePerDay),int(weight),int(height),int(waterIntakePerDay),int(exerciseInHoursperDay)]
        # final = []
        # #preparing input data like [[10,65,6,5,1]]
        # final.append(initial)

        #passing the prediction result to another page
        return redirect(url_for('success', name="results"))


@app.route('/success/<name>')
def success(name):
    return name

if __name__=='__main__':
    app.run()
