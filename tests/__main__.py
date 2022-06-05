import requests
import unittest
import json
from urllib import request

PORT = 8000
HOST = f"http://localhost:{PORT}"

def post(content, to):
  print(f"url={to}")

  data = json.dumps(content)

  print(f"data: {data}")
  
  res = requests.post(to, data=json.dumps(content))
  print(f'res: {res}')

  return res.json()["json"]

class Test(unittest.TestCase):
  def test_user_regist(self):
    user = {
      "email": "guarapita_dulce@gmail.com",
      "password": "caroreña"
    }
    
    res = requests.post(f"{HOST}/regist", data=json.dumps(user))
    print(f'res={res.json()}')
    result = res.json()

    self.assertEqual(result["success"], True)
    self.assertEqual(result["new_user"]['email'], user['email'])

unittest.main()