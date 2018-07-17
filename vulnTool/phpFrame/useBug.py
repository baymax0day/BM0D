
pluginName = "zabbix_latest_sql.py"

pluginName = pluginName.split('.')[0]

eval("import "+ pluginName)
eval(pluginName+".get_plugin_info()")

