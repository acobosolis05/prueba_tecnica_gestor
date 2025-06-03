from api.endpoints import app
import uvicorn
import logging

if __name__ == "__main__":
    try: 
        uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)

    except Exception as e:
        logging.error(f"Error starting the server: {e}"), 400
    

