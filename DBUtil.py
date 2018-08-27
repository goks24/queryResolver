import pymysql
import config as cfg

class DBUtil(object):
    def __init__(self):
        pass

    def initDB(self):
        connection = pymysql.connect(host=cfg.HOST,port=int(cfg.PORT),
                                          user=cfg.USER,
                                          password=cfg.PASSWORD,
                                          db=cfg.DB,
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)


        cfg.logger.info("Database Connection successful..")
        return connection
        

    def selectQuery(self,query,connection):
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                cfg.logger.info("Query is executed successfully..")
                return result

        except Exception as e:
                cfg.logger.error("Error in query execution")
                result = {
                    "message": "Error in executing the Query"
                }
                return result
        finally:
                cfg.logger.info("Database Connection is terminated..")
                connection.close()
                

    def insertQuery(self,query,param,TABLE_NAME,connection):
        try:
            with connection.cursor() as cursor:
                
                # Count the rows before inserting the new record
                beforeRowCount_query = "select count(*) from "+TABLE_NAME
                cursor.execute(beforeRowCount_query)
                beforeRowCount = cursor.fetchone()
                
                # Inserting new record to the databse
                cursor.execute(query,param)
                connection.commit()
                cfg.logger.info("Query is executed successfully..")
                
                # Count the rows before inserting the new record
                afterRowCount_query = "select count(*) from "+TABLE_NAME
                cursor.execute(afterRowCount_query)
                afterRowCount = cursor.fetchone()
                
                
                result = {
                    "message": "Record is inserted successfully",
                    "beforeInsertionCount":  beforeRowCount['count(*)'],
                    "afterInsertionCount":  afterRowCount['count(*)']
                }
                return result

        except Exception as e:
                cfg.logger.error("Error in query execution")
                result = {
                    "message": "Error in executing the Query"
                }
                return result
        finally:
                cfg.logger.info("Database Connection is terminated..")
                connection.close()
                

    def updateQuery(self,query,param,connection):
        try:
            with connection.cursor() as cursor:
                cursor.execute(query,param)
                connection.commit()
                cfg.logger.info("Query is executed successfully..")
                result = {
                    "message": "Record is updated successfully"
                }
                return result

        except Exception as e:
                cfg.logger.error("Error in query execution")
                result = {
                    "message": "Error in executing the Query"
                }
                return result
        finally:
                cfg.logger.info("Database Connection is terminated..")
                connection.close()
