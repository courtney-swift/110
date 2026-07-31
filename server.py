from flask import Flask, jsonify, request
import uuid

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


"""
Mini-Challenge

-Create a GET /user endpoint
-Return a dictionary:
  -name
  -role
  -is_active
  -favorite_technologies
  -Test on Thunderclient http://127.0.0.1:5000/user
"""

#http://127.0.0.1:5000/greet/Courtney
@app.route("/greet/<string:name>", methods=["GET"])
def say_hello(name):
  return f"hello {name}"




#---------Products----------
products = [
  {
      "id": "1",
      "title": "Nintendo Switch",
      "price": 499.99,
      "category": "Electronics",
      "image": "https://picsum.photos/300/200?random=1"
  },

  {
      "id": "2",
      "title": "Smart Refrigerator",
      "price": 999.99,
      "category": "Kitchen",
      "image": "https://picsum.photos/300/200?random=1"
  },

  {
      "id": "3",
      "title": "Bluetooth Speaker",
      "price": 78.99,
      "category": "Electronics",
      "image": "https://picsum.photos/300/200?random=1"
  }
]

@app.route("/api/products", methods=["GET"])
def get_products():
  return jsonify(products)



# http://127.0.0.1:5000/api/products/2
@app.route("/api/products/<string:product_id>")
def get_product_by_id(product_id):
  print(f"product id = {product_id}")
  for product in products:
    print(product)
    if product["id"] == product_id:
      return jsonify({
      "success": True,
      "message": "Product retrieved successfully",
      "data": product
    }), 200
  return jsonify({ 
    "success": False,
    "message": "Product not found"
  }), 404 # 404 Not Found

# POST http://127.0.0.1:5000/api/products
@app.route("/api/products", methods=["POST"])
def create_product():
  new_product = request.get_json()
  new_product["id"] = str(uuid.uuid4())
  products.append(new_product)
  print(new_product)


  return jsonify({
    "success": True,
    "Message": "Product created successfully"
  }), 201 # Created


# PUT http://127.0.0.1:5000/api/products/<>
@app.route("/api/products/<string:product_id>", methods=["PUT"])
def update_product_by_id(product_id):
    updated_product = request.get_json()
    print(updated_product)
    for product in products:
      if product["id"] == product_id:
        product["title"] = updated_product["title"]
        product["price"] = updated_product["price"]
        product["category"] = updated_product["category"]
        product["image"] = updated_product["image"]
        return jsonify({
          "success": True,
          "message": "Product updated successfully"
        }), 200 # OK
    return jsonify({
      "success": False,
      "message": "Product not Found"
    }), 404 # Not Found


# DELETE http://127.0.0.1:5000/api/products/<>
@app.route("/api/products/<string:product_id>", methods=["DELETE"])
def delete_product_by_id(product_id):
  print(f"the product id is = {product_id}")
  for product in products: 
      print(product["id"])
      if product["id"] == product_id:
        products.remove(product)
        return jsonify({
          "success": True,
          "message": "Product deleted successfully"
      }), 200
  return jsonify({
    "success": False,
    "message": "Product not found"
  }), 404 # not found

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


coupons = [
    {"id": 1, "code": "WELCOME10", "discount": 10},
    {"id": 2, "code": "SPOOKY25", "discount": 25},
    {"id": 3, "code": "VIP50", "discount": 50}
]


@app.route("/api/coupons", methods=["GET"])
def get_coupons():
    return jsonify(coupons), 200


@app.route("/api/coupons", methods=["POST"])
def create_coupon():

    new_coupon = request.get_json()

    if not new_coupon:
        return jsonify({
            "success": False,
            "message": "No coupon"
        }), 400

    new_coupon["id"] = len(coupons) + 1

    coupons.append(new_coupon)

    return jsonify({
        "success": True,
        "message": "Coupon created successfully",
        "data": new_coupon,
    }), 201



@app.route("/api/coupons/<int:id>", methods=["GET"])
def get_coupon_by_id(id):
    for coupon in coupons:
        if coupon["id"] == id:
            return jsonify({
                "success": True,
                "message": "Coupon found",
                "data": coupon
            }), 200

    return jsonify({
        "success": False,
        "message": "Coupon not found"
    }), 404



# DELETE http://127.0.0.1:5000/api/coupons/<>
@app.route("/api/coupons/<int:id>", methods=["DELETE"])
def delete_coupon_by_id(coupon_id):
  for coupon in coupons:
    if coupon["id"] == coupon_id:
      coupons.remove(coupon)
      return jsonify({
          "success": True,
          "message": "Coupon deleted successfully"
      }), 200
    
  return jsonify({
    "success": False,
    "message": "Coupon not found"
  }), 404 # not found

# http://127.0.0.1:5000/api/coupons/<>
@app.route("/api/coupons/<int:id>", methods=["PUT"])
def update_coupon_by_id(id):
    updated_coupon = request.get_json()
    for coupon in coupons:
        if coupon["id"] == id:
            coupon["code"] = updated_coupon["code"]
            coupon["discount"] = updated_coupon["discount"]
            return jsonify({
                "success": True,
                "message": "Coupon updated successfully"
            }), 200
    return jsonify({
        "success": False,
        "message": "Coupon not found"
    }), 404
app.run(debug=True)