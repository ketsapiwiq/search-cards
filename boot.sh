#!/bin/bash
source venv/bin/activate

# if [$FLASK_ENV = development]
# then
#     cd app
#     npm run dev &
#     cd ..
# fi


# flask db init
exec flask db migrate
exec flask db upgrade


exec flask run -h 0.0.0.0

# exec gunicorn -b :5000 --access-logfile - --error-logfile - search:app
