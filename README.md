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
