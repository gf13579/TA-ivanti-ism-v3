import ism
# encoding = utf-8

def process_event(helper, *args, **kwargs):
    """
    # IMPORTANT
    # Do not remove the anchor macro:start and macro:end lines.
    # These lines are used to generate sample code. If they are
    # removed, the sample code will not be updated when configurations
    # are updated.

    [sample_code_macro:start]

    # The following example gets and sets the log level
    helper.set_log_level(helper.log_level)

    # The following example gets the setup parameters and prints them to the log
    tenant = helper.get_global_setting("tenant")
    helper.log_info("tenant={}".format(tenant))
    api_key = helper.get_global_setting("api_key")
    helper.log_info("api_key={}".format(api_key))
    username = helper.get_global_setting("username")
    helper.log_info("username={}".format(username))
    password = helper.get_global_setting("password")
    helper.log_info("password={}".format(password))
    role = helper.get_global_setting("role")
    helper.log_info("role={}".format(role))
    verify_server_certificate = helper.get_global_setting("verify_server_certificate")
    helper.log_info("verify_server_certificate={}".format(verify_server_certificate))

    # The following example gets the alert action parameters and prints them to the log
    customer = helper.get_param("customer")
    helper.log_info("customer={}".format(customer))

    summary = helper.get_param("summary")
    helper.log_info("summary={}".format(summary))

    description = helper.get_param("description")
    helper.log_info("description={}".format(description))

    status = helper.get_param("status")
    helper.log_info("status={}".format(status))

    custom_fields = helper.get_param("custom_fields")
    helper.log_info("custom_fields={}".format(custom_fields))

    incident_type = helper.get_param("incident_type")
    helper.log_info("incident_type={}".format(incident_type))


    # The following example adds two sample events ("hello", "world")
    # and writes them to Splunk
    # NOTE: Call helper.writeevents() only once after all events
    # have been added
    helper.addevent("hello", sourcetype="sample_sourcetype")
    helper.addevent("world", sourcetype="sample_sourcetype")
    helper.writeevents(index="summary", host="localhost", source="localhost")

    # The following example gets the events that trigger the alert
    events = helper.get_events()
    for event in events:
        helper.log_info("event={}".format(event))

    # helper.settings is a dict that includes environment configuration
    # Example usage: helper.settings["server_uri"]
    helper.log_info("server_uri={}".format(helper.settings["server_uri"]))
    [sample_code_macro:end]
    """

    helper.log_info("Alert action create_an_incident_in_ism started.")

    username = helper.get_global_setting("username")
    password = helper.get_global_setting("password")
    api_key= helper.get_global_setting("api_key")
    opt_verify= helper.get_global_setting("verify_server_certificate")
    
    if opt_verify=="False":
        opt_verify=False
    else:
        opt_verify=True

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
    auth_token = ism.authenticate(helper=helper,base_url=tenant,username=username,password=password,role=role, api_key=api_key, verify=opt_verify)
    

    helper.log_info("calling ism.create_incident")
    ret_val = ism.create_incident(auth_token, tenant, customer, summary, description, status, custom_fields, helper=helper,verify=opt_verify, incident_type=incident_type)

    helper.log_info("create_incident return value={}".format(ret_val))

    return 0
