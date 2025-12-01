import logging
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Configure logging to log to stdout and stderr
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s',
                    handlers=[logging.StreamHandler()])

# Sample course documents
courses = {
    'Python': ['https://www.w3schools.com/python/', 'https://docs.python.org/3/tutorial/'],
    'HTML': ['https://www.w3schools.com/html/'],
    'CSS': ['https://www.w3schools.com/css/'],
    'JavaScript': ['https://www.w3schools.com/js/']
}

@app.route('/')
def index():
    app.logger.info('Main page accessed')
    return render_template('index.html', courses=courses)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    app.logger.info(f'Search for course: {query}')
    if query in courses:
        return render_template('index.html', courses={query: courses[query]})
    else:
        app.logger.warning(f'Course not found: {query}')
        return "Course not found", 404

@app.route('/add_course', methods=['POST'])
def add_course():
    course_name = request.form['course_name']
    course_link = request.form['course_link']
    app.logger.info(f'Adding course: {course_name} with link: {course_link}')
    if course_name in courses:
        courses[course_name].append(course_link)
    else:
        courses[course_name] = [course_link]
    return redirect(url_for('index'))

@app.route('/clear')
def clear():
    app.logger.info('Filter cleared')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
