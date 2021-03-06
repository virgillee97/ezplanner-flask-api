from flask import Blueprint
from flask_restful import Api
from app.resources.Courses import CoursesResource
from app.resources.PreReq import PreReqResource
from app.resources.PostReq import PostReqResource
from app.resources.Planner import PlannerResource
from app.resources.TranscriptParser import TranscriptParserResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(CoursesResource, '/courses')
api.add_resource(PreReqResource, '/prereqs')
api.add_resource(PostReqResource, '/postreqs')
api.add_resource(PlannerResource, '/planner')
api.add_resource(TranscriptParserResource, '/parser')