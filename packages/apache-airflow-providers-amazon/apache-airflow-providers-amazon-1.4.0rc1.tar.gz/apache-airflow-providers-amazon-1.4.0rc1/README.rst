
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


Package ``apache-airflow-providers-amazon``

Release: ``1.4.0rc1``


Amazon integration (including `Amazon Web Services (AWS) <https://aws.amazon.com/>`__).


Provider package
================

This is a provider package for ``amazon`` provider. All classes for this provider package
are in ``airflow.providers.amazon`` python package.

You can find package information and changelog for the provider
in the `documentation <https://airflow.apache.org/docs/apache-airflow-providers-amazon/1.4.0/>`_.


Installation
============

You can install this package on top of an existing airflow 2.* installation via
``pip install apache-airflow-providers-amazon``

PIP requirements
================

==============  ====================
PIP package     Version required
==============  ====================
``boto3``       ``>=1.15.0,<1.18.0``
``watchtower``  ``~=0.7.3``
==============  ====================

Cross provider package dependencies
===================================

Those are dependencies that might be needed in order to use all the features of the package.
You need to install the specified provider packages in order to use them.

You can install such cross-provider dependencies when installing from PyPI. For example:

.. code-block:: bash

    pip install apache-airflow-providers-amazon[apache.hive]


==============================================================================================================  ===============
Dependent package                                                                                               Extra
==============================================================================================================  ===============
`apache-airflow-providers-apache-hive <https://airflow.apache.org/docs/apache-airflow-providers-apache-hive>`_  ``apache.hive``
`apache-airflow-providers-exasol <https://airflow.apache.org/docs/apache-airflow-providers-exasol>`_            ``exasol``
`apache-airflow-providers-ftp <https://airflow.apache.org/docs/apache-airflow-providers-ftp>`_                  ``ftp``
`apache-airflow-providers-google <https://airflow.apache.org/docs/apache-airflow-providers-google>`_            ``google``
`apache-airflow-providers-imap <https://airflow.apache.org/docs/apache-airflow-providers-imap>`_                ``imap``
`apache-airflow-providers-mongo <https://airflow.apache.org/docs/apache-airflow-providers-mongo>`_              ``mongo``
`apache-airflow-providers-mysql <https://airflow.apache.org/docs/apache-airflow-providers-mysql>`_              ``mysql``
`apache-airflow-providers-postgres <https://airflow.apache.org/docs/apache-airflow-providers-postgres>`_        ``postgres``
`apache-airflow-providers-ssh <https://airflow.apache.org/docs/apache-airflow-providers-ssh>`_                  ``ssh``
==============================================================================================================  ===============