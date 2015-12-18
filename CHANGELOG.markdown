# django-watson changelog

## 1.2.0 - 03/12/2015

- **Breaking:** Updated the location of [search](https://github.com/etianen/django-watson/wiki/Searching-models) and
    [registration](https://github.com/etianen/django-watson/wiki/Registering-models) methods.
    Prior to this change, you could access the these methjods using the following import:

    ```py
    # Old-style import for accessing the search and registration methods.
    import watson

    # Use register and search methods from the watson namespace.
    watson.register(YourModel)
    watson.search("foo")
    ```

    In order to support Django 1.9, the search and registration
    methods have been moved to the following import:

    ```py
    # New-style import for accesssing the search and registration methods.
    from watson import search as watson

    # Use register and search methods from the watson namespace.
    watson.register(YourModel)
    watson.search("foo")
    ```

- **Breaking:** Updated the location of [admin classes](https://github.com/etianen/django-watson/wiki/Admin-integration).

    Prior to this change, you could access the `SearchAdmin` class using the following import:

    ```py
    # Old-style import for accessing the admin class.
    import watson

    # Access admin class from the watson namespace.
    class YourModelAdmin(watson.SearchAdmin):
        ...
    ```

    In order to support Django 1.9, the admin class has been moved to the following
    import:

    ```py
    # New-style import for accesssing admin class.
    from watson.admin import SearchAdmin

    # Use the admin class directly.
    class YourModelAdmin(SearchAdmin):
        ...
    ```

- Django 1.9 compatibility (@etianen).


## 1.1.9 - 09/11/2015

- Customization meta serialization (@samuelcolvin).
- Minor bugfixes (@etianen, @Fitblip).


## 1.1.8 - 24/04/2015

- Minor bugfixes.


## 1.1.7 - 06/04/2015

- Included south_migrations in the source distribution.


## 1.1.6 - 01/04/2015

- Added listwatson management command (@philippeowagner)
- Added _format_query() hook to MySQL search backend (@alexey-grom)
- Adding in Django 1.7 migrations.
- Ability to specify a search backend name for the filter() and search() methods (@amin-pylot)
- Bugfixes and tweaks (@thedrow, @dessibelle, @carltongibson, @philippeowagner)



## 1.1.5 - 08/11/2014

- Fixing issue with indexing nullable ForeignKey fields.


## 1.1.4 - 14/10/2014

- skip_index_update() context manager (@moggers87)
- Improved Travis CI integration (@thedrow)
- Minor bug fixes (@bdauvergne, @moggers87, @Gzing)


## 1.1.3 - 19/02/2014

- Ability to search for terms with apostrophes.
- Ability to rebuild watson indices for specific models.


## 1.1.2 - 05/10/2013

- More memory-efficient buildwatson command using data chunking.
- Python 3.3 compatibility (new and experimental!).
- Various minor bugfixes.


## 1.1.1 - 19/07/2012

- Ability to use a custom search adapter class in SearchAdmin.
- Template tag helpers for search results.
- Ability to specify search configuration for PostgreSQL backend.


## 1.1.0 - 05/04/2012

- Django 1.4 admin compatibility.
- Improved efficiency of large search index updates using update and bulk_create (when available).
- Added in SearchContextMiddleware.
- Removed potentially unreliable automatic wrapping of entire request in a search context.
- Improved escaping of PostgreSQL query characters.


## 1.0.2 - 07/03/2012

- Support for prefix matching in search queries.


## 1.0.1 - 06/02/2012

- Removing hacky searchentry_set generic relation being applied to registered models, which was causing spurious deletion warnings in the admin interface.


## 1.0.0 - 10/10/2012

- First production release.
