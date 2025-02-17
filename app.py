#from cgitb import text
from flask import Flask,render_template,request
import model 
app = Flask('__name__')

valid_userid = ['00sab00','1234','zippy','zburt5','joshua','dorothy w','rebecca','walker557','samantha','raeanne','kimmie','cassie','moore222']

@app.route('/favicon.ico')
def favicon():
    return '', 204  # No content, just avoid 404

@app.route('/')
def view():
    return render_template('index.html', text=None)

@app.route('/recommend',methods=['POST'])
def recommend_top5():
    user_name = request.form.get("username")
    other_username = request.form.get("other_username")

    # Use manually entered name if "Other" was selected
    if user_name == "Other" and other_username:
        user_name = other_username
    print('user_name=',user_name)    
    if  user_name in valid_userid and request.method == 'POST':
            top20_products = model.recommend_products(user_name)
            get_top5 = model.top5_products(top20_products)
            return render_template('index.html',
                                   column_names=get_top5.columns.values, 
                                   row_data=list(get_top5.values.tolist()), 
                                   zip=zip,
                                   text=f'Recommended products for {user_name}'
                                   )
    elif not user_name in  valid_userid:
        return render_template('index.html',text=f'No Recommendation found for the user {user_name}')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    # app.debug=True

    app.run(debug=True)
