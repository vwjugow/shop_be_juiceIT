import awsgi
import os
from project import create_app

cfg_file = os.environ.get("FLASK_CONFIG_FILE")
app = create_app(cfg_file or "flask.cfg")


def lambda_handler(event, context):
    return awsgi.response(app, event, context, base64_content_types={"image/png"})


if __name__ == "__main__":
    print(app.url_map)
    app.run()
