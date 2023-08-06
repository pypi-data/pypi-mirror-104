## deed - Python

ActivityFormatter for object changes (auditlog)

### Usage

Try it on your python console:

```python
from deed import AuditLog, AuditMode

# stored resource
resource = {'_id': '123', 'user_id': '123',
            'customer_id': '123',
            'title': "My amazing post"}
refs = [  # stakeholders
    'post:' + resource['_id'],
    'owner:' + resource['user_id'],
    'customer:' + resource['customer_id'],
]

# update example
audit_log = AuditLog(resource_type='shipment',
                     action='update', audit_mode=AuditMode.DIFF)
audit_log.session(actor='user:admin@example.com', where='10.0.0.2',
                  channel='edit-form', stakeholders=refs)

patch = {'title': 'My first post'}
new_resource = {**resource, **patch}
audit_log.audit(resource, payload=new_resource)
```
