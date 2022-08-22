from aenum import StrEnum


class Headers:
    AUTHORIZATION = lambda  token : {f"'Authorization': '{token}'"}
    CT_APPLICATION_JSON = {"content-type": "application/json"}
    TOKEN = {'X-CSRFToken': 'ImYwYjJlYzczY2IxYmU0NjRmOWFmZjM0MDEyN2U3ODdiNzkxMmMwNzci.Yvff0g.SYfJCIAiGdffqdR9JlsEqtnrN8M'}
