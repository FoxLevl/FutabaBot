from config import MODEL_NAME


class Brain:

    def __init__(self):
        self.model_name = MODEL_NAME
    
    def generate_response(self):
        return "HALLOOOOO" + self.model_name