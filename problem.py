import htmlCreator
from flask import Flask, render_template,request,jsonify
app = Flask(__name__)



class Problems:
    def __init__(self,id,title,catagory,level,details,count):
        self.id = id
        self.title = title
        self.category = catagory
        self.level = level
        self.details = details
        self.count = count

# transport = Problems(1, "Road issues","Transportation",  "level 3", "The roads are not properly maintained. Even though the maintainence work is done, its not that fast. Sanitary status is also not so good as well.The roads are not properly maintained.",1)
# transport1 = Problems(1, "Health issues","Health",  "level 1", "The roads are not properly maintained. Even though the maintainence work is done, its not that fast. Sanitary status is also not so good as well. The roads are not properly maintained.",32)
# transport3 = Problems(1, "Education issues","Education",  "level 2", "The roads are not properly maintained. Even though the maintainence work is done, its not that fast. Sanitary status is also not so good as well.Even though the maintainence work is done, its not that fast. Sanitary status is also not so good as well.",1)
# transport4 = Problems(1, "Drinking water","Drinking Water",  "level 1", "The roads are not properly maintained. Even though the maintainence work is done, its not that fast. Sanitary status is also not so good as well.Even though the maintainence work is done, its not that fast. Sanitary status is also not so good as well.",1)
# transport5 = Problems(1, "Electricity","Electricity",  "level 3", "The roads are not properly maintained. Even though the maintainence work is done, its not that fast. Sanitary status is also not so good as well.Sanitary status is also not so good as well. The roads are not properly maintained.",32)
# transport6 = Problems(1, "Health issues","Health",  "level 2","The roads are not properly maintained. Even though the maintainence work is done, its not that fast. Sanitary status is also not so good as well.Sanitary status is also not so good as well. The roads are not properly maintained.",1)
# problemarray = [transport,transport1,transport3,transport4,transport5,transport6]
problemarray = []
htmlCreator.hc(problemarray)

@app.route('/')
def mainHandler():
    return render_template('index.html')

@app.route('/issues')
def issueView():
    return htmlCreator.hc(problemarray)



@app.route('/send',methods=['GET','POST'])
def postData():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        catagory = request.form['service']
        label = request.form['budget']
        message = request.form['message']
        problemarray.append(Problems(id=1,title="Problem",catagory=catagory,level=label,details =message,count=1))
        return issueView()
       # return jsonify(problemarray)
    return mainHandler()



if __name__ == '__main__':
    app.secret_key = 'itstimetomoveon'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

