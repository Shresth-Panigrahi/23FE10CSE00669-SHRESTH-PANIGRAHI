import os
import sys
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def main():
    try:
        df = pd.read_excel('../ENB2012_data.xlsx')
    except Exception as e:
        print('Failed to read dataset:', e)
        sys.exit(1)

    # Create binary target
    df['Y1_binary'] = (df['Y1'] > df['Y1'].median()).astype(int)

    X = df.drop(['Y1', 'Y2', 'Y1_binary'], axis=1)
    y = df['Y1_binary']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = LogisticRegression(class_weight='balanced', max_iter=1000, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    cm = confusion_matrix(y_test, y_pred)
    print('Confusion matrix:\n', cm)

    target_names = ['LowHeating', 'HighHeating']
    print('\nClassification report:\n')
    print(classification_report(y_test, y_pred, target_names=target_names))

    acc = accuracy_score(y_test, y_pred)
    print('Accuracy:', acc)

    # Plot and save confusion matrix heatmap
    plt.figure(figsize=(5,4))
    sns.heatmap(pd.DataFrame(cm), annot=True, cmap='YlGnBu', fmt='g')
    plt.title('Confusion matrix')
    plt.ylabel('Actual label')
    plt.xlabel('Predicted label')
    out_path = os.path.join(os.getcwd(), 'confusion_matrix.png')
    plt.tight_layout()
    plt.savefig(out_path)
    print('Saved confusion matrix to', out_path)

if __name__ == '__main__':
    main()
