from flask import redirect
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag
from urllib.parse import unquote

info = Info(title="qip api", version="0.0.1")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentation", description="Documentation utilitary")

@app.get('/', tags=[home_tag], summary="Shows API doc")
def home():
    return redirect('/openapi/swagger')