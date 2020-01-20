"""
Application Manager.
Use this script to start the Flask server.
"""

import sys

from app import create_app

app = create_app()
app.run(debug=True,
        host=sys.argv[1],
        port=sys.argv[2])
