import unittest
from tool import status,summarize
class HeartbeatTests(unittest.TestCase):
 def test_states(self):self.assertEqual(status(95,100,2,10)['status'],'degraded');self.assertEqual(status(80,100,2,10)['status'],'stale');self.assertEqual(summarize([{'id':'a','last_seen':100}],100)['a']['status'],'healthy')
if __name__=='__main__':unittest.main()
