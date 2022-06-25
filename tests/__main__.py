import requests
import unittest
import json
from urllib import request

PORT = 8000
HOST = f"http://localhost:{PORT}"

class Test(unittest.TestCase):
  
  #unittest.skip('')
  def test_user_routes(self):
    # REGIST...
    print('[!] Registing user...')
    user = {
      "name": "guarapita",
      "lastname": "acida",
      "email": "guarapita_dulce@gmail.com",
      "password": "caroreña",
      "cedula": 12345
    }
    
    res = requests.post(f"{HOST}/users", data=json.dumps(user))
    result = res.json()

    self.assertEqual(result["success"], True)
    self.assertEqual(result["new_user"]['email'], user['email'])
    user['id'] = result["new_user"]['id']

    # now, AUTH...

    print('[!] Authenticating user...')
    auth_user = {
      "email": user['email'],
      "password": user['password']
    }

    res = requests.post(f"{HOST}/auth", data=json.dumps(auth_user))

    result = res.json()
    self.assertTrue(result['success'])
    self.assertEqual(result['user']['id'], user['id'])
    self.assertEqual((len(result['token']) > 7), True)

    # now, DELETE..., if is 0 not run
    if 1:
      print('[t] deleting user...')
      res = requests.delete(f"{HOST}/users/{user['id']}")
      result = res.json()
      self.assertTrue(result['success'])  

  #@unittest.skip('for now')
  def test_forms_routes(self):
    print('[!] Creating form...')
    form = {
      "name": "Formulario de Douglas",
      "items": '{"msg": "hola mundo"}',
      "id_creator": "1"
      
    }
    
    res = requests.post(f"{HOST}/forms", data=json.dumps(form))
    result = res.json()
    self.assertTrue(result['success'], True)
    form['id'] = result['form']['id']

    # now, to find the form with resived id
    print('[!] Retriving form...')

    res = requests.get(f"{HOST}/forms/{form['id']}")
    result = res.json()
    self.assertEqual(result['form']['id'], form['id'])
    self.assertEqual(result['form']['name'], form['name'])
    
    # now, to delete the form
    print('[!] Deleting form...')

    res = requests.delete(f"{HOST}/forms/{form['id']}")
    result = res.json()
    self.assertTrue(result['success'])

  def test_mod_user(self):
    
    return
    
unittest.main()