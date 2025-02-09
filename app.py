from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

# A sample endpoint that (naïvely) uses user input.
# In real applications, ensure proper input sanitization.
@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    # Potential vulnerability: rendering unsanitized input.
    template = f"Hello, {name}!"
    return render_template_string(template)

if __name__ == '__main__':
    # Run the app so that it is accessible for DAST scans.
    app.run(host='0.0.0.0', port=5000)
