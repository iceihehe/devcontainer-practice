from flask import Flask


def status():
        
    return {
        "status": "OK"
    }, 200, {"Content-Type": "application/json"}


def create_app():
    
    app = Flask("devcontainer-practice")
    
    app.add_url_rule("/status", view_func=status)
    
    return app
