# VOXY CODE CHALLENGE

CREATE A USER-FACING FORM THAT COUNTS THE NUMBER OF WORDS IN A BLOCK OF TEXT.

Acceptance Criteria:

● As a user when I view the application then I see a form containing a text box
to enter a body of text and when I submit the form with some text then I see
a result containing the number of words in the text box; and when I submit
the form with an empty text then I see a form error telling me that some text
input is required.

● As an engineer when I look at your project then I should understand how to
install and run it.

● The form can be delivered as a web page or mobile app. The word counting
function(s) can be implemented in whatever language or framework you
prefer.

● You may use any third-party libraries or packages that you need to.

*SOLUTION PRESENTATION*

I have created a simple web application using Python language and Flask Framework, `render_template`, and `request` libraries. The front end was developed with HTML. There is room for improvement with JavaScript and CSS in the front end.

`Flask` - A Python Framework is known to be light and easy, excellent for small applications.
`render_template`- A Flask built-in functionality from the `Jinja2` template engine to automatically render `html`templates.

`request` - Flask built-in library to handle HTTP requests.

`html` template: The `index.html` template creates the user interface. There is room to improve the UX by improving the HTML template and implementing CSS in the code.

`Error Handling` - The code includes error handling to display an error if the user submits the text field empty. It was implemented to prevent unexpected behavior.

# HOW TO RUN THE APPLICATION

- Clone the repository;

- Run the code;

- Open the localhost route;

- Insert some words, and submit;

- If you submit without writing words, an error message will dislay.