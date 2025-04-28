# django-grist-loader

Django reusable app to load data from Grist into read-only Django models.

## Installation

The usual way:

1. Install
   ```shell
   uv add django-grist-loader
   ```

2. Configure

   Django's settings:
   ```python
   INSTALLED_APPS = (
       ...,
       "grist_loader",
       ...,
   )
   
   GRIST_PYGRISTER_CONFIG = {
       "GRIST_API_KEY": os.environ.get("GRIST_API_KEY", ""),
       "GRIST_SELF_MANAGED": "Y",
       "GRIST_SELF_MANAGED_HOME": f"{os.environ.get('GRIST_PROTOCOL', 'https://')}{os.environ.get('GRIST_HOST', '')}",
       "GRIST_SELF_MANAGED_SINGLE_ORG": "N",
       "GRIST_SERVER_PROTOCOL": os.environ.get("GRIST_PROTOCOL", "https://"),
       "GRIST_API_SERVER": os.environ.get("GRIST_HOST", ""),
       "GRIST_API_ROOT": os.environ.get("GRIST_API_ROOT", "api"),
       "GRIST_TEAM_SITE": os.environ.get("GRIST_API_DOCS", "docs"),
       "GRIST_WORKSPACE_ID": os.environ.get("GRIST_WORKSPACE_ID", ""),
       "GRIST_DOC_ID": os.environ.get("GRIST_DOC_ID", ""),
       "GRIST_RAISE_ERROR": "Y",
       "GRIST_SAFEMODE": "N",
   } 
   ```
3. Define the required envvars that make sense to your project

## Usage

1. Define a Django model that subclasses `GristModel`:

    ```python
   from django.db import models
   from grist_loader.models import GristModel


   class MyModel(GristModel):
       my_char_field = models.CharField(max_length=100)
       my_int_field = models.IntegerField()
       my_date_field = models.DateField()
    ```
2. Within a `grist.py` module, define a loader class that subclasses `GristLoader`:

    ```python
   from django.conf import settings
   from grist_loader.loader import GristLoader, register_grist_loader

   from .models import MyModel


   @register_grist_loader
   class MyLoader(GristLoader):
       model = MyModel
       pygrister_config = settings.GRIST_PYGRISTER_CONFIG
       table = "MyGristTableName"
       required_cols = ("MyChar",)
       fields = {
         "MyChar": MyModel.my_char_field,
         "MyInt": MyModel.my_int_field,
         "MyDate": MyModel.my_date_field,
       }
       filter = {
           "MyChar": ["some value"],
       }
    ```
3. Load your data
   ```shell
   python manage.py grist_load_all
   ```
4. Profit!