path =  "model/encoder.pkl"
encoder = load_model(path)

path = "model/model.pkl"
model = load_model(path)

app = FastAPI() 


#Posted at root "/" domain and will return friendly greeting to request "Hello World!"
@app.get("/")
async def get_root():
    """ Say hello!"""
    return {"greeting": "Hello World!"}

#Posted at the domain of /"data/" and 
@app.post("/data/")
async def post_inference(data: Data):
    data_dict = data.dict()
    data = {k.replace("_", "-"): [v] for k, v in data_dict.items()}
    data = pd.DataFrame.from_dict(data)

    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]
    data_processed, _, _, _ = process_data(
        data,     
        cat_features,
        training=False,
        encoder=encoder,
    )        
        
    _inference = inference(model, data_processed)
    return {"result": apply_label(_inference)}
