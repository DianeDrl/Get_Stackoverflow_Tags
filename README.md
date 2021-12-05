# Get Tags for Stackoverflow questions

This repo contains the codes of a web framework on which we can get approproate tags for a question that we would ask on Stackoverflow. Tags are predicted from a machine learning model using a Multilable Text classification algorithm, a Linear Support Vector Classification. 

![alt text](https://github.com/DianeDrl/Get_Stackoverflow_Tags/blob/main/flask.png?raw=true)

requirements.txt contains the recommended versions of the packages used for working API. 

### Web Framework : Flask

app.py contains the code for the Flask frameworks.

    python app.py

### Machine Learning Model

tdidfvectorizer_body.pkl contains the model to transform the cleaned text of the question into numbers. 

svc_tfi.pkl contains the machine learning model to predict tags of the question. 

word_list.txt contains the dictionnary of all possible tags from the train exemples. 

stackoverflow_predict_tags.py contains the code to clean the text and then predict the tags using tdidfvectorizer_body.pkl, svc_tfi.pkl and word_list.txt. 

### Web Framework design 

templates/index.html contains the design of the web framework 

static/Get_Keywords.js contains AJAX request to print the predict tags on web framework 

![alt text](https://github.com/DianeDrl/Get_Stackoverflow_Tags/blob/main/Request_exemple.png?raw=true)
