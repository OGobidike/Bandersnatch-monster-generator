from datetime import datetime
from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
from joblib import dump, load


class Machine:

    def __init__(self, df):
        self.name = 'Random Forest Classifier'

        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # year month day...

        target_y = df['Rarity']
        features_x = df.drop(columns=['Rarity'])

        self.model = RandomForestClassifier(
            n_estimators=100,
            max_depth=30,
            min_samples_split=5,
            min_samples_leaf=2,
            max_features='sqrt',
            bootstrap=False,
            random_state=42
        )

        self.model.fit(features_x, target_y)


    def __call__(self, feature_basis):
        prediction, *_ = self.model.predict(feature_basis)
        probability, *_ = self.model.predict_proba(feature_basis)
        return prediction, max(probability)

    def save(self, filepath):
        # make sure save method is dump()'ed into file name 'model.joblib()'
        dump(self.model, "model.joblib")


    @staticmethod
    def open(filepath):
        model = load("model.joblib")

        return model

    def info(self):
        return f'Currently running: {self.name}, at: {self.timestamp}'
