This is a backport package from [@timonweb](https://github.com/timonweb)'s [ClearCache](https://github.com/timonweb/django-clearcache) to Python 2.7.

# Django ClearCacheBackport

![License](https://img.shields.io/pypi/l/django-clearcache-backport)
![Django versions](https://img.shields.io/pypi/djversions/django-clearcache-backport)
![Python versions](https://img.shields.io/pypi/pyversions/django-clearcache-backport)

Allows you to clear Django cache via admin UI or manage.py command.

![demo](https://raw.githubusercontent.com/bernardoduarte/django-clearcache-backport/master/demo.gif)

## Installation

1. Install using PIP:

      ```
      pip install django-clearcache-backport
      ```

2. Add **clearcache** to INSTALLED_APPS, make sure it's above `django.contrib.admin`:

      ```
      INSTALLED_APPS += [
          ...
          'clearcache',
          'django.contrib.admin',
          ...
      ]
      ```

3. Add url to the main **urls.py** right above root admin url:
   
       ```
       urlpatterns = [
           url(r'^admin/clearcache/', include('clearcache.urls')),
           url(r'^admin/', admin.site.urls),
       ]
       ```

## Usage

### Via Django admin

1. Go to `/admin/clearcache/`, you should see a form with cache selector
2. Pick a cache. Usually there's one default cache, but can be more.
3. Click the button, you're done!

### Via manage.py command

1. Run the following command to clear the default cache

      ```
      python manage.py clearcache
      ```

2. Run the command above with an additional parameter to clear non-default cache (if exists):

      ```
      python manage.py clearcache cache_name
      ```
