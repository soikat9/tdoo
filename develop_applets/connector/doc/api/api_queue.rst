.. _api-queue:

#####
Queue
#####

Models
******

.. automodule:: tele.applets.queue_job.models.base
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: tele.applets.queue_job.models.queue_job

   .. autoclass:: QueueJob

     .. autoattribute:: _name
     .. autoattribute:: _inherit

***
Job
***

.. automodule:: tele.applets.queue_job.job

   Decorators
   ==========

   .. autofunction:: job
   .. autofunction:: related_action

   Internals
   =========

   .. autoclass:: DelayableRecordset
      :members:
      :undoc-members:
      :show-inheritance:

   .. autoclass:: Job
      :members:
      :undoc-members:
      :show-inheritance:
