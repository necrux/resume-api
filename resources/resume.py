import requests
import yaml
from flask.views import MethodView
from flask_smorest import Blueprint, abort

RESUME_ENDPOINT = "https://raw.githubusercontent.com/weshenderson/weshenderson.github.io/main/configs/resume.yaml"
resume = {}

blp = Blueprint("Resume", __name__, description="Operations on Wes' Resume")


@blp.route("/")
class Welcome(MethodView):
    def get(self):
        return {"message": "Welcome. Be sure to review the Swagger docs: /swagger-ui"}


@blp.route("/resume")
class Resume(MethodView):
    def get(self):
        return resume


@blp.route("/resume/refresh")
class Refresh(MethodView):
    def get(self):
        global resume
        try:
            response = requests.get(url=RESUME_ENDPOINT)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            abort(500, message="Failed to update resume content. Please try again.")
        else:
            resume = yaml.safe_load(response.text)
            return "Grabbed the latest resume."


@blp.route("/resume/<string:section>")
class Section(MethodView):
    def get(self, section):
        try:
            return resume[section.title()]
        except KeyError:
            abort(404, message=f"No section found: {section}")
