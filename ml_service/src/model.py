class PreTrainedModel:
    def __init__(self):
        # Modify this as required. E.g. you don't need to build sklearn models
        self.built = False
        self.loaded = False
        self.model = None
        self._build()
        self._load()

    def _build(self):
        # once built, make self.built = True
        pass

    def _load(self):
        # if not self.built:
        #     raise RuntimeError("Model is not built.")
        pass

    def preprocess(self, input_x):
        # Preproces/Augment data before prediciton
        pass

    def predict(self, input_X):
        # if not self.built:
        #     raise RuntimeError("Model is not built.")
        # if not self.loaded:
        #     raise RuntimeError("Model is not loaded.")
        # preds = self.model.predict(input_X)
        # return preds
        pass
