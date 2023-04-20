from rest_framework.views import APIView

from .serializer import CreatePatient




# Create your views here.


# TODO: API to admit new patient

class AdmitPatient(APIView):

    def post(self, request):

        request_data = request.data.copy()

        field_spec = [
            {"key": "id", "type": str, "is_mandatory": True, "is_none_allowed": False},
            {"key": "name", "type": str, "is_mandatory": True, "is_none_allowed": False},
            {"key": "age", "type": str},
            {"key": "gender", "type": str},
            {"key": "dob", "type": str, "is_mandatory": True, "is_none_allowed": False},
            {"key": "disease", "type": str},
            {"key": "admit_date", "type": str, "is_mandatory": True, "is_none_allowed": False},
            {"key": "discharge_date", "type": str, "is_mandatory": True, "is_none_allowed": False},
            {"key": "location", "type": str},
            {"key": "contact_no", "type": str, "is_mandatory": True, "is_none_allowed": False},

        ]

        





# View details
# Admit new patient
# Update patient
# delete patient
