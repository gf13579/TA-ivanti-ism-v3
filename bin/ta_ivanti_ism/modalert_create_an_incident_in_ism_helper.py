import ism
# encoding = utf-8

def process_event(helper, *args, **kwargs):

    helper.log_info("Alert action create_an_incident_in_ism started.")

    username = helper.get_global_setting("username")
    password = helper.get_global_setting("password")
    api_key= helper.get_global_setting("api_key")

    tenant = helper.get_global_setting("tenant")
    #helper.log_info("tenant={}".format(tenant))
    api_key = helper.get_global_setting("api_key")
    #helper.log_info("api_key={}".format(api_key))
    role = helper.get_global_setting("role")
    #helper.log_info("role={}".format(role))

    customer = helper.get_param("customer")
    #helper.log_info("customer={}".format(customer))
    summary = helper.get_param("summary")
    #helper.log_info("summary={}".format(summary))
    description = helper.get_param("description")
    #helper.log_info("description={}".format(description))
    status = helper.get_param("status")
    #helper.log_info("status={}".format(status))
    custom_fields = helper.get_param("custom_fields")
    #helper.log_info("custom_fields={}".format(custom_fields))
    incident_type = helper.get_param("incident_type")
    #helper.log_info("custom_fields={}".format(custom_fields))

    helper.log_info("Calling ism.authenticate")
    auth_token = ism.authenticate(helper=helper,base_url=tenant,username=username,password=password,role=role, api_key=api_key)
    

    helper.log_info("calling ism.create_incident")
    ret_val = ism.create_incident(auth_token, tenant, customer, summary, description, status, custom_fields, helper=helper, incident_type=incident_type)

    helper.log_info("create_incident return value={}".format(ret_val))

    return 0
