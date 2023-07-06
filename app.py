from flask import redirect
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag
from urllib.parse import unquote

info = Info(title="qip api", version="0.0.1")
app = OpenAPI(__name__, info=info)
CORS(app)