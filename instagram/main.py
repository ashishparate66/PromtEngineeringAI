from flask import Flask

app=Flask(__name__)
dis=[]

@app.route('/post/<int:post_id>')
def add_image(post_id):
      return  dis.append({post_id})

@app.route('/user/<username>')
def show_profile(username):
      return  dis

@app.route('/post/<int:post_id>')
def delete_image(post_id):
      return  dis.delete({post_id})




