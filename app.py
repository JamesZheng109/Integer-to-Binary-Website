#import
from flask import Flask,render_template,request,abort
app=Flask(__name__)
#list of numeric repesentation of 8-bit binary
binary_list=[128,64,32,16,8,4,2,1]
#Home
@app.route('/')
def home():
    return render_template('index.html')
#Output
@app.route('/output',methods=['GET','POST'])
def output():
    #Check method
    if request.method=='POST':
        #Check within acceptable range
        if request.form['variable'].isdigit():
            if int(request.form['variable'])>=0 and int(request.form['variable'])<=255:
                #variable to hold num
                num_hold=int(request.form['variable'])
                #variable to hold final output
                output=''
                for i in binary_list:
                    if i<=num_hold:
                        num_hold-=i
                        output+='1'
                    elif i>=num_hold:
                        output+='0'  
                return render_template('index.html', output=output),201
            else:
                abort(500,'Not within 0 and 255')
        else:
            abort(500,'Not within acceptable input')
    elif request.method=='GET':
        return render_template('index.html')
#Run app
if __name__=='__main__':
    app.run()