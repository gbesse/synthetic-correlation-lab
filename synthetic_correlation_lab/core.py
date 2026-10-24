import random,math
from .common import number,integer

def run(data):
 rho=number(data['latent_correlation'],-1,1);count=integer(data.get('count',1000),2,10000);seed=integer(data.get('seed',0),0,2**53-1);rng=random.Random(seed);margins=data['margins']
 if not isinstance(margins,list)or len(margins)!=2:raise ValueError('margins')
 distributions=[]
 for margin in margins:
  values=margin['values'];probs=margin['probabilities']
  if not isinstance(values,list)or not 1<=len(values)<=100 or len(values)!=len(probs)or any(not isinstance(v,str)for v in values)or len(values)!=len(set(values)):raise ValueError('categories')
  for p in probs:number(p,0,1)
  if abs(math.fsum(probs)-1)>1e-12:raise ValueError('probabilities')
  cumulative=[];s=0
  for p in probs:s+=p;cumulative.append(s)
  distributions.append((values,cumulative))
 def choose(u,distribution):
  vals,probs=distribution
  return vals[next((i for i,p in enumerate(probs)if u<p),len(vals)-1)]
 rows=[];counts=[{v:0 for v in dist[0]}for dist in distributions];pairs={}
 for _ in range(count):
  x=rng.gauss(0,1);z=rng.gauss(0,1);y=rho*x+math.sqrt(max(0,1-rho*rho))*z;u=.5*(1+math.erf(x/math.sqrt(2)));v=.5*(1+math.erf(y/math.sqrt(2)));a=choose(u,distributions[0]);b=choose(v,distributions[1]);rows.append([a,b]);counts[0][a]+=1;counts[1][b]+=1;pairs[(a,b)]=pairs.get((a,b),0)+1
 return {'rows':rows,'marginal_counts':counts,'joint_counts':[{'values':list(k),'count':v}for k,v in sorted(pairs.items())],'latent_correlation':rho,'seed':seed,'model':'bivariate_gaussian_copula_discrete_quantiles_finite_sample_margins_not_exact'}
