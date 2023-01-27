# haystack-on-sagemaker
Haystack demo on Amazon SageMaker

# Steps to set up this demo
1. This demo requires an Elasticsearch (ES) server where the documents will be stored. If you already have an ES server then you can skip this step.
  a. Spin up an EC2 instance where the ES server (and potentially also the Streamlit app) will live. Instance type `t3.medium will` be sufficient
  b. Make sure `git` is installed. If not run `sudo yum install git`
  c. Clone this repo with `git clone https://github.com/marshmellow77/haystack-on-sagemaker.git`
  d. Run the script (elasticsearch_setup.sh)[elasticsearch_setup.sh] which will set up the ES server
  e. Test if the ES server is running with the command `curl localhost:9200`
2. Once the ES server is up and running you can add documents to it and deploy the model endpoint
  a. If you want to bring your own documents, add them to the `data` folder. If the docs are in one large CSV file you can (this notebook)[00_data_prep.ipynb] to split it into individal files
  b. Once the data is ready you can load them into the ES server with notebook (01_init_es.ipynb)[01_init_es.ipynb]. Make sure to replace the `IP_ADDRESS_ES` placeholder with the IP address of the ES server
  c. Deploy the model to a SageMaker endpoint with notebook (02_deploy_model.ipynb)[02_deploy_model.ipynb]
3. Now we can set up the Web UI for the demo
  a. On the EC2 instance where you want to deploy the app (can be the same one as in step 1), run the script (streamlit_demo_setup.sh)[streamlit_demo_setup.sh], which will seut up miniconda and install the required packages
  b. You can now run the app with the command `streamlit run streamlit/app.py`
  c. Now you can navigate in the browser to `https://IP-ADDRESS:8501`, where you should see the app running
  
