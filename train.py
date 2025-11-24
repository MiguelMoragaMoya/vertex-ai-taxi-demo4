{\rtf1\ansi\ansicpg1252\cocoartf2865
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red131\green0\blue165;\red255\green255\blue255;\red0\green0\blue0;
\red15\green112\blue1;\red0\green0\blue255;\red86\green65\blue25;\red0\green0\blue109;\red144\green1\blue18;
\red19\green85\blue52;}
{\*\expandedcolortbl;;\cssrgb\c59216\c13725\c70588;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;
\cssrgb\c0\c50196\c0;\cssrgb\c0\c0\c100000;\cssrgb\c41569\c32157\c12941;\cssrgb\c0\c6275\c50196;\cssrgb\c63922\c8235\c8235;
\cssrgb\c6667\c40000\c26667;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf0 \strokec4  pandas \cf2 \strokec2 as\cf0 \strokec4  pd\cb1 \
\cf2 \cb3 \strokec2 import\cf0 \strokec4  numpy \cf2 \strokec2 as\cf0 \strokec4  np\cb1 \
\cf2 \cb3 \strokec2 from\cf0 \strokec4  sklearn.ensemble \cf2 \strokec2 import\cf0 \strokec4  RandomForestRegressor\cb1 \
\cf2 \cb3 \strokec2 from\cf0 \strokec4  sklearn.metrics \cf2 \strokec2 import\cf0 \strokec4  mean_squared_error\cb1 \
\cf2 \cb3 \strokec2 from\cf0 \strokec4  sklearn.model_selection \cf2 \strokec2 import\cf0 \strokec4  train_test_split\cb1 \
\cf2 \cb3 \strokec2 import\cf0 \strokec4  joblib\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 #This script describe the logic used in the Notebook for Demo4\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \strokec4  \cf7 \strokec7 train_model\cf0 \strokec4 (\cf8 \strokec8 df\cf0 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3   \cf9 \strokec9 """\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf9 \cb3 \strokec9   Train the model for ETA prediction\cf0 \cb1 \strokec4 \
\cf9 \cb3 \strokec9   """\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3   \cf5 \strokec5 #1 Define columnes \cf0 \cb1 \strokec4 \
\cb3   cols = [\cf9 \strokec9 'trip_miles'\cf0 \strokec4 , \cf9 \strokec9 'pickup_community_area'\cf0 \strokec4 , \cf9 \strokec9 'dropoff_community_area'\cf0 \strokec4 , \cf9 \strokec9 'hour_of_day'\cf0 \strokec4 , \cf9 \strokec9 'day_of_week'\cf0 \strokec4 ]\cb1 \
\cb3   target = \cf9 \strokec9 'trip_seconds'\cf0 \cb1 \strokec4 \
\cb3   \cf5 \strokec5 #2 Data Preparation, X/y for test and split\cf0 \cb1 \strokec4 \
\cb3   X =  df[cols].copy().fillna(\cf10 \strokec10 0\cf0 \strokec4 )\cb1 \
\cb3   y = df[target].copy()\cb1 \
\cb3   \cf5 \strokec5 #3 Split\cf0 \cb1 \strokec4 \
\cb3   \cf7 \strokec7 print\cf0 \strokec4 (\cf9 \strokec9 "Dividing data in test and train..."\cf0 \strokec4 )\cb1 \
\cb3   X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = \cf10 \strokec10 0.75\cf0 \strokec4 , test_size = \cf10 \strokec10 0.25\cf0 \strokec4 , random_state = \cf10 \strokec10 14\cf0 \strokec4 )\cb1 \
\cb3   \cf5 \strokec5 #4 Training \cf0 \cb1 \strokec4 \
\cb3   \cf7 \strokec7 print\cf0 \strokec4 (\cf9 \strokec9 "Training RandomForest..."\cf0 \strokec4 )\cb1 \
\cb3   model = RandomForestRegressor(n_estimators=\cf10 \strokec10 20\cf0 \strokec4 , max_depth=\cf10 \strokec10 10\cf0 \strokec4 , random_state=\cf10 \strokec10 14\cf0 \strokec4 )\cb1 \
\cb3   model.fit(X_train, y_train)\cb1 \
\cb3   \cf5 \strokec5 #5 Evaluation\cf0 \cb1 \strokec4 \
\cb3   rsme = np.sqrt(mean_squared_error(y_test, model.predict(X_test)))\cb1 \
\cb3   \cf7 \strokec7 print\cf0 \strokec4 (\cf6 \strokec6 f\cf9 \strokec9 "Model Trained, RMSE: \cf0 \strokec4 \{rsme\}\cf9 \strokec9 "\cf0 \strokec4 )\cb1 \
\cb3   \cf5 \strokec5 #6 Save \cf0 \cb1 \strokec4 \
\cb3   joblib.dump(model, \cf9 \strokec9 'model.joblib'\cf0 \strokec4 )\cb1 \
\cb3   \cf7 \strokec7 print\cf0 \strokec4 (\cf9 \strokec9 "Model saved"\cf0 \strokec4 )\cb1 \
\cb3   \cf2 \strokec2 return\cf0 \strokec4  model\cb1 \
\cb3   \cb1 \
\cb3   \cf2 \strokec2 if\cf0 \strokec4  \cf8 \strokec8 __name__\cf0 \strokec4  == \cf9 \strokec9 "__main__"\cf0 \strokec4 :\cb1 \
\cb3     \cf5 \strokec5 #In the notebook the data is loaded direclty from BQ\cf0 \cb1 \strokec4 \
\cb3     model = train_model(df)\cb1 \
\cb3     \cf7 \strokec7 print\cf0 \strokec4 (\cf9 \strokec9 "This script contains the logic used in the Notebook"\cf0 \strokec4 )\cb1 \
\
\
\
}