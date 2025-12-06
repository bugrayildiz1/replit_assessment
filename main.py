from flask import Flask, request, render_template_string
import requests

app = Flask('app')

HTML_TEMPLATE = """
<html>
  <head>
    <title>XKCD Portal</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        max-width: 800px;
        margin: 50px auto;
        padding: 20px;
        background-color: #f5f5f5;
      }
      .container {
        background-color: white;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
      }
      h1 {
        color: #333;
      }
      form {
        margin: 20px 0;
      }
      input[type="number"] {
        padding: 10px;
        font-size: 16px;
        width: 200px;
        border: 2px solid #ddd;
        border-radius: 5px;
      }
      button {
        padding: 10px 20px;
        font-size: 16px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
      }
      button:hover {
        background-color: #45a049;
      }
      .comic-container {
        margin-top: 30px;
        text-align: center;
      }
      .comic-image {
        max-width: 100%;
        height: auto;
        border: 2px solid #ddd;
        border-radius: 5px;
      }
      .comic-title {
        font-size: 18px;
        font-weight: bold;
        margin: 10px 0;
        color: #333;
      }
      .error {
        color: #d32f2f;
        font-weight: bold;
        margin: 20px 0;
      }
      .fallback-image {
        max-width: 400px;
        margin: 20px auto;
        display: block;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>XKCD Portal</h1>
      <p>Enter an XKCD comic ID number to view the comic.</p>
      
      <form method="POST" action="/">
        <label for="comic_id">Comic ID:</label>
        <input type="number" id="comic_id" name="comic_id" min="1" value="{{ default_id }}" required>
        <button type="submit">Get Comic</button>
      </form>

      {% if error %}
        <div class="error">{{ error }}</div>
        <div class="comic-container">
          <p>Here's a random XKCD comic instead:</p>
          <img src="https://imgs.xkcd.com/comics/random.png" alt="Random XKCD" class="fallback-image" onerror="this.src='https://via.placeholder.com/400x200?text=XKCD+Not+Available'">
        </div>
      {% elif comic_data %}
        <div class="comic-container">
          <div class="comic-title">{{ comic_data.title }}</div>
          <img src="{{ comic_data.img }}" alt="{{ comic_data.alt }}" class="comic-image">
          <p style="margin-top: 10px; color: #666; font-style: italic;">{{ comic_data.alt }}</p>
        </div>
      {% endif %}

      <p style="margin-top: 30px; color: #666; font-size: 14px;">
        Use the XKCD JSON API: <code>https://xkcd.com/{id}/info.0.json</code> to get the metadata of one of the (currently) 2752 XKCDs.
      </p>
    </div>
  </body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    default_id = 936
    error = None
    comic_data = None
    
    submitted_id = default_id
    
    if request.method == 'POST':
        # Get the comic ID from the form
        comic_id = request.form.get('comic_id', type=int)
        submitted_id = comic_id if comic_id else default_id
        
        if comic_id:
            try:
                # Fetch the XKCD comic data
                url = f"https://xkcd.com/{comic_id}/info.0.json"
                response = requests.get(url, timeout=5)
                
                if response.status_code == 200:
                    comic_data = response.json()
                else:
                    error = f"Comic with ID {comic_id} could not be found."
            except requests.exceptions.RequestException as e:
                error = f"Error fetching comic with ID {comic_id}: {str(e)}"
        else:
            error = "Please provide a valid comic ID."
    
    return render_template_string(HTML_TEMPLATE, 
                                 default_id=submitted_id,
                                 error=error,
                                 comic_data=comic_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

