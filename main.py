from fastapi import FastAPI, Request, Response, HTTPException, Header

app = FastAPI()

API_KEY = API_KEY = "testingapitokenkey1234" #testing api token key 1234

@app.get('/')
def getHome():
    return{
        "message": "this galo"
    }
@app.get("/see-headers")
def readHeaders(request: Request):
    headers = request.headers

    print(headers.items)

    user_agent = headers.get("user-agent")
    authorization = headers.get("authorization")
    custom_header = headers.get("custom-header")

    return {
        "User-Agent": user_agent,
        "Authorization": authorization,
        "Custom-Header": custom_header
    }

@app.get("/example2")
def example_endpoint():
    content = "Hello, this is the response content."

    # Create a Response object and set custom headers
    response = Response(content=content)
    response.headers["X-Custom-Header"] = "This is custom value"
    response.headers["Authorization"] = "pass_token_1234"

    return response

@app.get("/protected2")
def protect(api_key: str = Header(None)):

  if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

  return {"message":"This endpoint is protected by API Token Key.",
          "data":{"1":{"username":"lis","password":"nyamandilambung"},
                  "2":{"username":"gif","password":"whitecoffe"},
                  "3":{"username":"titan","password":"kopiluwak"}
                 }
          }