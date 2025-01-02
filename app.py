from flask import Flask,render_template,request
import numpy as np
import pickle
popular_df=pickle.load(open('popular.pkl','rb'))
final_table=pickle.load(open('final_table.pkl','rb'))
similarity_score=pickle.load(open('similarity_score.pkl','rb'))
books=pickle.load(open('books.pkl','rb'))
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html',book_name=list(popular_df['Book-Title'].values),image=list(popular_df['Image-URL-M']),author=list(popular_df['Book-Author']),votes=list(popular_df['num-rating']),score=list(popular_df['avg-rating']))
@app.route('/recommend')
def recommend():
    return render_template('recommend.html')
@app.route('/recommend_books',methods=['post'])
def recommendation():
    user_input = request.form.get('user_input')
    index=np.where(final_table.index==user_input)[0][0] # fetching index
    similar_items=sorted(list(enumerate(similarity_score[index])),key=lambda x:x[1],reverse=True)[1:6]
    data = []
    for i in similar_items:
        item = []
        temp_data = books[books['Book-Title'] == final_table.index[i[0]]]
        item.extend(list(temp_data.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_data.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_data.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)
    return render_template('recommend.html',data=data)


if __name__ == '__main__':
    app.run(debug=True)
