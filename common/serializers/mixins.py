from rest_framework import serializers
from rest_framework.generics import get_object_or_404


class CamelCaseSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return self.camelize_data(data)

    def camelize_data(self, data):
        if isinstance(data, list):
            return [self.camelize_data(item) for item in data]
        elif isinstance(data, dict):
            return {self.camelize_key(key): self.camelize_data(value) for key, value in data.items()}
        return data

    def camelize_key(self, key):
        words = key.split("_")
        return words[0] + "".join(word.capitalize() for word in words[1:])


class ExtendedModelSerializer(CamelCaseSerializer):
    class Meta:
        abstract = True

    def get_from_url(self, lookup_field):
        assert "view" in self.context, (
            'No view context in "%s". ' "Check parameter context on function calling." % self.__class__.__name__
        )
        assert self.context["view"].kwargs.get(lookup_field), (
            'Got no data from url in  "%s". ' "Check lookup field on function calling."
        )
        value = self.context["view"].kwargs.get(lookup_field)
        return value

    def get_object_from_url(self, model, lookup_field="pk", model_field="pk"):
        obj_id = self.get_from_url(lookup_field)
        obj = get_object_or_404(queryset=model.objects.all(), **{model_field: obj_id})
        return obj
