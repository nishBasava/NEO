import pandas as pd
from utils.data_preprocessing import preprocess_data, split_data
from train.train_ann import train_ann
from train.train_rnn import train_rnn

# Load data
df_train = pd.read_csv('data/mmp_train_df.csv')
df_test = pd.read_csv('data/mmp_test_df.csv')

# Data Preprocessing
df_train = preprocess_data(df_train)
df_test = preprocess_data(df_test)

# Split data
X_train, X_val, X_test, y_train, y_val, y_test = split_data(df_train.drop('epitope status', axis=1), df_train['epitope status'])

# Train models
train_ann(X_train, y_train, X_val, y_val)
train_rnn(X_train, y_train, X_val, y_val)

