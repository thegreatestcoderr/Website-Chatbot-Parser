from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'id': 1,
        'title': 'First Blog Post',
        'date': 'May 15, 2025',
        'content': 'This is the content of my first blog post. It can contain lots of interesting information.'
    },
    {
        'id': 2,
        'title': 'Another Great Post',
        'date': 'May 10, 2025',
        'content': 'Here\'s some more insightful writing for you to enjoy.'
     }
]
@app.route('/post/<int:post_id')
def post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    else:
        return 'Post not found.'
if __name__ == '__main__':
    app.run(debug=True)
