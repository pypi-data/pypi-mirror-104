from localstack.utils.aws import aws_models
udCKR=super
udCKY=None
udCKL=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  udCKR(LambdaLayer,self).__init__(arn)
  self.cwd=udCKY
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class BaseComponent(aws_models.Component):
 def name(self):
  return self.udCKL.split(':')[-1]
class RDSDatabase(BaseComponent):
 def __init__(self,udCKL,env=udCKY):
  udCKR(RDSDatabase,self).__init__(udCKL,env=env)
class RDSCluster(BaseComponent):
 def __init__(self,udCKL,env=udCKY):
  udCKR(RDSCluster,self).__init__(udCKL,env=env)
class AppSyncAPI(BaseComponent):
 def __init__(self,udCKL,env=udCKY):
  udCKR(AppSyncAPI,self).__init__(udCKL,env=env)
class AmplifyApp(BaseComponent):
 def __init__(self,udCKL,env=udCKY):
  udCKR(AmplifyApp,self).__init__(udCKL,env=env)
class ElastiCacheCluster(BaseComponent):
 def __init__(self,udCKL,env=udCKY):
  udCKR(ElastiCacheCluster,self).__init__(udCKL,env=env)
class TransferServer(BaseComponent):
 def __init__(self,udCKL,env=udCKY):
  udCKR(TransferServer,self).__init__(udCKL,env=env)
class CloudFrontDistribution(BaseComponent):
 def __init__(self,udCKL,env=udCKY):
  udCKR(CloudFrontDistribution,self).__init__(udCKL,env=env)
class CodeCommitRepository(BaseComponent):
 def __init__(self,udCKL,env=udCKY):
  udCKR(CodeCommitRepository,self).__init__(udCKL,env=env)
# Created by pyminifier (https://github.com/liftoff/pyminifier)
