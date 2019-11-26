import os
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()

def run():
    """
    Populate a MongoDB instance running on localhost:27017 using region data
    from raw_data.csv
    """
    
    basedir = os.path.abspath(os.path.dirname(__file__))
    raw_data_path = basedir + '/raw_data.csv'

    connection = MongoClient(os.environ["DATABASE_URL"])

    try:
        connection.shipping.command(
            "dropUser",
            os.environ['MONGO_INITDB_ROOT_USERNAME'],
        )
    except:
        pass

    connection.drop_database('shipping')

    connection.shipping.command(
        "createUser",
        os.environ['MONGO_INITDB_ROOT_USERNAME'],
        pwd=os.environ['MONGO_INITDB_ROOT_PASSWORD'],
        roles=[{'role':'readWrite','db':'shipping'}]
    )

    with open(raw_data_path, 'r') as fh:
        data = fh.read().split('\n')
        fields = data[0]
        idx_fields = {k:i for i, k in enumerate(fields.split(','))}
        data = data[1:]
        data = [line.split(',') for line in data]

        docs = [
            {   
                "base_price": int(line[idx_fields["base_price"]]),
                "num_days": int(line[idx_fields["num_days"]]),
                "region": {
                    "state": line[idx_fields["state"]],
                    "start_zipcode": int(line[idx_fields["start_zipcode"]]),
                    "end_zipcode": int(line[idx_fields["end_zipcode"]]),
                    "max_base_items": int(line[idx_fields["max_base_items"]]),
                    "extra_item_tax": float(line[idx_fields["extra_item_tax"]])
                }
            } for line in data
        ]
 
    connection.shipping.zipcode_fee.insert_many(docs)


run()