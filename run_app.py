from app import create_app, socketio

# Option ngrok si besoin
# from pyngrok import ngrok
# public_url = ngrok.connect(5000)
# print("Ngrok URL:", public_url)

app = create_app()

if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0", port=5000)
