import numpy as np
import featureExtraction
from sklearn import tree
from sklearn.model_selection import train_test_split
def CheckUrl(url,setPrecisionTo,country,setdomain,createdate,expirydate,servername,setipaddress,urllen,orgname,statename):
    #Importing dataset
    # return True
    data = np.loadtxt("maindataset.csv", delimiter = ",")

    #Seperating features and labels
    X = data[: , :-1]
    y = data[: , -1]

    #Seperating training features, testing features, training labels & testing labels
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

    clf = tree.DecisionTreeClassifier()


    clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    setPrecisionTo.set(score*100)
    X_new = []

    X_input = url
    X_new=featureExtraction.generate_result(X_input,country,setdomain,createdate,expirydate,servername,setipaddress,urllen,orgname,statename)
    X_new = np.array(X_new).reshape(1,-1)
    
    # check input url is in our phiching-sites.txt file
    f=open("phishing-sites.txt","r")
    for i in f.read().split("\n"):
        if url in i:
            return False
    f.close()
    # check input url is in our legit-sites.txt file
    f=open("legit-sites.txt","r")
    for i in f.read().split("\n"):
        if url in i:
            return True
    f.close()
    prediction = clf.predict(X_new)
    if prediction == -1:
        return False
    else:
        return True
