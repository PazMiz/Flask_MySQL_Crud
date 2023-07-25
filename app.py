from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# MySQL configuration
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'cars'
}

# Connect to MySQL database
conn = mysql.connector.connect(**mysql_config)
cursor = conn.cursor()

@app.route('/create_car', methods=['POST'])
def create_car():
    try:
        # Get data from the request JSON
        data = request.json['cars']
        print(data)  # Add this line to print the received data

        # SQL query to insert data into the "cars" table
        insert_query = """
            INSERT INTO cars (model, color) VALUES (%s, %s)
        """

        # Execute the query for each car record
        for car in data:
            model = car['model']
            color = car['color']
            cursor.execute(insert_query, (model, color))

        conn.commit()

        return 'Car data inserted successfully!', 200
    except Exception as e:
        print(e)  # Add this line to print the error message
        return f"Error creating car record: {e}", 500


# Route to fetch car data as JSON
@app.route('/cars', methods=['GET'])
def get_cars():
    query = 'SELECT id, model, color FROM cars'
    cursor.execute(query)
    cars_data = cursor.fetchall()

    # Convert data to a list of dictionaries
    cars_list = []
    for car in cars_data:
        car_dict = {'id': car[0], 'model': car[1], 'color': car[2]}
        cars_list.append(car_dict)

    return jsonify(cars_list)



@app.route('/update_car', methods=['POST'])
def update_car():
    try:
        # Get data from the request JSON
        data = request.json['cars']
        print(data)  # Add this line to print the received data

        # SQL query to update data in the "cars" table
        update_query = """
            UPDATE cars SET model = %s, color = %s WHERE id = %s
        """

        # Execute the query for each car record
        for car in data:
            model = car['model']
            color = car['color']
            car_id = car['id']
            cursor.execute(update_query, (model, color, car_id))

        conn.commit()

        return 'Car data updated successfully!', 200
    except Exception as e:
        print(e)  # Add this line to print the error message
        return f"Error updating car record: {e}", 500
    
@app.route('/delete_car', methods=['POST'])
def delete_car():
    try:
        # Get the car ID from the request JSON
        car_id = request.json['car_id']

        # SQL query to delete a car record
        delete_query = """
            DELETE FROM cars WHERE id = %s
        """

        cursor.execute(delete_query, (car_id,))
        conn.commit()

        return 'Car data deleted successfully!', 200
    except Exception as e:
        print(e)  # Add this line to print the error message
        return f"Error deleting car record: {e}", 500



if __name__ == '__main__':
    app.run(debug=True)
