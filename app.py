from flask import Flask,render_template,request
app=Flask(__name__)

JOBS=[
    {
        'id':1,
        'title': 'Data Analyst',
        'salary':'Rs.15,000,00',
        'location':'Delhi India'
    },
    {
        
        'id':2,
        'title': 'Data Engineer',
        'salary':'Rs.25,000,00',
        'location':'Hyderabad India'
    
    },
    {
        'id':3,
        'title': 'Busniess Analyst',
        'salary':'Rs.15,000,00',
        'location':'Munbia India'
    },
    {
        'id':4,
        'title': 'Web Developer',
        'salary':'Rs.10,000,00',
        'location':'Remote'
    }

]
@app.route('/')
def home():
    return render_template('hello.html',jobs=JOBS)

if __name__=='__main__':
    app.run(debug=True)