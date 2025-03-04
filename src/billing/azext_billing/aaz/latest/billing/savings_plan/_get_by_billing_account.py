# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "billing savings-plan get-by-billing-account",
)
class GetByBillingAccount(AAZCommand):
    """Get savings plan by billing account.

    :example: SavingsPlanGet
        az billing savings-plan get-by-billing-account --billing-account-name 00000000-0000-0000-0000-000000000000:00000000-0000-0000-0000-000000000000_2019-05-31 --savings-plan-order-id 20000000-0000-0000-0000-000000000000 --savings-plan-id 30000000-0000-0000-0000-000000000000
    """

    _aaz_info = {
        "version": "2024-04-01",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.billing/billingaccounts/{}/savingsplanorders/{}/savingsplans/{}", "2024-04-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.billing_account_name = AAZStrArg(
            options=["--billing-account-name"],
            help="The ID that uniquely identifies a billing account.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^([0-9]+|([Pp][Cc][Nn]\\.[A-Za-z0-9]+)|[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}(:[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}_[0-9]{4}(-[0-9]{2}){2})?)$",
            ),
        )
        _args_schema.savings_plan_id = AAZStrArg(
            options=["--savings-plan-id"],
            help="ID of the savings plan",
            required=True,
        )
        _args_schema.savings_plan_order_id = AAZStrArg(
            options=["--savings-plan-order-id"],
            help="Order ID of the savings plan",
            required=True,
        )
        _args_schema.expand = AAZStrArg(
            options=["--expand"],
            help="May be used to expand the planInformation.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.SavingsPlansGetByBillingAccount(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class SavingsPlansGetByBillingAccount(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/savingsPlanOrders/{savingsPlanOrderId}/savingsPlans/{savingsPlanId}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "billingAccountName", self.ctx.args.billing_account_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "savingsPlanId", self.ctx.args.savings_plan_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "savingsPlanOrderId", self.ctx.args.savings_plan_order_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "expand", self.ctx.args.expand,
                ),
                **self.serialize_query_param(
                    "api-version", "2024-04-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.sku = AAZObjectType(
                flags={"required": True},
            )
            _GetByBillingAccountHelper._build_schema_sku_read(_schema_on_200.sku)
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.applied_scope_properties = AAZObjectType(
                serialized_name="appliedScopeProperties",
            )
            _GetByBillingAccountHelper._build_schema_applied_scope_properties_read(properties.applied_scope_properties)
            properties.applied_scope_type = AAZStrType(
                serialized_name="appliedScopeType",
            )
            properties.benefit_start_time = AAZStrType(
                serialized_name="benefitStartTime",
                flags={"read_only": True},
            )
            properties.billing_account_id = AAZStrType(
                serialized_name="billingAccountId",
                flags={"read_only": True},
            )
            properties.billing_plan = AAZStrType(
                serialized_name="billingPlan",
            )
            properties.billing_profile_id = AAZStrType(
                serialized_name="billingProfileId",
                flags={"read_only": True},
            )
            properties.billing_scope_id = AAZStrType(
                serialized_name="billingScopeId",
            )
            properties.commitment = AAZObjectType()
            _GetByBillingAccountHelper._build_schema_commitment_read(properties.commitment)
            properties.customer_id = AAZStrType(
                serialized_name="customerId",
                flags={"read_only": True},
            )
            properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            properties.display_provisioning_state = AAZStrType(
                serialized_name="displayProvisioningState",
                flags={"read_only": True},
            )
            properties.effective_date_time = AAZStrType(
                serialized_name="effectiveDateTime",
                flags={"read_only": True},
            )
            properties.expiry_date_time = AAZStrType(
                serialized_name="expiryDateTime",
                flags={"read_only": True},
            )
            properties.extended_status_info = AAZObjectType(
                serialized_name="extendedStatusInfo",
                flags={"read_only": True},
            )
            properties.product_code = AAZStrType(
                serialized_name="productCode",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.purchase_date_time = AAZStrType(
                serialized_name="purchaseDateTime",
                flags={"read_only": True},
            )
            properties.renew = AAZBoolType()
            properties.renew_destination = AAZStrType(
                serialized_name="renewDestination",
            )
            properties.renew_properties = AAZObjectType(
                serialized_name="renewProperties",
            )
            properties.renew_source = AAZStrType(
                serialized_name="renewSource",
            )
            properties.term = AAZStrType()
            properties.user_friendly_applied_scope_type = AAZStrType(
                serialized_name="userFriendlyAppliedScopeType",
                flags={"read_only": True},
            )
            properties.utilization = AAZObjectType(
                flags={"read_only": True},
            )

            extended_status_info = cls._schema_on_200.properties.extended_status_info
            extended_status_info.message = AAZStrType()
            extended_status_info.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            extended_status_info.status_code = AAZStrType(
                serialized_name="statusCode",
            )

            properties = cls._schema_on_200.properties.extended_status_info.properties
            properties.subscription_id = AAZStrType(
                serialized_name="subscriptionId",
            )

            renew_properties = cls._schema_on_200.properties.renew_properties
            renew_properties.purchase_properties = AAZObjectType(
                serialized_name="purchaseProperties",
            )

            purchase_properties = cls._schema_on_200.properties.renew_properties.purchase_properties
            purchase_properties.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            purchase_properties.sku = AAZObjectType()
            _GetByBillingAccountHelper._build_schema_sku_read(purchase_properties.sku)

            properties = cls._schema_on_200.properties.renew_properties.purchase_properties.properties
            properties.applied_scope_properties = AAZObjectType(
                serialized_name="appliedScopeProperties",
            )
            _GetByBillingAccountHelper._build_schema_applied_scope_properties_read(properties.applied_scope_properties)
            properties.applied_scope_type = AAZStrType(
                serialized_name="appliedScopeType",
            )
            properties.billing_plan = AAZStrType(
                serialized_name="billingPlan",
            )
            properties.billing_scope_id = AAZStrType(
                serialized_name="billingScopeId",
            )
            properties.commitment = AAZObjectType()
            _GetByBillingAccountHelper._build_schema_commitment_read(properties.commitment)
            properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            properties.renew = AAZBoolType()
            properties.term = AAZStrType()

            utilization = cls._schema_on_200.properties.utilization
            utilization.aggregates = AAZListType()
            utilization.trend = AAZStrType(
                flags={"read_only": True},
            )

            aggregates = cls._schema_on_200.properties.utilization.aggregates
            aggregates.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.utilization.aggregates.Element
            _element.grain = AAZFloatType(
                flags={"read_only": True},
            )
            _element.grain_unit = AAZStrType(
                serialized_name="grainUnit",
                flags={"read_only": True},
            )
            _element.value = AAZFloatType(
                flags={"read_only": True},
            )
            _element.value_unit = AAZStrType(
                serialized_name="valueUnit",
                flags={"read_only": True},
            )

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _GetByBillingAccountHelper:
    """Helper class for GetByBillingAccount"""

    _schema_applied_scope_properties_read = None

    @classmethod
    def _build_schema_applied_scope_properties_read(cls, _schema):
        if cls._schema_applied_scope_properties_read is not None:
            _schema.display_name = cls._schema_applied_scope_properties_read.display_name
            _schema.management_group_id = cls._schema_applied_scope_properties_read.management_group_id
            _schema.resource_group_id = cls._schema_applied_scope_properties_read.resource_group_id
            _schema.subscription_id = cls._schema_applied_scope_properties_read.subscription_id
            _schema.tenant_id = cls._schema_applied_scope_properties_read.tenant_id
            return

        cls._schema_applied_scope_properties_read = _schema_applied_scope_properties_read = AAZObjectType()

        applied_scope_properties_read = _schema_applied_scope_properties_read
        applied_scope_properties_read.display_name = AAZStrType(
            serialized_name="displayName",
        )
        applied_scope_properties_read.management_group_id = AAZStrType(
            serialized_name="managementGroupId",
        )
        applied_scope_properties_read.resource_group_id = AAZStrType(
            serialized_name="resourceGroupId",
        )
        applied_scope_properties_read.subscription_id = AAZStrType(
            serialized_name="subscriptionId",
        )
        applied_scope_properties_read.tenant_id = AAZStrType(
            serialized_name="tenantId",
        )

        _schema.display_name = cls._schema_applied_scope_properties_read.display_name
        _schema.management_group_id = cls._schema_applied_scope_properties_read.management_group_id
        _schema.resource_group_id = cls._schema_applied_scope_properties_read.resource_group_id
        _schema.subscription_id = cls._schema_applied_scope_properties_read.subscription_id
        _schema.tenant_id = cls._schema_applied_scope_properties_read.tenant_id

    _schema_commitment_read = None

    @classmethod
    def _build_schema_commitment_read(cls, _schema):
        if cls._schema_commitment_read is not None:
            _schema.amount = cls._schema_commitment_read.amount
            _schema.currency_code = cls._schema_commitment_read.currency_code
            _schema.grain = cls._schema_commitment_read.grain
            return

        cls._schema_commitment_read = _schema_commitment_read = AAZObjectType()

        commitment_read = _schema_commitment_read
        commitment_read.amount = AAZFloatType()
        commitment_read.currency_code = AAZStrType(
            serialized_name="currencyCode",
        )
        commitment_read.grain = AAZStrType()

        _schema.amount = cls._schema_commitment_read.amount
        _schema.currency_code = cls._schema_commitment_read.currency_code
        _schema.grain = cls._schema_commitment_read.grain

    _schema_sku_read = None

    @classmethod
    def _build_schema_sku_read(cls, _schema):
        if cls._schema_sku_read is not None:
            _schema.name = cls._schema_sku_read.name
            return

        cls._schema_sku_read = _schema_sku_read = AAZObjectType()

        sku_read = _schema_sku_read
        sku_read.name = AAZStrType()

        _schema.name = cls._schema_sku_read.name


__all__ = ["GetByBillingAccount"]
