#
# {
#   "version": 2,
#   "builds": [
#     { "src": "main.py", "use": "@vercel/python" }
#   ],
#   "routes": [
#     { "src": "/(.*)", "dest": "/main.py" }
#   ],
#   "env": {
#     "APP_MODULE": "main:app"
#   }
# }