class LearningData(object):
    def __init__(self, id, text, pred):
        self.id = id
        self.text = text
        self.pred = pred

    def toJSON(self):
        return {
            '_id': self.id,
            'text': self.text,
            'pred': self.pred.tolist()
        }