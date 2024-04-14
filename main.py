path =  "model/encoder.pkl"
encoder = load_model(path)

path = "model/model.pkl"
model = load_model(path)

app = FastAPI() 

@app.get("/")
async def get_root():
    """ Say hello!"""
    # your code here
    return {"greeting": "Hello World!"}

@app.post("/data/")
async def post_inference(data: Data):
    # DO NOT MODIFY: turn the Pydantic model into a dict.
    data_dict = data.dict()
    # DO NOT MODIFY: clean up the dict to turn it into a Pandas DataFrame.
    # The data has names with hyphens and Python does not allow those as variable names.
    # Here it uses the functionality of FastAPI/Pydantic/etc to deal with this.
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
        # your code here
        # use data as data input
        # use training = False
        # do not need to pass lb as input    
        data,     
        cat_features,
        training=False,
        encoder=encoder,
    )        
        
    _inference = inference(model, data_processed)  # your code here to predict the result using data_processed
    return {"result": apply_label(_inference)}