from flask import Flask, url_for, request, render_template, redirect
from use_model import recommend, nameCheck 

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def index():
    movies=[]
    if request.method == 'POST':
        try:
            movie, found = nameCheck(request.form['content'])
            if found == False:
                return movie
            else:
                rec_movies = recommend(movie)
                print(rec_movies)

                movies = [movie for movie in rec_movies]
                return render_template('index.html', movies=movies)
                # return redirect('/')
        except:
            return "Error in movies"
        
    else:        
        movies=[]
        return render_template('index.html', movies=movies)


if __name__ == '__main__':
    app.run(debug=True)