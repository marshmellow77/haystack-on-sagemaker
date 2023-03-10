# haystack-on-sagemaker
![Screenshot](images/screenshot.png)

# Acknowledgement
This is an adaptation of [Deepset's Haystack tutorial on basic Q&A systems](https://haystack.deepset.ai/tutorials/01_basic_qa_pipeline) to run it on [Amazon SageMaker](https://aws.amazon.com/sagemaker/).

# Steps to set up this demo
1. This demo requires an Elasticsearch (ES) server where the documents will be stored. If you already have an ES server then you can skip this step.
    1. Spin up an EC2 instance where the ES server (and potentially also the Streamlit app) will live. Instance type `t3.medium will` be sufficient
    2. Make sure that port 9200 is open to connect to the ES server
    3. Make sure `git` is installed. If not run `sudo yum install git`
    4. Clone this repo with `git clone https://github.com/marshmellow77/haystack-on-sagemaker.git`
    5. Run the script [elasticsearch_setup.sh](elasticsearch_setup.sh) which will set up the ES server
    6. Test if the ES server is running with the command `curl localhost:9200`
2. Once the ES server is up and running you can add documents to it and deploy the model endpoint
    1. If you want to bring your own documents, add them to the `data` folder. If the docs are in one large CSV file you can [this notebook](00_data_prep.ipynb) to split it into individal files
    2. Once the data is ready you can load them into the ES server with notebook [01_init_es.ipynb](01_init_es.ipynb). Make sure to replace the `IP_ADDRESS_ES` placeholder with the IP address of the ES server
    3. In the [inference script](model/code/inference.py), make sure you also replace the placeholder for the ES server with the actual IP address
    4. Deploy the model to a SageMaker endpoint with notebook [02_deploy_model.ipynb](02_deploy_model.ipynb)
3. Now we can set up the Web UI for the demo
    1. On the EC2 instance where you want to deploy the app (can be the same one as in step 1), run the script [streamlit_demo_setup.sh](streamlit_demo_setup.sh), which will seut up miniconda and install the required packages
    2. Make sure port 8501 is open to connect to the Streamlit application
    3. You can now run the app with the command `streamlit run streamlit/app.py`
    4. Now you can navigate in the browser to `https://IP-ADDRESS:8501`, where you should see the app running
  
# Architecture diagram
![Architecture diagram](images/architecture.png)