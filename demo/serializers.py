from swampdragon.serializers.model_serializer import ModelSerializer

# Need a serializer to publish the messages
class NotificationSerializer(ModelSerializer):
	class Meta:
		model = 'demo.Notification'
		publish_fields = ['message']