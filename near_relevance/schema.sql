DROP TABLE IF EXISTS model;
DROP TABLE IF EXISTS model_result;

CREATE TABLE model (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  model_name TEXT UNIQUE NOT NULL
);

CREATE TABLE model_result (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  model_id INTEGER NOT NULL,
  generated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  input_text TEXT NOT NULL,
  result TEXT NOT NULL,
  FOREIGN KEY (model_id) REFERENCES model (id)
);

INSERT INTO model(model_name) values ('ulmfit');
INSERT INTO model(model_name) values ('logistic_regression');
INSERT INTO model(model_name) values ('xgboost');