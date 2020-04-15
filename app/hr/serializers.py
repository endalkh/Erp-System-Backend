from rest_framework import serializers
from .models import *


class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = claimModel
        fields = "__all__"
        depth = 2


class RoleSerializer(serializers.ModelSerializer):
    role_levels = ClaimSerializer(many=True, read_only=True,)

    class Meta:
        model = RoleModel
        fields = "__all__"


class EmployeReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeModel
        fields = "__all__"
        depth = 1


class DepartmentSerializer(serializers.ModelSerializer):

    department_roles = RoleSerializer(many=True, read_only=True,)
    department_employes = EmployeReadSerializer(many=True, read_only=True,)

    class Meta:
        model = DepartmentModel
        fields = ("departmentName", "department_roles", "department_employes")
        depth = 1


class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeModel
        fields = "__all__"


class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CatagoryModel
        fields = "__all__"


class InventoryItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItemModel
        fields = "__all__"
        depth = 1


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    item_order = ItemSerializer(many=True)

    class Meta:
        model = OrderModel
        fields = [
            "orderid",
            "orderNumber",
            "company",
            "orderName",
            "salesPerson",
            "description",
            "orderDate",
            "shipmentAddress",
            "item_order",
        ]

    def create(self, validated_data):
        items_data = validated_data.pop("item_order")
        order = OrderModel.objects.create(**validated_data)
        for item_data in items_data:
            ItemModel.objects.create(order=order, **item_data)
        return order


class OrderReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = "__all__"


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusModel
        fields = "__all__"


class ShipmentScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipmentScheduleModel
        fields = "__all__"


class SivSerializer(serializers.ModelSerializer):
    class Meta:
        model = sivModel
        fields = "__all__"
