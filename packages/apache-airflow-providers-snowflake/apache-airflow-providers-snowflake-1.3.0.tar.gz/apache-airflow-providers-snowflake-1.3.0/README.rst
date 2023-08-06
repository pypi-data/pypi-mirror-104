
.. Licensed to the Apache Software Foundation (ASF) under one
   or more contributor license agreements.  See the NOTICE file
   distributed with this work for additional information
   regarding copyright ownership.  The ASF licenses this file
   to you under the Apache License, Version 2.0 (the
   "License"); you may not use this file except in compliance
   with the License.  You may obtain a copy of the License at

..   http://www.apache.org/licenses/LICENSE-2.0

.. Unless required by applicable law or agreed to in writing,
   software distributed under the License is distributed on an
   "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
   KIND, either express or implied.  See the License for the
   specific language governing permissions and limitations
   under the License.


Package ``apache-airflow-providers-snowflake``

Release: ``1.3.0``


`Snowflake <https://www.snowflake.com/>`__


Provider package
================

This is a provider package for ``snowflake`` provider. All classes for this provider package
are in ``airflow.providers.snowflake`` python package.

You can find package information and changelog for the provider
in the `documentation <https://airflow.apache.org/docs/apache-airflow-providers-snowflake/1.3.0/>`_.


Installation
============

You can install this package on top of an existing airflow 2.* installation via
``pip install apache-airflow-providers-snowflake``

PIP requirements
================

==============================  ==================
PIP package                     Version required
==============================  ==================
``snowflake-connector-python``  ``>=2.4.1``
``snowflake-sqlalchemy``        ``>=1.1.0``
==============================  ==================

Cross provider package dependencies
===================================

Those are dependencies that might be needed in order to use all the features of the package.
You need to install the specified provider packages in order to use them.

You can install such cross-provider dependencies when installing from PyPI. For example:

.. code-block:: bash

    pip install apache-airflow-providers-snowflake[slack]


==================================================================================================  =========
Dependent package                                                                                   Extra
==================================================================================================  =========
`apache-airflow-providers-slack <https://airflow.apache.org/docs/apache-airflow-providers-slack>`_  ``slack``
==================================================================================================  =========