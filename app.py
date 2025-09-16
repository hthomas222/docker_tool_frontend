from flask import Flask, render_template, request, redirect, url_for
import subprocess


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ""
    if request.method == 'POST':
        command = subprocess.run(["docker", "ps", "-a", "--format", "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Status}}\t{{.Ports}}"], capture_output=True, text=True)
        output = command.stdout + command.stderr
        if command.returncode != 0:
            output = f"Error (code {command.returncode}):\n{output}"
    return render_template('index.html', context=output)


@app.route('/images', methods=['GET', 'POST'])
def images():
    output = ""
    if request.method == 'POST':
        command = subprocess.run(
            ["docker", "images"], 
            capture_output=True, text=True
        )
        output = command.stdout + command.stderr
        if command.returncode != 0:
            output = f"Error (code {command.returncode}):\n{output}"
    return render_template('images.html', active_page='images', output=output)

@app.route('/df', methods=['GET', 'POST'])
def df():
    output = ""
    if request.method == 'POST':
        command = subprocess.run(
            ["docker", "system", "df"], 
            capture_output=True, text=True
        )
        output = command.stdout + command.stderr
        if command.returncode != 0:
            output = f"Error (code {command.returncode}):\n{output}"
    return render_template('df.html', active_page='df', output=output)

@app.route('/start', methods=['GET', 'POST'])
def start():
    output = ""
    if request.method == 'POST':
        container_id = request.form.get('container_id')
        if container_id:
            command = subprocess.run(
                ["docker", "start", container_id],
                capture_output=True,
                text=True
            )
            output = command.stdout + command.stderr
            if command.returncode != 0:
                output = f"Error (code {command.returncode}):\n{output}"
    return render_template('start.html', active_page='start', output=output)


@app.route('/stop', methods=['GET', 'POST'])
def stop():
    output = ""
    if request.method == 'POST':
        container_id = request.form.get('container_id')
        if container_id:
            command = subprocess.run(
                ["docker", "stop", container_id],
                capture_output=True,
                text=True
            )
            output = command.stdout + command.stderr
            if command.returncode != 0:
                output = f"Error (code {command.returncode}):\n{output}"
    return render_template('stop.html', active_page='stop')


@app.route('/system', methods=['GET', 'POST'])
def system():
    output = ""
    if request.method == 'POST':
        command = subprocess.run(
            ["docker", "system", "prune", "-f"], 
            capture_output=True, text=True
        )
        output = command.stdout + command.stderr
        if command.returncode != 0:
            output = f"Error (code {command.returncode}):\n{output}"
    return render_template('system.html', active_page='system', output=output)


if __name__ == '__main__':
     app.run(port=5000, debug=True)
