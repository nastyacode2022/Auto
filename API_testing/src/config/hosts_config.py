API_HOSTS = {
    "test": "http://localhost:7888/site/wp-json/wc/v3/",
    "dev": "",
    "prod": ""
}
#http://localhost:7888/site
#http://host.docker.internal:7888/site

DB_HOST = {
    'machine1': {
        "test": {
                    "host": "localhost",
                    "database": "site",
                    "table_prefix": "wp_",
                    "socket": None,
                    "port": 8889
        }
    },
    'docker': {
            "test": {
                        "host": "host.docker.internal",
                        "database": "site",
                        "table_prefix": "wp_",
                        "socket": None,
                        "port": 8889
            }
        }
}