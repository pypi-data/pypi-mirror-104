=============================
Multiple Select Widget
=============================

.. image:: https://badge.fury.io/py/multiple_select_widget.svg
    :target: https://badge.fury.io/py/multiple_select_widget

.. image:: https://travis-ci.org/JPolonia/multiple_select_widget.svg?branch=master
    :target: https://travis-ci.org/JPolonia/multiple_select_widget

.. image:: https://codecov.io/gh/JPolonia/multiple_select_widget/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/JPolonia/multiple_select_widget

Multiple Select Widget with autocomplete

Documentation
-------------

The full documentation is at https://multiple_select_widget.readthedocs.io.

Quickstart
----------

Install Multiple Select Widget::

    pip install multiple_select_widget

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'multiple_select_widget.apps.MultipleSelectWidgetConfig',
        ...
    )

Add Multiple Select Widget's to your forms:

.. code-block:: python

    class GroupChangeForm(forms.ModelForm):

        users = MSWModelMultipleChoiceField(
            queryset=User.objects.all(),
            required=False,
            widget=MultipleSelectWidget('Users', reverse_lazy('user_filter'), lazy=True, use_async=True),
        )

For Django Admin user register using the form

.. code-block:: python

    @admin.register(Group)
    class GroupAdmin(admin.ModelAdmin):
        form = GroupChangeForm

Add the autocomplete view MultipleSelectWidgetView to urls.py

.. code-block:: python

    ### views.py
    class UsersAutocompleteMSWView(MultipleSelectWidgetView):
        model = User
        fields = ('email__icontains',)
        obj_limit = 100

    ### urls.py
    path('user/autocomplete-msw/', UsersAutocompleteMSWView.as_view(), name='user_autocomplete_msw'),


Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
