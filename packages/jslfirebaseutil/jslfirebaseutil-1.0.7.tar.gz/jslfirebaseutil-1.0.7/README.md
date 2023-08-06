# JSLFireBaseUtils

The JSLFireBaseUtils is a basic python library for managing Firebase and CloudStore vey easily and efficiently.  We will be managing more APIs and reusable on the fly functions for Firebase. [Pypi Library](https://pypi.org/project/jslfirebaseutil/)

# Our Home page [JSoftwareLabs.com](https://www.jsoftwarelabs.com/)

## Installation

You can install the JSLFireBaseUtils from [PyPI](https://pypi.org/project/jslfirebaseutil/):

    pip install jslfirebaseutil

The jslfirebaseutil is supported on Python 3+ and above.

## How to use

# Example Usage

## Initialize the utils class:

```python
import logging
from jslfirebaseutils.cloudstore.cloud_store_utils import JslFirebaseUtil

jslFirebaseUtilObject = JslFirebaseUtil('test.json', log_level=logging.INFO)
```
## delete a document containg a string
```python
jslFirebaseUtilObject.delete_document_collection_with_contains(collection_name=u'collection name',string_contains='any string which is present in your document collection')
```
## delete a whole collection

```python
jslFirebaseUtilObject.clear_all_collection(collection_name=u'testcollection')
```

## read a document as dictionary from collection
```python

document = jslFirebaseUtilObject.read_document_as_dict(u'testcollection', id='whateverid')
print(document)
```

## Current Releases


[V1_0_7](https://github.com/JSoftwareLabs/JSLFireBaseUtils/releases/tag/V1_0_7)

