
from flask import Flask, jsonify, request

app = Flask(__name__)

todos = []

weather_data = {
    'astana': 15,
    'almaty': 20,
    'moscow': 5,
    'new york': 10
}

@app.route('/todos/new/<title>', methods=['GET'])
def add_todo(title):
    todos.append(title)
    return jsonify(todos), 200

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route('/todos/remove/<int:index>', methods=['GET'])
def remove_todo(index):
    if 0 <= index < len(todos):
        todos.pop(index)
        return jsonify(todos), 200
    else:
        return "Задание не найдено", 404

@app.route('/todos/get/<int:index>', methods=['GET'])
def get_todo(index):
    if 0 <= index < len(todos):
        return jsonify(todos[index]), 200
    else:
        return "Задание не найдено", 404

@app.route('/todos/edit/<int:index>/<new_title>', methods=['GET'])
def edit_todo(index, new_title):
    if 0 <= index < len(todos):
        todos[index] = new_title
        return jsonify(todos), 200
    else:
        return "Задание не найдено", 404

@app.route('/city/<city_name>', methods=['GET'])
def get_weather(city_name):
    city_name = city_name.lower()
    if city_name in weather_data:
        return f"Текущая погода в {city_name.capitalize()}: {weather_data[city_name]} цельсия", 200
    else:
        return f"У меня нет информации о погоде в {city_name.capitalize()}", 404

if __name__ == '__main__':
    app.run(debug=True)
