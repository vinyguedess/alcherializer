

.. image:: https://api.codeclimate.com/v1/badges/332cfdc498df9f6dc272/maintainability
   :target: https://codeclimate.com/github/vinyguedess/alcherializer/maintainability
   :alt: Maintainability


.. image:: https://api.codeclimate.com/v1/badges/332cfdc498df9f6dc272/test_coverage
   :target: https://codeclimate.com/github/vinyguedess/alcherializer/test_coverage
   :alt: Test Coverage


Alcherializer
=============

A "Django like" model serializer.

Declaring Serializer
--------------------

.. code-block:: python

   from alcherializer import Serializer
   import sqlalchemy


   class MyModel:
       name = sqlalchemy.Column(sqlalchemy.String(100))


   class MySerializer(Serializer):
       class Meta:
           model = MyModel


   serializer = MySerializer(data={
       "name": "John Lennon"
   })
   serializer.is_valid()  # True
