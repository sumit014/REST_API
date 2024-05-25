from flask import Flask, jsonify

app = Flask(__name__)

courses = [{
                       "Description": "Python programming certification helps you learnpython in the structured learning path with Innovative out of the hox projects watching the industry standards",

                       "course_id": "8",

                       "name": "Python Programming Certification",

                       "price": "visit Edureka.co to know more"
                   },
                   {
                       "Description": "Data science with python helps you master the data science life cycle processes in a structured learning path",

                       "course_id": "1",

                       "name": "Data Science With Python Certification",

                       "price": "visit edureka.co to know more"
                   },
                   {
                       "Description": "AI and HL certification will help you master AI/ML with top notch projects like speechrecognition, chatbots, etc..",

                       "course_id": "2",

                       "name": "AI and Machine Learning Certification",

                       "price": "visit edureka.co to know more"
                   },
                   {
                       "Description": "ySpark Certification Training is designed to provide you the knowledge and skillsthat are required to become a successful Spark Developer using Python and prepareyou for the Cloudera madoop and Spark Developer Certification Exam",

                       "course_id": "3",

                       "name": "Python Spark Certification",

                       "price": "visit edureka.co to know more"
                   },
                   {
                       "Description": "Natural Language Processing with Python course will take you through the essentialsof text processing all the way up to classifying texts using Machine Learning",

                       "course_id": "4",

                       "name": "Natural Language Processing With Python Certification",

                       "Price": "visit edureka.co to know more"
                   }
    ]


@app.route('/')
def index():
    return "Welcome to REST API"


@app.route("/courses", methods=["GET"])
def get():
    return jsonify({"Courses": courses})


@app.route("/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    return jsonify({"Courses": courses[course_id]})


@app.route("/courses", methods=["POST"])
def create():
    course = {
                       "Description": "Natural Language Processing with Python course will take you through the essentialsof text processing all the way up to classifying texts using Machine Learning",

                       "course_id": "5",

                       "name": "Natural Language Processing With Python Certification",

                       "Price": "visit edureka.co to know more"
                   }
    courses.append(course)
    return jsonify({"created": course})


@app.route("/courses/<int:course_id>", methods=['PUT'])
def course_update(course_id):
    courses[course_id]['Description'] = "XYZ"
    return jsonify({"Updated": courses[course_id]})


@app.route("/courses/<int:course_id>", methods=['DELETE'])
def course_delete(course_id):
    courses.remove(courses[course_id])
    return jsonify({'result': True})


if __name__ == "__main__":
    app.run(debug = True)
