from flask import Flask, render_template, send_file, make_response, jsonify
import io
import livepopulartimes
import matplotlib.pyplot as plt

# Set Matplotlib to use the Agg backend
plt.switch_backend('Agg')

app = Flask(__name__)

def generate_chart(popular_times):
    # Extract relevant data from popular_times
    days = [day['name'] for day in popular_times]
    hours = list(range(24))
    popularity_data = [day['data'] for day in popular_times]

    # Create a line chart using matplotlib
    plt.figure(figsize=(12, 6))

    for i, day_data in enumerate(popularity_data):
        plt.plot(hours, day_data, label=days[i])

    plt.title('Popular Times Throughout the Week')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Popularity')
    plt.legend()

    # Save the chart to a BytesIO object
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    return img

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_popular_times')
def get_popular_times():
    # Replace with the actual address and your Google API Key
    formatted_address = "(H-Mart Dunbar) 5557 Dunbar Street, Vancouver BC, Canada"
    API_KEY = "AIzaSyBgGz3o7wxW7Z3FeqURE8mo6hqbERk4MgQ"

    try:
        result = livepopulartimes.get_populartimes_by_address(formatted_address)
        img = generate_chart(result['populartimes'])
        response = make_response(send_file(img, mimetype='image/png'))
        response.headers['Content-Disposition'] = 'inline; filename=popular_times.png'
        return response
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
