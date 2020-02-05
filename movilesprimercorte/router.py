from api.viewsets import JuegosViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('juegos',JuegosViewSet)
urlpatterns = router.urls