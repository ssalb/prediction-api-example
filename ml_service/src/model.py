import pickle
from sklearn.svm import SVC

class PreTrainedModel:
    def __init__(self):
        self.built = False
        self.loaded = False
        self.model = None
        self._build()
        self._load()

    def _build(self):
        # Nothing to build in this example
        self.built = True

    def _load(self):
        if not self.built:
            raise RuntimeError("Model is not built.")
        
        with open(f"model/my-model.pkl", "rb") as f:
            self.model = pickle.load(f)
        self.loaded = True

    def preprocess(self, input_x):
        # Nothing to do in this example
        return input_x

    def predict(self, input_X):
        if not self.built:
            raise RuntimeError("Model is not built.")
        if not self.loaded:
            raise RuntimeError("Model is not loaded.")
        preds = self.model.predict(input_X)
        return preds
