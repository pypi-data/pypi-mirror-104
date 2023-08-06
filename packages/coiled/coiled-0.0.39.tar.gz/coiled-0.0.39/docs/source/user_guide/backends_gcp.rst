GCP Backend
===========

You can have Coiled launch computations on Google Cloud Platform (GCP). Your
computations will run inside Coiled's Google Cloud account, this makes it easy
for you to get started quickly, without needing to set up any additional
infrastructure.

.. figure:: images/backend-coiled-gcp-vm.png

.. note::

   GCP support is currently experimental with new features under active
   development.

.. tip::

    In addition to the usual cluster logs, our current GCP backend support also
    includes system-level logs. This provides rich insight into any potential
    issues while GCP support is still experimental.


Switching Coiled to run on GCP
--------------------------------

To use Coiled on GCP select "GCP" in the "Cloud Backend Options" section of the
Account page of your Coiled account.


Region
------

GCP support is currently only available in the ``us-east1`` region. If you have
data in a different region on Google Cloud, you may be charged transfer fees.


GPU support
-----------

This backend allows you to run computations with GPU-enabled machines if your
account has access to GPUs. See the :doc:`GPU best practices <gpu>`
documentation for more information on using GPUs with this backend.

Workers currently have access to a single GPU, if you try to create a cluster
with more than one GPU, the cluster will not start, and an error will be
returned to you.
