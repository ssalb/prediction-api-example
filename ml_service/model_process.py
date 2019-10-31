import json
import config
import time
import redis
import numpy as np
from src.model import PreTrainedModel

db = redis.StrictRedis(host=config.DB_HOST, port=config.DB_PORT, db=config.DB_NAME)

if __name__ == "__main__":

    model = PreTrainedModel()

    while True:
        queue = db.lrange(config.DB_QUEUE, 0, config.BATCH_SIZE - 1)
        q_ids = []
        batch = None

        for q in queue:
            q = json.loads(q.decode("utf-8"))
            input_x = q["input"]

            if batch is None:
                batch = input_x
            else:
                batch = np.vstack([batch, input_x])

            q_ids.append(q["id"])

        if len(q_ids) > 0:
            ####################################################
            # If required, preprocess input_x here
            proc_batch = model.preprocess(batch)
            ####################################################

            preds = model.predict(proc_batch)
            for (q_id, result) in zip(q_ids, results):
                output = {"prediction": result}
                #########################################
                #
                # If required, add other metadata to output here.
                #
                #########################################
                db.set(q_id, json.dumps(output))

            db.ltrim(config.DB_QUEUE, len(q_ids), -1)

        time.sleep(config.SERVER_SLEEP)
