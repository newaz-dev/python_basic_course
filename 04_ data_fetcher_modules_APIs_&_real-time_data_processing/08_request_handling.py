# We can perform basically 4 type of request 
# 1. GET Request:----Request to "show/see" anything on website 
# 2. PUT Request:----Request to "update" anything on website
# 3. POST Request:---Request to "create" anything
# 4. DELETE Request:-Request to "Delete" anything from website
# REQUEST ------> API --------> Cycle Response
# API = Its shows 
import requests

# GET Request: 
response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response)
print(response.status_code)
print(response.json())

# POST Request:
data = {'name':'Newaz', 'id':'1', 'purpose':'test'}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json = data)
print(response.status_code)
print(response.json())


#UPDATE Request: PUT
data = {'name':'Newaz', 'id':'1', 'purpose':'update request check test 2'}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json = data)
#-------------------------------------------------------------------^^^.......
print(response.status_code)#.........................................^........
print(response.json())#..............................................^........
#....................................................................^........
# Now the question is where we want the update, how the link over will understand ?
# for that we have to add 1 indicated over '^' with this sign 
#URL taake bujhanor jonno amader id ta dhore bole dite hobe post er pore /1 ba /2 ba /id 


# DELETE Request:
data = {'name':'Newaz', 'id':'1', 'purpose':'test'}
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1", json = data)
print(response.status_code)
print(response.json())


# RESPONSE STATUS CODES LIST:

# # 1xx — Informational (request peyechi, kaj cholche)
# 100  # CONTINUE
# 101  # SWITCHING_PROTOCOLS        -> WebSocket upgrade
# 102  # PROCESSING

# # 2xx — Success
# 200  # OK                         -> normal GET success
# 201  # CREATED                    -> POST e notun data create holo
# 202  # ACCEPTED                   -> queue te niye nilam, kaj pore hobe
# 204  # NO_CONTENT                 -> success, kintu body nai (DELETE)
# 206  # PARTIAL_CONTENT            -> range request, video streaming

# # 3xx — Redirection
# 301  # MOVED_PERMANENTLY          -> URL permanent change
# 302  # FOUND                      -> temporary redirect
# 304  # NOT_MODIFIED               -> cache valid, abar pathalam na
# 307  # TEMPORARY_REDIRECT         -> method same thake
# 308  # PERMANENT_REDIRECT

# # 4xx — Client error (user/frontend er dosh)
# 400  # BAD_REQUEST                -> invalid data pathaise
# 401  # UNAUTHORIZED               -> login e koro nai / token nai
# 403  # FORBIDDEN                  -> login ache kintu permission nai
# 404  # NOT_FOUND                  -> resource nai
# 405  # METHOD_NOT_ALLOWED         -> GET er jaygay POST marse
# 409  # CONFLICT                   -> duplicate entry, already exists
# 413  # REQUEST_ENTITY_TOO_LARGE   -> file onek boro
# 415  # UNSUPPORTED_MEDIA_TYPE     -> wrong content type
# 422  # UNPROCESSABLE_ENTITY       -> FastAPI validation fail
# 429  # TOO_MANY_REQUESTS          -> rate limit

# # 5xx — Server error (tomar dosh)
# 500  # INTERNAL_SERVER_ERROR      -> code e exception
# 501  # NOT_IMPLEMENTED
# 502  # BAD_GATEWAY                -> proxy/nginx backend dhorte pare nai
# 503  # SERVICE_UNAVAILABLE        -> server down / overload
# 504  # GATEWAY_TIMEOUT