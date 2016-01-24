from swampdragon import route_handler
from swampdragon.route_handler import ModelPubRouter
from .models import Notification
from .serializers import NotificationSerializer


# Using SwampDragon routers to deal with the data we're passing
class NotificationRouter(ModelPubRouter):
    valid_verbs = ['subscribe']
    route_name = 'notifications'
    model = Notification
    serializer_class = NotificationSerializer


route_handler.register(NotificationRouter)