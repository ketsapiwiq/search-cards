#!/bin/bash
source venv/bin/activate
until $(curl --output /dev/null -sS -X GET "elastic_knowledge:9200/_cluster/health?wait_for_status=yellow&timeout=50s"); do
    sleep 5
done

# if [$FLASK_ENV = development]
# then
#     cd app
#     npm run dev &
#     cd ..
# fi

# exec flask elastic create cards

exec flask run -h 0.0.0.0
# exec gunicorn -b :5000 --access-logfile - --error-logfile - search:app
