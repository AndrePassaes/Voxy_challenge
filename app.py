from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def index() -> str:
    """
    This function handles both GET and POST requests to the root URL.

    Returns:
        A rendered HTML template with word count (if the request is POST and text is provided)
        or an error message (if the request is POST and text is not provided).
        If the request is GET, it returns the index.html template.
    """
    # Handle POST request
    if request.method == 'POST':
        # Get text from form data
        text: str = request.form.get('text', '')
        
        # Check if text is provided
        if text:
            # Calculate word count
            word_count: int = len(text.split())
            
            # Render index.html template with word count
            return render_template('index.html', word_count=word_count)
        
        # Render index.html template with error message
        return render_template('index.html', error='Text is required!')
    
    # Handle GET request
    # Render index.html template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    
#TODO
# Add a feature to test the implementation using Pytest
