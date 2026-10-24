import unittest
from synthetic_correlation_lab import run
class Tests(unittest.TestCase):
 def data(self,rho):return {'latent_correlation':rho,'count':1000,'seed':3,'margins':[{'values':['a','b'],'probabilities':[.5,.5]},{'values':['a','b'],'probabilities':[.5,.5]}]}
 def test_perfect_latent_correlation_matches_quantiles(self):self.assertTrue(all(a==b for a,b in run(self.data(1))['rows']))
 def test_negative_correlation_reverses_symmetric_quantiles(self):self.assertTrue(all(a!=b for a,b in run(self.data(-1))['rows']))
 def test_counts_conserve_rows_and_seed_is_replayable(self):
  d=self.data(.2);r=run(d);self.assertEqual(r,run(d));self.assertTrue(all(sum(c.values())==1000 for c in r['marginal_counts']));self.assertEqual(sum(c['count']for c in r['joint_counts']),1000)
 def test_zero_probability_category_not_selected(self):
  d=self.data(0);d['margins'][0]['probabilities']=[0,1];self.assertTrue(all(a=='b'for a,b in run(d)['rows']))
 def test_invalid_probability_mass_rejected(self):
  d=self.data(0);d['margins'][0]['probabilities']=[.2,.2]
  with self.assertRaises(ValueError):run(d)
