API_HOSTS = {
    "test": "http://host.docker.internal:7888/site/wp-json/wc/v3/",
    "dev": "",
    "prod": ""
}
#http://localhost:7888/site
WOO_API_HOSTS = {
    "test": "http://192.168.1.23/site/",
    "dev": "",
    "prod": ""
}

DB_HOST = {
    'machine1': {
        "test": {
                    "host": "127.0.0.1",
                    "database": "site",
                    "table_prefix": "wp_",
                    "socket": None,
                    "port": "8889"
        }
    }
}