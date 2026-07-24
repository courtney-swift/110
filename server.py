from flask import Flask

app = Flask(__name__) # Intance of Flask

@app.route("/home", methods=["GET"])
def home():
    return {"message": "Welcome to Flask, cohort#68"}


@app.route("/greet-students", methods=["GET"])
def say_hi():
  return {"message": "Ey hello students"}


 #GET /cohort68 

@app.route("/cohort68", methods=["GET"])
def get_students_68():
  student_list = ["Courtney", "Shea", "Tim", "Nico", "Cole", "Titan", "Adam", "Leo"]
  return student_list


# GET http://127.0.0.1:5000/course_information
@app.route("/course_information", methods=["GET"])
def get_course_information():
  course_information = {
     "title": "Inroductory web API with Flask",
     "Duration": "4 Sessions",
     "level": "Beginner"
  }
  return course_information


@app.route("/coupon_list", methods=["GET"])
def get_coupon_list():
  coupon_list = [
  {"_id": 1, "code": "WELCOME10", "discount": 10}, 
  {"_id": 2, "code": "SPOOKY25", "discount": 25},
  {"_id": 3, "code": "VIP50", "discount": 50} ]
  return coupon_list



@app.route("/coupon_count", methods=["GET"])
def get_coupon_count():
    coupon_list = [
        {"_id": 1, "code": "WELCOME10", "discount": 10},
        {"_id": 2, "code": "SPOOKY25", "discount": 25},
        {"_id": 3, "code": "VIP50", "discount": 50}
    ]

    return {"count": len(coupon_list)}


# coupons = [ {"_id": 1, "code": "WELCOME10", "discount": 10},
  #         {"_id": 2, "code": "SPOOKY25", "discount": 25},
  #         {"_id": 3, "code": "VIP50", "discount": 50} #

  #GET /api/coupons endpoint that returns a list of coupons.
  #GET /api/coupons/count returns the number of coupons in the system.


app.run(debug=True)