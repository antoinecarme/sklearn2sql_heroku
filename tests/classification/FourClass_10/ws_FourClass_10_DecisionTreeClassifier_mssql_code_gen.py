from sklearn2sql_heroku.tests.classification import generic as class_gen


class_gen.test_model("DecisionTreeClassifier" , "FourClass_10" , "mssql")