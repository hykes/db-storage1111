import launch

if not launch.is_installed("pymysql"):
    launch.run_pip("install pymysql", "requirements for db-storage1111")