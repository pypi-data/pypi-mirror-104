# firebaseutils

This is a simple firebase related utils developed by JSoftwareLabs.

# Example Usage

Initialize the utils class:

```python
from jslfirebaseutils.cloudstore.cloud_store_utils import JslFirebaseUtil

# initialize the firebase utils class

jslFirebaseUtilObject = JslFirebaseUtil(
	'path to your json file credentials from firebase')
jslFirebaseUtilObject.delete_document_collection_with_contains(collection_name=u'collection name',
															   string_contains='any string which is present in your document collection')

jslFirebaseUtilObject.clear_all_collection(collection_name=u'myvaultlogsprod')

```


