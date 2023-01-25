from haystack.nodes import BM25Retriever
from haystack.nodes import FARMReader
from haystack.pipelines import ExtractiveQAPipeline
from haystack.document_stores import ElasticsearchDocumentStore
import json


def dumper(obj):
    try:
        return obj.toJSON()
    except:
        return obj.__dict__


def model_fn(model_dir):
    document_store = ElasticsearchDocumentStore(
        host=<IP address of ES server>,
        port=9200,
        index="document"
    )
    
    retriever = BM25Retriever(document_store=document_store)
    reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=True)
    pipe = ExtractiveQAPipeline(reader, retriever)
    
    return pipe


def predict_fn(data, pipe):
    query = data.pop("inputs")
    params = data.pop("parameters", None)
    print(params)
    prediction = pipe.run(query=query, params=params)
    
    for a in prediction['answers']:
        print(f"Answer: {a.answer}, Confidence: {a.score*100:.1f}%, Context: {a.context}\n")
        
    response = json.dumps(prediction, default=dumper)
    
    return {"response": response}
    