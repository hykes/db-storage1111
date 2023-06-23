import launch

if not launch.is_installed("pymongo"):
    launch.run_pip("install pymongo", "requirements for db-storage1111")

if not launch.is_installed("pymysql"):
    launch.run_pip("install pymysql", "requirements for db-storage1111")