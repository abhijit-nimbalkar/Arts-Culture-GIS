MY_GOOGLE_API_KEY='AIzaSyCAmdbHoQiKeX_qoq55UsTK59X7rakrzPk'
MY_WHOPER_DUCK_KEY='8e7b26e6-8ff5-49d0-8a0c-73792f1d6244'
def query_resource(site,query):
    import ckanapi
    ckan = ckanapi.RemoteCKAN(site)
    response = ckan.action.datastore_search_sql(sql=query)
    return response['records']
