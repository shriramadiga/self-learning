
from snowflake.snowpark.session import Session

class SnowflakeConnector():


    @staticmethod
    def get_connection():
        session = Session.builder.configs({
            'account': 'taubihu-ia48423',
            'user':'adigashriram',
            'password':'974078$Rs'
        }).getOrCreate()

        return session

if __name__ == '__main__':
    print(SnowflakeConnector.get_connection())