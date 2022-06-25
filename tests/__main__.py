import requests
import unittest
import json
from urllib import request

PORT = 8000
HOST = f"http://localhost:{PORT}"

class Test(unittest.TestCase):
  '''
  @unittest.skip('kaslñfjalskjf')
  def sssstest_user_regist(self):
    user = {
      "email": "guarapita_dulce@gmail.com",
      "password": "caroreña"
    }
    
    res = requests.post(f"{HOST}/regist", data=json.dumps(user))
    print(f'res={res.json()}')
    result = res.json()

    self.assertEqual(result["success"], True)
    self.assertEqual(result["new_user"]['email'], user['email'])

  @unittest.skip('kaslñfjalskjf')
  def test_auth(self):
    user = {
      "email": "guarapita_dulce@gmail.com",
      "password": "caroreña"
    }

    res = requests.post(f"{HOST}/auth", data=json.dumps(user))
    print(f'res_raw={res}')
    print(f'res={res.json()}')

    result = res.json()
    self.assertEqual(result['success'], True)
    self.assertEqual((len(result['token']) > 7), True)
  '''

  def test_forms(self):
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

    res = requests.get(f"{HOST}/forms/{form['id']}")
    result = res.json()
    self.assertEqual(result['form']['id'], form['id'])
    self.assertEqual(result['form']['name'], form['name'])
    
    # now, to delete the form
    
    res = requests.delete(f"{HOST}/forms/{form['id']}")
    result = res.json()
    self.assertTrue(result['success'])
    
unittest.main()