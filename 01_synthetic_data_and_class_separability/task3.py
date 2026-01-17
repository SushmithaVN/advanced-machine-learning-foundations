import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from data import generate_xor_data
from visual import plot_2d_data

def main():
    X,y = generate_xor_data(n=200)
    plot_2d_data(X,y, title="XOR Data (Original sapce)")

    # Linear SVM
    linear_svm = SVC(kernel='linear')
    linear_svm.fit(X,y)
    y_pred_linear = linear_svm.predict(X)
    plot_2d_data(X,y_pred_linear, title="Linear SVM prediction(Fails)")

    # Polynomial Kernel SVM
    poly_svm = SVC(kernel = 'poly', degree= 2)
    poly_svm.fit(X,y)
    y_pred_poly = poly_svm.predict(X)
    plot_2d_data(X,y_pred_poly, title="Polynomial Kernel SVM prediction (Succeeds)")

    # RBF Kernel SVM
    rbf_svm = SVC(kernel='rbf',gamma='scale')
    rbf_svm.fit(X,y)
    y_pred_rbf = rbf_svm.predict(X)
    plot_2d_data(X,y_pred_rbf, title="RBF kernel SVM prediction(Succeeds)")

    # print accuracies
    from sklearn.metrics import accuracy_score
    print("Linear SVM accuracy", accuracy_score(y,y_pred_linear))
    print("Polynomial SVM accuracy", accuracy_score(y,y_pred_poly))
    print("RBF SVM accuracy", accuracy_score(y,y_pred_rbf))

if __name__=="__main__":
    main()