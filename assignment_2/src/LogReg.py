import cv2
import matplotlib
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import tensorflow
from tensorflow.keras.datasets import cifar10



def preprocessing(X_train, X_test):
    '''
    This function grayscales, normalizes and reshapes the data
    '''
    done_list_train = []
    for picture in X_train:
        greyscaled= cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY) 
        normalized = greyscaled/255.0 
        done_list_train.append(normalized) 
    X_train=np.array(done_list_train) 
    X_train = X_train.reshape(-1,1024)


    done_list_test = []
    for picture in X_test:
        greyscaled= cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY) 
        normalized = greyscaled/255.0 
        done_list_test.append(normalized) 
    X_test=np.array(done_list_test) 
    X_test= X_test.reshape(-1,1024) 

    return X_train, X_test



def fit_classfier(X_train, y_train):
    '''
    This function defines a classifier and fit the model
    '''
    classifier = LogisticRegression(tol = 0.1,
                                solver = 'saga',
                                multi_class = 'multinomial',
                                random_state = 789)

    model = classifier.fit(X_train, y_train)

    return model, classifier



def evaluate(model, X_test, y_test):
    '''
    This function makes predictions, creates classification report and save it in the out folder
    '''
    y_pred = model.predict(X_test)  
    classifier_metrics = metrics.classification_report(y_test, y_pred, target_names =["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"])

    filepath = "../out/log_classification_report.txt"

    with open(filepath, 'w') as file:
        file.write(classifier_metrics)



def main():
    (X_train, y_train), (X_test, y_test) = cifar10.load_data()
    X_train, X_test = preprocessing(X_train, X_test)
    model, classifier = fit_classfier(X_train, y_train)
    evaluate(model, X_test, y_test)


if __name__ == "__main__":
    main()