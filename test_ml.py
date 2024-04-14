import pytest

from sklearn.ensemble import RandomForestClassifier
from ml.model import (
    compute_model_metrics,
    inference,
    train_model
)

def test_trainer():
    X_train = [[1,2,3,4,5],[1,2,3,4,5]]
    y_train = [[1,2,3,4,5],[1,2,3,4,5]]
    X_test = [[1,2,3,4,5],[1,2,3,4,5]]
    m = train_model(X_train, y_train)
    p = m.predict(X_test)
    assert p.all() == 1

def test_compute_metrics_model():
    y_test = [1,0,1,0,1]
    preds = [1,0,1,0,1]
    p, r, fb = compute_model_metrics(y_test, preds)
    assert fb == 1

def test_fucntion_inference():
    X_train = [[1,2,3,4,5],[1,2,3,4,5]]
    y_train = [[1,2,3,4,5],[1,2,3,4,5]]  
    X_test = [[1,2,3,4,5],[1,2,3,4,5]] 
    random_forest = RandomForestClassifier()
    model = random_forest.fit(X_train, y_train)
    p = inference(model, X_test)
    assert p.all() == 1