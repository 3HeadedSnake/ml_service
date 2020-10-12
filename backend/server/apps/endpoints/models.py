from django.db import models

# Keep information about our endpoints
class Endpoint(models.Model):
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)

# To keep information about ML algorithms used in the service
class MLAlgorithm(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    code = models.CharField(max_length=50000)
    version = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)

#To keep information about ML algorithm statuses
class MLAlgorithmStatus(models.Model):
    status = models.CharField(max_length=128)
    active = models.BooleanField()
    created_by =  models.CharField(max_length=128)
    created_on =  models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalogirthm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE, related_name='status')

#To keep information about all requests to ML algorithms
class MLRequest(models.Model):
    input_data = models.CharField(max_length=10000)
    full_response = models.CharField(max_length=10000)
    response = models.CharField(max_length=10000)
    feedback = models.CharField(max_length=10000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE)
